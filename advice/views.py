from django.shortcuts import render
import openai
import googlemaps
from django.conf import settings

# print(f"Google Maps API Key: {settings.GOOGLEMAPS_API_KEY}")
# Create your views here.
gmaps = googlemaps.Client(key=settings.GOOGLEMAPS_API_KEY)
openai.api_key = settings.OPENAI_API_KEY


# function to generate the response for user acccording to their text(that they are asking)
def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        #The messages parameter contains a list of chat messages, where the user's message is specified by the prompt.
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=2500, #Specifies the maximum number of tokens (words) in the generated text.
        n=1, #give only one response for the the requests
        stop=None,  #Indicates that the model should continue generating text until it reaches the specified token limit.
        temperature=0.5, #Controls the randomness of the generated text.
        stream=False #Specifies that the response should not be streamed.
    )
    return response["choices"][0].message["content"]  #choices is the openai documented variable to generate the response from OpenAI.
                                                      #[0] means retrieve the first choice from the list of choices 
                                                      
                                                
def home(request):#request is the http request that server recieved from client(browser)
    #defining the request operaton i.e,POST
    if request.method== "POST":
        lat= request.POST['latitude']
        lng=request.POST['longitude']
        
        if lat and lng:
            reverse_geocode_result=gmaps.reverse_geocode((lat,lng)) #reverse_geocode is done to make location for human readability
            city=None
            country= None
            for result in reverse_geocode_result:
                if 'locality' in result['types']:
                    city=result['address_components'][0]['long_name'] #address_components is the part of rev_geocdng which contains 
                                                                    #    info about the address components of a location
                elif 'country' in result['types']:
                    country=result['address_components'][0]['long_name'] #long_name is used to access the human readable, full name of
                                                                         #an address component

            if city and country:
                place_results=gmaps.places(query=f'tourists attraction in {city}, {country}', type='tourist_attraction')       
                place_names=[]
                for place in place_results['results']: #results is the key whithin the dictionary returned by the "gmaps.places"
                    place_names.append(place['name']) #name is the key whithin the dictionary present in "results"
                
                #creating a common seperated string from list of string
                places_str=", ".join(place_names) #using "join" method to concatenate the elements of 'place_names' list into 
                                                  #a single STRING
                
                locations = []
                if places_str:
                    for place in place_results['results']:
                        location={
                            'name': place['name'],
                            'lat': place['geometry']['location']['lat'],
                            'lng': place['geometry']['location']['lng']
                        }
                        locations.append(location)
                        
                        content = f"Call me Travel Partner. Help me as a tourist guide for only the top 5 important places in {city} city: {places_str}. Describe them wildly and excitingly. Be funny. Explain in 50 words.Write in English. Use emojis at the end of sentences. Use paragraphs."
                            
                else:
                    content = f"Call me Travel Partner. Tell me there are no any place to visit in this {city} city. Ask if I can find another spot on Earth. Be funny. Explain very briefly. Write in English."
                    
                print(city)
                print(places_str)
                
                text=generate_text(content)
                data = {
                    'content': text,
                    'lat': lat,
                    'lng': lng,
                    'locations': locations
                }
                
                return render(request, "advice.html", data)
            
            else:
                content = f"Call me Travel Partner. Say there aren't many places to visit here. Ask if I can't find another spot on Earth. Be funny. Explain briefly. Write in English."
                text = generate_text(content)
                data = {
                    'content': text,
                    'lat': lat,
                    'lng': lng
                }
                return render(request, 'advice.html', data)
            
        else:
            data = {'content': "First, mark a place on the map where you want to find visiting places"}
            return render(request, "home.html", data)
        
    else:
        return render(request, "home.html")

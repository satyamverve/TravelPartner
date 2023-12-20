Travel Partner - Django Tourist Guide:

Description:

I have developed the Travel Partner - Django Tourist Guide application to provide online tourist guide services to users. The application empowers users to explore tourist attractions in a city by connecting them to a selected location on a world map. Users can mark points of interest on the map, click the "Get Recommendations" button, and access highlighted tourist spots in the associated city. Moreover, the application generates a concise summary of the tourist guide, presenting information about activities and attractions in the marked locations. To build this application, I utilized HTML, CSS, and JavaScript for the frontend, while the backend leverages the Django framework and Python programming language. The map functionality relies on the Google Maps API, tourist spot retrieval is facilitated by the Google Places API, and the OpenAI ChatGPT API is employed to generate the tourist guide text. By sending the coordinates obtained from Google Maps as a prompt to the ChatGPT API, the guide text is dynamically created. I have created this platform with the intention of sharing it with others on GitHub.


Installation:

To install and run the application locally, follow these steps:

Clone the repository:
>>git clone https://github.com/satyamverve/travelpartner-django.git

Navigate to the project directory:
>>cd project_directory

Install the required packages by running the following command:
>>pip install -r requirements.txt

>Obtain the necessary API keys:
>>Google Maps API: Visit the Google Cloud Console (https://console.cloud.google.com/) to create a project and generate an API key. Enable the Maps JavaScript API, Places API, and Geocoding API for your project.

>>OpenAI ChatGPT API: Obtain an API key from OpenAI (https://platform.openai.com/account/api-keys/) to use the ChatGPT API.
Update API keys in the application: Open the settings.py file located at boosttravel/settings.py. In this file, replace the placeholders GOOGLEMAPS_API_KEY and OPENAI_API_KEY with your own API keys. Additionally, in the HTML files within the Templates folder (advice/templates), make sure to replace the placeholder GOOGLEMAPS_API_KEY with your own API key.

>Run the development server:
>>python manage.py runserver

>>Access the application in your web browser: http://localhost:8000/
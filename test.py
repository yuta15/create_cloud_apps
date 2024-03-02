import json
import os
import webbrowser

import requests


nasa_api_key = os.environ.get('NASA_API_KEY')
api_url = 'https://api.nasa.gov/planetary/apod?api_key={}'.format(nasa_api_key)


def use_requests(api_url):

    response = requests.get(api_url)
    json_response = json.loads(response.text)
    # photo_url = json_response['date']
    return json_response



print(use_requests(api_url))
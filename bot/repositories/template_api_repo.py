from pipes import Template


import requests
import os
import logging

class TemplateApiRepository:
    API_URL = os.getenv('API_URL', 'http://crash:8080')
    logging.info(f'API_URL: {API_URL}')

    async def get_example_data():
        response = requests.get(TemplateApiRepository.API_URL + '/example')
        return response.json()
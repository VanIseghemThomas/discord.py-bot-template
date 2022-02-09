from pipes import Template

import requests
import os
import logging

class TemplateApiRepository:
    API_URL = os.getenv('API_URL', 'http://fastapi:8080')
    logging.info(f'API_URL: {API_URL}')

    async def get_example_data():
        try:
            response = requests.get(TemplateApiRepository.API_URL + '/example')
            return response.json()

        except Exception as e:
            logging.error(e)
            return {"data": "Error, API service is not available"}
import logging as logger
from lib.helpers.api_helpers import *
import requests
import os
import ast
from urllib.parse import urlencode

import pdb

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.http_conn = requests.Session()

    def retrieve_reg_token(self):
        response = self.http_conn.get(os.environ["REGISTER_API_HOST"])
        token = response.headers["Set-Cookie"].split(";")[0]
        return token

    def register_user(self, user):
        headers = ast.literal_eval(os.environ["API_HEADERS"])
        headers.update({"Cookie": self.retrieve_reg_token()})
        payload = urlencode(generate_user_payload(user))
        response = self.http_conn.post(os.environ["REGISTER_API_HOST"], data=payload, headers=headers)
        logger.debug(f"\nRegister user: {user},\nStatus code: {response.status_code}")

        match response.status_code:
            case 200:
                logger.info(f"Request was successful: {response.status_code}")
            case range(400, 499):
                logger.info(f"Client error occurred: {response.status_code}")
            case range(500, 599):
                logger.info(f"Server error occurred: {response.status_code}")
            case _:
                logger.info(f"Unexpected status code: {response.status_code}")

        return response

    def api_get(self, url, payload, **kwargs):
        pass

import requests

from config.config import Config
from utils.logger import get_logger

logger = get_logger()

class APIClient:

    def post(self, endpoint, payload= None):
        logger.info(f"POST request to {endpoint}")
        response = requests.post(
            f"{Config.BASE_URL}"
            f"{endpoint}",
            json=payload
        )
        logger.info(
            f"Response code: "
            f"{response.status_code}"
        )
        return response
        
    def get(self, endpoint):
        logger.info(
            f"GET request to {endpoint}"
        )
        return requests.get(
            f"{Config.BASE_URL}"
            f"{endpoint}"
        )
import requests
import logging
from abc import ABC, abstractmethod


# Abstract base class

class AbstractHttpRequest(ABC):
    """
    Abstract base class that defines the method signatures for an HTTP request.
    It includes common functionality like base_url, headers, token-based auth, and timeout handling.
    """

    def __init__(self, base_url=None, headers=None, token=None, timeout=None):
        """
        Initialize the HTTP request with base_url, headers, token, and timeout.
        :param base_url: The base URL of the API
        :param headers: Any default headers to be passed
        :param token: Authentication token (optional)
        :param timeout: Request timeout in seconds (optional)
        """
        self.base_url = base_url
        self.timeout = timeout
        self.headers = headers if headers else {}

        # If a token is provided, add it to the Authorization header
        if token:
            self.headers['Authorization'] = f'Bearer {token}'

    def _build_url(self, endpoint):
        """
        Build the full URL using base_url and endpoint.
        :param endpoint: The API endpoint
        :return: Full URL string
        """
        if self.base_url:
            return f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        return endpoint

    @abstractmethod
    def send_request(self, endpoint, **kwargs):
        """
        Abstract method for sending a request. Must be implemented by subclasses.
        :param endpoint: The API endpoint
        :param kwargs: Additional parameters specific to the HTTP method
        """
        pass


# GET Request Class
class GetRequest(AbstractHttpRequest):
    """
    Handles GET requests.
    """

    def __init__(self, base_url=None, headers=None, token=None, timeout=None):
        """
        Initialize the GET request class.
        """
        super().__init__(base_url, headers, token, timeout)

    def send_request(self, endpoint, params=None, headers=None):
        """
        Send a GET request.
        :param endpoint: The API endpoint
        :param params: Query parameters
        :param headers: Additional headers for this request
        :return: The response JSON or None in case of failure
        """
        url = self._build_url(endpoint)
        try:
            logging.info(f"GET request to {url} with params: {params}")
            response = requests.get(
                url, params=params, headers={**self.headers, **(headers or {})}, timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"GET request failed: {e}")
            return None


# POST Request Class
class PostRequest(AbstractHttpRequest):
    """
    Handles POST requests.
    """

    def __init__(self, base_url=None, headers=None, token=None, timeout=None):
        """
        Initialize the POST request class.
        """
        super().__init__(base_url, headers, token, timeout)

    def send_request(self, endpoint, data=None, json=None, headers=None):
        """
        Send a POST request.
        :param endpoint: The API endpoint
        :param data: Form data
        :param json: JSON body
        :param headers: Additional headers for this request
        :return: The response JSON or None in case of failure
        """
        url = self._build_url(endpoint)
        try:
            logging.info(f"POST request to {url} with data: {data}, json: {json}")
            response = requests.post(
                url, data=data, json=json, headers={**self.headers, **(headers or {})}, timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"POST request failed: {e}")
            return None


# PATCH Request Class
class PatchRequest(AbstractHttpRequest):
    """
    Handles PATCH requests.
    """

    def __init__(self, base_url=None, headers=None, token=None, timeout=None):
        """
        Initialize the PATCH request class.
        """
        super().__init__(base_url, headers, token, timeout)

    def send_request(self, endpoint, data=None, json=None, headers=None):
        """
        Send a PATCH request.
        :param endpoint: The API endpoint
        :param data: Form data
        :param json: JSON body
        :param headers: Additional headers for this request
        :return: The response JSON or None in case of failure
        """
        url = self._build_url(endpoint)
        try:
            logging.info(f"PATCH request to {url} with data: {data}, json: {json}")
            response = requests.patch(
                url, data=data, json=json, headers={**self.headers, **(headers or {})}, timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"PATCH request failed: {e}")
            return None


# DELETE Request Class
class DeleteRequest(AbstractHttpRequest):
    """
    Handles DELETE requests.
    """

    def __init__(self, base_url=None, headers=None, token=None, timeout=None):
        """
        Initialize the DELETE request class.
        """
        super().__init__(base_url, headers, token, timeout)

    def send_request(self, endpoint, headers=None):
        """
        Send a DELETE request.
        :param endpoint: The API endpoint
        :param headers: Additional headers for this request
        :return: The response JSON or None in case of failure
        """
        url = self._build_url(endpoint)
        try:
            logging.info(f"DELETE request to {url}")
            response = requests.delete(
                url, headers={**self.headers, **(headers or {})}, timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"DELETE request failed: {e}")
            return None

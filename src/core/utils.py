"""
core utils.
"""
import requests


class EmailHunterClient:
    """
    Use emailhunter.co for verifying email existence on signup. 
    """
    def __init__(self, api_key, api_version='v1'):
        self.api_key = api_key
        self.api_version = api_version
        self.base_url = 'https://api.emailhunter.co/{}/'.format(api_version)

    def _make_request(self, url, payload):
        r = requests.get(url, params=payload)
        data = r.json()
        r.raise_for_status()

        return data

    def exist(self, email):
        """
        Checks if a given email address has been found in the EmailHunter base and returns the sources.
        :param email: the email address you want to check
        :return: Tuple, 'exist' (boolean) and sources (list of dicts)
        """
        url = self.base_url + 'exist'
        payload = {'api_key': self.api_key, 'email': email}
        data = self._make_request(url, payload)

        return data['exist'], data['sources']

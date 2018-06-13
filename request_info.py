import time, requests
from vultrBase import VultrError
import json
import vultrBase
class vultr_Request(Vultr):
    def request(self, path, params={}, method='GET'):
        _start = time.time()

        if not path.startswith('/'):
            path = '/' + path
        url = self.api_endpoint + path

        try:
            if method == 'POST':
                if (self.api_key):
                    query = {'api_key': self.api_key}
                resp = requests.post(url, params=query, data=params,
                                     timeout=60)
            elif method == 'GET':
                if (self.api_key):
                    params['api_key'] = self.api_key
                resp = requests.get(url, params=params, timeout=60)
            else:
                raise VultrError('Unsupported method %s' % method)

        except requests.RequestException as e:  # errors from requests
            raise RuntimeError(e)

        if resp.status_code != 200:
            if resp.status_code == 400:
                raise VultrError('Invalid API location. Check the URL that' +
                                 ' you are using')
            elif resp.status_code == 403:
                raise VultrError('Invalid or missing API key. Check that' +
                                 ' your API key is present and matches' +
                                 ' your assigned key')
            elif resp.status_code == 405:
                raise VultrError('Invalid HTTP method. Check that the' +
                                 ' method (POST|GET) matches what the' +
                                 ' documentation indicates')
            elif resp.status_code == 412:
                raise VultrError('Request failed. Check the response body ' +
                                 'for a more detailed description. Body: \n' +
                                 resp.text)
            elif resp.status_code == 500:
                raise VultrError('Internal server error. Try again at a' +
                                 ' later time')
            elif resp.status_code == 503:
                raise VultrError('Rate limit hit. API requests are limited' +
                                 ' to an average of 1/s. Try your request' +
                                 ' again later.')

        # very simplistic synchronous rate limiting;
        _elapsed = time.time() - _start
        if (_elapsed < self.requestDuration):
            time.sleep(self.requestDuration - _elapsed)

        # return an empty json object if the API
        # doesn't respond with a value.
        if not resp.text:
            return json.loads('{}')
        else:
        return resp.json()

    def account(self):

    def application(self):

    def api_key(self):

    def backup(self):

    def bare_metal(self):

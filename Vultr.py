import json
import requests

API_BASE_ADDR = 'https://api.vultr.com'


def http_response_code(code):

    state = {
        200:'Function successfully executed.',
        400:'Invalid API location. Check the URL that you are using.',
        403:'Invalid or missing API key. Check that your API key is present and matches your assigned key.',
        405:'Invalid HTTP method. Check that the method (POST|GET) matches what the documentation indicates.',
        412:'Request failed. Check the response body for a more detailed description.',
        500:'Internal server error. Try again at a later time.',
        503:'Rate limit hit. API requests are limited to an average of 2/s. Try your request again later.'
    }
    return state[code]



def os_list(self):
    """
    /v1/os/list
    GET - public
    Retrieve a list of available operating systems. If the 'windows' flag
    is true, a Windows licenses will be included with the instance, which
    will increase the cost.

    Example Request:
    GET https://api.vultr.com/v1/os/list
    Example Response:
    {
        "127": {
            "OSID": "127",
            "name": "CentOS 6 x64",
            "arch": "x64",
            "family": "centos",
            "windows": false
        },
        "148": {
            "OSID": "148",
            "name": "Ubuntu 12.04 i386",
            "arch": "i386",
            "family": "ubuntu",
            "windows": false
        }
    }
    Parameters:
    No Parameters
    """
    return self.request('/v1/os/list')

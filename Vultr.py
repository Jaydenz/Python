import json
import requests

API_BASE_ADDR = 'https://api.vultr.com'
API_KEY = 'CDWQ2PYLN4IC3IOFCFLSHCJ74E4DSFHM3FDA'


# class VultrError(RuntimeError):
#     pass

# class Vultr(object):
#     def __init__(self, apikey, requestpath):
#         self.apikey = apikey
#         self.requestpath = requestpath
    
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



def list_server(self):
    




def list_snapshot:
    curl -H 'API-Key: YOURKEY' https://api.vultr.com/v1/snapshot/list

def create_snapshot:
    curl -H 'API-Key: YOURKEY' https://api.vultr.com/v1/snapshot/create --data 'SUBID=1312965'
    '''成功返回{
                "SNAPSHOTID": "544e52f31c706"
            }'''
def destroy_snapshot:
    curl -H 'API-Key: YOURKEY' https://api.vultr.com/v1/snapshot/destroy --data 'SNAPSHOTID=5359435d28b9a'



if __name__ == "__main__":
    

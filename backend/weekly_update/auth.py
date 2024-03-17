import requests
import os

WEEKLY_CLIENT_ID = os.environ.get("CLIENT_ID")
WEEKLY_REDIRECT_URI = os.environ.get('REDIRECT_URI')

WEEKLY_SCOPE = 'playlist-modify-public user-follow-read'

def request_authorization(correlation_id: str):
    body = {
      'response_type': 'code',
      'client_id': WEEKLY_CLIENT_ID,
      'scope': WEEKLY_SCOPE,
      'redirect_uri': WEEKLY_REDIRECT_URI,
      'state': correlation_id
    }

    print(body)

    url = 'https://accounts.spotify.com/authorize?' + '&'.join(f'{key}={val}' for key, val in body.items())
    return url
    
    # if not resp.ok:
    #     raise Exception(f'Response not OK: [{resp.status_code}]\n{resp.text}')
from requests_oauthlib import OAuth2Session

with open('creds.txt') as file:
    creds = file.read().splitlines()
    CLIENT_ID = creds[0]
    CLIENT_SECRET = creds[1]

REDIRECT_URI='oob'
# REDIRECT_URI='https://localhost/'
scopes=['fspt-w']

yahoo = OAuth2Session(CLIENT_ID,
                      # client_secret=CLIENT_SECRET,
                      scope=scopes,
                      redirect_uri=REDIRECT_URI)
authorization_url, state = yahoo.authorization_url(
        'https://api.login.yahoo.com/oauth2/request_auth',
        prompt="login",
        nonce="noncestring")

print('Please go to %s and authorize access.' % authorization_url)
auth_code = input('Enter the auth code given: ')

token = yahoo.fetch_token(
        'https://api.login.yahoo.com/oauth2/get_token',
        code=auth_code,
        # Yahoo specific extra parameter used for client authentication
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)

r = yahoo.get('https://fantasysports.yahooapis.com/fantasy/v2/game/nfl')
# Enjoy =)

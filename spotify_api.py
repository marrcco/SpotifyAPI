import requests
import base64

class SpotifyAPI:
    client_id = None
    client_secret = None

    def __init__(self,client_id,client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_creds(self):
        # combine client id and client secret
        return f"{self.client_id}:{self.client_secret}"

    def get_token_params(self):
        # one of spotifys required params
        return {"grant_type" : "client_credentials"}

    def get_token_header(self):
        # token header required to authoirze user
        return {
            "Authorization" : f"Basic {base64.b64encode(self.get_client_creds().encode()).decode()}", # required to convert client creds to base64
            "Content-Type" : "application/x-www-form-urlencoded"
            }

    def get_access_token(self):
        # using client_id and client_secret in order to get token
        # token is needed to send requests to Spotify API
        token_url = "https://accounts.spotify.com/api/token"
        r = requests.post(token_url, data=self.get_token_params(), headers=self.get_token_header())  # sending request to get token
        req_json = r.json()
        access_token = req_json["access_token"]
        return access_token

    def get_track_data(self,track_id):
        # pulls all publicly available data for required track
        headers = {"Authorization" : f"Bearer {self.get_access_token()}"}
        url = "https://api.spotify.com/v1/tracks"
        curl = f"{url}/{track_id}"
        r = requests.get(curl,headers=headers).json()
        return r

    def get_aritst(self,artist_id):
        # pulls all publicly available data for artist
        headers = {"Authorization": f"Bearer {self.get_access_token()}"}
        url = "https://api.spotify.com/v1/artists"
        curl = f"{url}/{artist_id}"
        r = requests.get(curl, headers=headers).json()
        return r

    def get_artist_albums(self,artist_id):
        # returns all albums from artist
        headers = {"Authorization": f"Bearer {self.get_access_token()}"}
        url = "https://api.spotify.com/v1/artists"
        curl = f"{url}/{artist_id}/albums"
        r = requests.get(curl, headers=headers).json()
        return r


api = SpotifyAPI(client_id="95f368d4307141009e9cb23bedacb8a9",client_secret="0d2dfa1fb06445a9a05359335286d5db")
drake = api.get_artist_albums(artist_id="3TVXtAsR1Inumwj472S9r4")
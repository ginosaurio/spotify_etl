import spotipy
from spotipy.oauth2 import SpotifyOAuth
from cfg import CLIENT_ID, CLIENT_SECRET, SPOTIPY_REDIRECT_URI


def extract(date, limit=50):
    """Get limit elements from last listen tracks
    Args:
        ds (datetime): Date to query
        limit (int): Limit of element to query
    """
    
    scope = "user-read-recently-played"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri=SPOTIPY_REDIRECT_URI,
                                                scope=scope))


    ds = int(date.timestamp()) * 1000
    return sp.current_user_recently_played(limit=limit, after=ds)
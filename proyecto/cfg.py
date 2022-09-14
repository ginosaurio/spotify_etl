from decouple import RepositoryIni, Config
from sqlalchemy import create_engine
import pathlib

L_DIR = str(pathlib.Path(__file__).parent.absolute())

config = Config(RepositoryIni('C:\project\Spotify\proyecto\settings.ini'))


CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = config("SPOTIPY_REDIRECT_URI")
DB_CONNSTR = config("DB_CONNSTR")

engine = create_engine(DB_CONNSTR) if DB_CONNSTR else None

TABLE_INFO = ["history"]

print(L_DIR)
from cfg import DB_CONNSTR, L_DIR, TABLE_INFO
from sqlalchemy import text
from sqlalchemy import create_engine

engine = create_engine(DB_CONNSTR)
#log = logging.getLogger()


def create_tables():


    with engine.connect() as con:
        for file in TABLE_INFO:
            #print(file)
            with open(L_DIR+'/sql/' f"{file}.sql") as f:
                query = text(f.read())
            con.execute(f"DROP TABLE IF EXISTS {file}")
            con.execute(query)
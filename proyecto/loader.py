from cfg import DB_CONNSTR, TABLE_INFO
from sqlalchemy import create_engine

def load(df):
    print(f"Uploading {df.shape[0]} to pg")
    engine = create_engine(DB_CONNSTR)
    df.to_sql(TABLE_INFO[0], con=engine, index=False, if_exists='replace')
from sqlalchemy import create_engine
import psycopg2
from cfg import DB_CONNSTR

engine = create_engine(DB_CONNSTR) if DB_CONNSTR else None
#meta = MetaData(engine)
#Base = declarative_base(metadata=meta)

TABLENAME = "history_sql"

#class SpotipyOut(Base):
#    __tablename__ = TABLENAME
#    
#    played_at = Column(TIMESTAMP, primary_key=True)
#    artist = Column(String(255), nullable=False)
#    track = Column(String(255), nullable=False)
    
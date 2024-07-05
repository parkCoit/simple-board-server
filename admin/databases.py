from sqlalchemy import create_engine

from admin.env import CHARSET, DB_URL

ENGINE = create_engine(DB_URL, encoding=CHARSET, echo=True)
conn = ENGINE.connect()

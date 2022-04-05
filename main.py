from fastapi import FastAPI

from db.db_config import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()

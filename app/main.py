from fastapi import FastAPI
from app.routes.route import router
from app.database.database import Base,engine

app = FastAPI()

app.include_router(router)

Base.metadata.create_all(bind=engine)

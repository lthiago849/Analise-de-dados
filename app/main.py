from fastapi import FastAPI
from views import router

app = FastAPI(title= "API de analise estudantil", version="1.0")
app.include_router(router)
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import routers

app = FastAPI(title="M.J. Ammaar | Official Website")

if not os.path.exists("uploads"):
    os.makedirs("uploads")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="uploads"), name="static")
app.include_router(routers.router)


@app.get("/")
async def serve_home():
    return FileResponse("index.html")
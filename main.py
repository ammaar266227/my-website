import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import routers

app = FastAPI(title="M.J. Ammaar | Official Website")

# Safely check for uploads folder without trying to create directories on read-only server
if os.path.exists("uploads"):
    app.mount("/static", StaticFiles(directory="uploads"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.router)


@app.get("/")
async def serve_home():
    return FileResponse("index.html")
import os
from datetime import datetime
from fastapi import APIRouter, Form, HTTPException

router = APIRouter(prefix="/api")

PROFILE_DATA = {
    "name": "M.J. Ammaar",
    "title": "Graphic Designer & Harball Cricket Player",
    "bio": "Welcome to my official personal hub! Expressing creativity through design and passion on the cricket field.",
    "email": "ammaarmj123@gmail.com",
    "instagram": "https://www.instagram.com/ammaar_266227/",
    "twitter": "https://x.com/ammaar_266227",
    "youtube": "https://www.youtube.com/channel/UCpAt3g657AyZgPqvNVgNXRQ",
    "tiktok": "https://www.tiktok.com/@ammaar_266227",
    "stat1_label": "Community Members",
    "stat1_val": "1,200+",
    "stat2_label": "Projects Completed",
    "stat2_val": "50+",
    "photo_url": "20241106_172219.png",
}

messages_db = [
    {
        "name": "Alex",
        "message": "Awesome website! Keep making great designs and cricket plays.",
        "time": "2026-08-24 10:15",
    }
]


@router.get("/profile")
async def get_profile():
    return PROFILE_DATA


@router.get("/messages")
async def get_messages():
    return messages_db


@router.post("/messages")
async def add_message(name: str = Form(...), message: str = Form(...)):
    if not name.strip() or not message.strip():
        raise HTTPException(
            status_code=400, detail="Name and message are required."
        )

    new_entry = {
        "name": name.strip(),
        "message": message.strip(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    messages_db.insert(0, new_entry)
    return {"status": "success", "messages": messages_db}
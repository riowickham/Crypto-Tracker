from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from signals import get_all_signals
from utils import send_email, load_json, save_json
import os

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File paths
USERS_FILE = "users.json"
WATCHLIST_FILE = "watchlists.json"

users = load_json(USERS_FILE, {})
watchlists = load_json(WATCHLIST_FILE, {})

@app.get("/")
def home():
    return {"message": "Crypto Stock Backend Running"}

@app.get("/signals")
def signals():
    data = get_all_signals()
    return data

@app.post("/subscribe/{email}")
def subscribe(email: str):
    users[email] = {"subscribed": True}
    save_json(USERS_FILE, users)
    return {"message": f"{email} subscribed"}

@app.get("/notify")
def notify():
    data = get_all_signals()
    strong_buys = [s for s in data if s['signal'] == "BUY"]
    if strong_buys:
        message = "\n".join([f"{s['symbol']} → {s['signal']}" for s in strong_buys])
        for email in users:
            if users[email]["subscribed"]:
                send_email(email, "Crypto Signals Alert", message)
    return {"notified": True, "sent": len(users)}

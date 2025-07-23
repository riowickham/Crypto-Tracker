from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for React frontend running on port 3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Crypto Stock Backend Running"}

@app.get("/signals")
async def get_signals():
    # Dummy data example
    signals = [
        {"symbol": "BTC", "signal": "BUY", "price": 30000},
        {"symbol": "ETH", "signal": "HOLD", "price": 2000},
        {"symbol": "XRP", "signal": "SELL", "price": 0.5},
    ]
    return {"signals": signals}

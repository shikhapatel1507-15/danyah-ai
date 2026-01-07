from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "THIS IS THE NEW CODE"}

@app.post("/personalize")
async def personalize(request: Request):
    try:
        user = await request.json()
    except Exception:
        user = {}

    if not isinstance(user, dict):
        user = {}

    user.setdefault("pages", [])
    user.setdefault("time_on_site", 0)
    user.setdefault("region", "US")

    return {
        "status": "AI is alive",
        "received_input": user,
        "identity": "leader_ceo",
        "hero_text": "Precision in every fold.",
        "recommended_products": [
            {"title": "Power Saree 1"},
            {"title": "Power Saree 2"}
        ],
        "bundle": {
            "saree": {"title": "Power Saree 1"},
            "blouse": {"title": "Power Blouse", "price": "2499"},
            "jewelry": {"title": "Statement Jewelry", "price": "4999"},
            "footwear": {"title": "Heritage Heels", "price": "6999"}
        }
    }

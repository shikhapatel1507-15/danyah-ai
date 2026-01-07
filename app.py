from fastapi import FastAPI, Request
from identity import assign_identity
from ranking import rank_products
from bundles import build_bundle

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

    # AI identity logic
    user = assign_identity(user)

    # TEMP: Fake products (so no Shopify crashes yet)
    products = [
        {
            "title": "Power Saree 1",
            "power_score": 9.5,
            "identity_match": ["leader_ceo"],
            "region_preference": ["US", "global"]
        },
        {
            "title": "Heritage Saree 2",
            "power_score": 8.2,
            "identity_match": ["leader_heritage"],
            "region_preference": ["India"]
        }
    ]

    ranked = rank_products(products, user)
    bundle = build_bundle(ranked[0])

    return {
        "identity": user.get("identity"),
        "hero_text": user.get("hero_text"),
        "recommended_products": ranked,
        "bundle": bundle
    }

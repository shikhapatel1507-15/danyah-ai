from fastapi import FastAPI, Request
from identity import assign_identity
from ranking import rank_products
from bundles import build_bundle
from shopify import fetch_products

app = FastAPI()

@app.post("/personalize")
async def personalize(request: Request):
    # Always read JSON body safely
    try:
        user = await request.json()
    except Exception:
        user = {}

    # If user is not a dictionary, fix it
    if not isinstance(user, dict):
        user = {}

    # Ensure required keys exist
    user.setdefault("pages", [])
    user.setdefault("time_on_site", 0)
    user.setdefault("region", "US")

    # Run AI logic
    user = assign_identity(user)
    products = fetch_products()
    ranked = rank_products(products, user)
    bundle = build_bundle(ranked[0])

    return {
        "identity": user.get("identity"),
        "hero_text": user.get("hero_text"),
        "recommended_products": ranked[:6],
        "bundle": bundle
    }

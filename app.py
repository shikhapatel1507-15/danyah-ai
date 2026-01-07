from fastapi import FastAPI, Request
from identity import assign_identity
from ranking import rank_products
from bundles import build_bundle
from shopify import fetch_products

app = FastAPI()

@app.post("/personalize")
async def personalize(request: Request):
    # Force read JSON body
    user = await request.json()

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

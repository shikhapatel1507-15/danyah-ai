from fastapi import FastAPI
from identity import assign_identity
from ranking import rank_products
from bundles import build_bundle
from shopify import fetch_products

app = FastAPI()

@app.post("/personalize")
def personalize(user):
    user = assign_identity(user)
    products = fetch_products()
    ranked = rank_products(products, user)
    bundle = build_bundle(ranked[0])

    return {
        "identity": user["identity"],
        "hero_text": user["hero_text"],
        "recommended_products": ranked[:6],
        "bundle": bundle
    }

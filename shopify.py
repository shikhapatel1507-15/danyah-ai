import requests
import os

SHOPIFY_STORE = os.getenv("SHOPIFY_STORE")
SHOPIFY_TOKEN = os.getenv("SHOPIFY_TOKEN")
API_VERSION = "2024-01"

def fetch_products():
    url = f"https://{SHOPIFY_STORE}/admin/api/{API_VERSION}/graphql.json"

    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": SHOPIFY_TOKEN
    }

    query = """
    {
      products(first: 20) {
        edges {
          node {
            id
            title
            handle
            vendor
            productType
            tags
          }
        }
      }
    }
    """

    try:
        response = requests.post(
            url,
            json={"query": query},
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

    except Exception as e:
        print("❌ Shopify request failed:", e)
        return []

    # 🔍 DEBUG: Print raw Shopify response
    print("🛍 Shopify raw response:", data)

    # 🚨 SAFETY: If Shopify returned an error instead of data
    if "data" not in data:
        print("⚠️ Shopify API did not return 'data'. Full response:", data)
        return []

    products = []

    try:
        edges = data["data"]["products"]["edges"]
        for edge in edges:
            node = edge["node"]
            products.append({
                "id": node.get("id"),
                "title": node.get("title"),
                "handle": node.get("handle"),
                "vendor": node.get("vendor"),
                "productType": node.get("productType"),
                "tags": node.get("tags", [])
            })
    except Exception as e:
        print("❌ Error parsing Shopify products:", e)
        return []

    return products

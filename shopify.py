import requests

SHOPIFY_DOMAIN = "your-store.myshopify.com"
STOREFRONT_TOKEN = "your_storefront_api_token"

def fetch_products():
    url = f"https://{SHOPIFY_DOMAIN}/api/2024-01/graphql.json"

    query = """
    {
      products(first: 50) {
        edges {
          node {
            title
            handle
            featuredImage { url }
            metafields(namespace: "danyah", first: 10) {
              edges {
                node {
                  key
                  value
                }
              }
            }
          }
        }
      }
    }
    """

    headers = {
        "X-Shopify-Storefront-Access-Token": STOREFRONT_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json={"query": query}, headers=headers)
    data = response.json()

    products = []
    for edge in data["data"]["products"]["edges"]:
        node = edge["node"]
        metafields = {}

        for m in node["metafields"]["edges"]:
            metafields[m["node"]["key"]] = m["node"]["value"]

        products.append({
            "title": node["title"],
            "handle": node["handle"],
            "image": node["featuredImage"]["url"] if node["featuredImage"] else "",
            "power_score": float(metafields.get("power_score", 5)),
            "identity_match": metafields.get("identity_match", "").split(","),
            "region_preference": metafields.get("region_preference", "").split(",")
        })

    return products

def rank_products(products, user):
    ranked = []
    for p in products:
        score = float(p["power_score"])

        if user["identity"] in p["identity_match"]:
            score *= 1.5

        if user["region"] in p["region_preference"] or "global" in p["region_preference"]:
            score *= 1.3

        p["final_score"] = score
        ranked.append(p)

    return sorted(ranked, key=lambda x: x["final_score"], reverse=True)

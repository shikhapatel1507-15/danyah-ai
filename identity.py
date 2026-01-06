def assign_identity(user):
    pages = user.get("pages", [])
    time = user.get("time_on_site", 0)
    region = user.get("region", "US")

    if "power" in pages and time > 60:
        identity = "leader_ceo"
        hero_text = "Precision in every fold."
    elif "banarasi" in pages:
        identity = "leader_heritage"
        hero_text = "Legacy worn with authority."
    else:
        identity = "leader_modern"
        hero_text = "Power, wrapped in elegance."

    user["identity"] = identity
    user["hero_text"] = hero_text
    user["region"] = region
    return user

def boss_settings(config: dict) -> dict:

    start = {
        "hp": 100,
        "nickname": "Гоблин",
        "friendly_fire": True
    }

    result = {}
    for key in start:
        if key not in config or config[key] is None:
            result[key] = start[key]
        else:
            result[key] = config[key]

    return result

print(boss_settings({"hp": 0, "nickname": "", "friendly_fire": False}))
print(boss_settings({"hp": None, "debug": 42}))
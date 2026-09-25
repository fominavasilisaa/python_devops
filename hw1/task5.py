import unicodedata

def unique_nicknames(names: list[str]) -> list[str]:
    seen = set()
    result = []

    for name in names:
        normal = unicodedata.normalize("NFC", name.strip().casefold())
        if normal and normal not in seen:
            seen.add(normal)
            result.append(normal)

    return result
names = [" УТКА ", "утка", "И\u0306ожик", "ЙОЖИК", " "]
print(unique_nicknames(names))
print(unique_nicknames(["Straße", "STRASSE"]))
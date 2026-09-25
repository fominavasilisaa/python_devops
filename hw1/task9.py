passports = {True: "утка", 1: "гусь", 1.0: "дракон"}
print(len(passports))
print(passports[True])

def typed_counts(values) -> dict:
    counts = {}
    for value in values:
        key = (type(value), value)
        counts[key] = counts.get(key, 0) + 1
    return counts

result = typed_counts([True, 1, 1.0, "1", False, 0, True])
print(result)

print(len(result)) 
def raid_audit(alpha: set, beta: set, required: set) -> tuple[frozenset, frozenset, frozenset]:
    both = alpha & beta
    only_one = alpha ^ beta
    missing = required - (alpha | beta)
    return (frozenset(both), frozenset(only_one), frozenset(missing))

print(raid_audit(
 {"танк", "маг"},
 {"маг", "лекарь"},
 {"танк", "лекарь", "бард"},
))
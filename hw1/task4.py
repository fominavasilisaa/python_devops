def landing_hits(readings: list[float], target: float) -> list[int]:
    result = []
    for i, value in enumerate(readings):
        tolerance = max(1e-9 * max(abs(value), abs(target)), 1e-12)
        if abs(value - target) <= tolerance:
            result.append(i)
    return result

print(landing_hits([0.1 + 0.2, 0.3001, 0.3], 0.3))
print(landing_hits([1e-13, 1e-6], 0.0))
print(landing_hits([1e9 + 0.5, 1e9 + 2.0], 1e9))
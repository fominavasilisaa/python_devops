values = iter([3, -1, 4])
total = sum(values)
count = len(list(values))

from collections.abc import Iterable

def energy_report(values: Iterable[int]) -> tuple[int, int, float | None]:
    ct = 0
    total = 0
    for v in values:
        ct += 1
        total += v
    if ct == 0:
        return (0, 0, None)
    average = total / ct
    return (ct, total, average)

stream = iter([3, -1, 4])
print(energy_report(stream))
print(list(stream))

print(energy_report(iter([])))
print(energy_report(x for x in [0, 0]))
def meme_rating(votes: list[str]) -> list[tuple[str, int]]:
    vote = {}
    for meme in votes:
        if meme not in vote:
            vote[meme] = 0
        vote[meme] += 1
    return sorted(vote.items(), key=lambda x: x[1], reverse=True)

print(meme_rating(["утка", "кот", "утка", "гусь", "кот"]))
print(meme_rating(["z", "a"]))
print(meme_rating([]))
print(meme_rating(["утка", "кот", "собака", "гаст", "крот"]))
print(meme_rating(["утка", "кот", "собака", "гаст", "Гаст"]))
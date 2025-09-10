from collections import Counter

# How many times a character repeats

text = "alcalinohermanopiedraestiloplazahito"
counter: dict[str, int] = {}

for idx, elem in enumerate(text):
    counter[elem] = counter.get(elem, 0) + 1

print(counter)

# using Counter module

counter = Counter(text)
print(f"Desde collections.Counter: {counter}")

# How many times a SPECIFIC character repeats

text2 = "alcalinohermanopiedraestiloplazahito"
specificChar = "l"
countChar: int = 0

for idx, elem in enumerate(text2):
    if elem == specificChar:
        countChar += 1

print(f"{specificChar} aparece {countChar} veces en el texto")

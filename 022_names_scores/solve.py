def calculate_alphabet_score(name):
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    return sum(alphabet.index(letter) + 1 for letter in name)

with open("names.txt") as f:
    names = sorted([name.strip('"') for name in f.read().split(",")])

print(sum((calculate_alphabet_score(name) * (i+1) for i, name in enumerate(names))))


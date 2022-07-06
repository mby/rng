import random

vowels = list('aeiou')
consonants = list('cfhklmnprstyz')

def main():
    syllable_count = random.choice([2, 3, 4])
    name = ''.join([generate_syllable() for _ in range(syllable_count)])
    print(name)

def generate_syllable():
    letters = [
        random.choice(vowels),
        random.choice(consonants),
    ]
    random.shuffle(letters)
    return ''.join(letters)

main()

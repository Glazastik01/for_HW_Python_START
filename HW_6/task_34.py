def count_vowels(word):
    vowels = "AEIOUaeiou"
    return len([letter for letter in word if letter in vowels])

def check_rhythm(poem):
    lines = poem.split()
    syllables = [count_vowels(line.replace("-", "")) for line in lines]
    return "Парам пам-пам" if len(set(syllables)) == 1 else "Пам парам"

poem = input("Введите стихотворение: ")
print(check_rhythm(poem))
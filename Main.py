class LetterFilter(object):

    def __init__(self, s):
        self.s = s

    def filter_vowels(self):
        return "".join([char for char in self.s if char in "aeiouAEIOU"])

    def filter_consonants(self):
        return "".join([char for char in self.s if char not in "aeiouAEIOU"])


# Enter your code here
# Return a string
s = input()
f = LetterFilter(s)

print(f.filter_vowels())
print(f.filter_consonants())

for i in range(2, 3):
    print(i)

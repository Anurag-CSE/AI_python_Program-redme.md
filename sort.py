import string

s = input("Enter a sentence: ")
for ch in string.punctuation:
    s = s.replace(ch, " ")

words = s.split()
words.sort(key=str.lower)


print("Sorted sentence:")
print(" ".join(words))

sentence = input("Enter a sentence: ")

words = sentence.split()
words.sort(key=str.lower)

sorted_sentence = " ".join(words)


print("Sorted sentence:")
print(sorted_sentence)

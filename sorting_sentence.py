s = input("Enter the sentence: ")
w = s.split()
sorted_words = sorted(w, key=lambda w: w.lower())
print("sorted sentence",sorted_words)

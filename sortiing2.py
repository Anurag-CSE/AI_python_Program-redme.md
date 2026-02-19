s= input("enter the sentence:")
w = s.split()

w.sort(key=str.lower)
print("words in alphabetical order:")
for i in w:
    print(w)
    

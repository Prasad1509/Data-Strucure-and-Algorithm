# Q: How to reverse each word in a sentence?
s = "hello world"
words = s.split()
reversed_words = [word[::-1] for word in words]
print(" ".join(reversed_words))  

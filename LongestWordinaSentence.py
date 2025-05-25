# Q: How to find the longest word in a sentence?
sentence = "Python is a powerful programming language"
words = sentence.split()
longest = max(words, key=len)
print(longest) 

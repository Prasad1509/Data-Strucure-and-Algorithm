# Q: How to count vowels in a string?
s = "education"
vowels = "aeiou"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Vowel count:", count)


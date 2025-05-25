# Q: How to check if two strings are anagrams?
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))  
print(are_anagrams("key", "seen"))  

s1 = "listen"
s2 = 'silent'
s1 = s1.replace(" ","").lower()
s2 = s1.replace(" ","").lower()
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not an Anagram")
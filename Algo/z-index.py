s = "ababaaa"
ind = 0
z = []
z.append(len(s))
ind = 0
count = 0
while ind <= len(s):
    new_s = s[ind:]
    for i in range(len(new_s)):
        if s[i] == new_s[i]:
            count += 1
        else:
            break
        z.append(count)
print(z)

                    
            
            
            
        
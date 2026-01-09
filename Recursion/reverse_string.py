def reverse_string(s,n,i):
    if(i == n-1):
        return s[i]
    return reverse_string(s,n,i+1) + s[i]
print(reverse_string("Daisy",5,0))
    
    
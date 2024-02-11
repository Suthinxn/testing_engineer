def alternatingCharacters(s):
    a = 0
    for i,k in enumerate(s):
        if i == 0:
            continue
        elif s[i] == s[i-1]:
            a+=1
    return a

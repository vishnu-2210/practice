def extra_char(str1, str2):
    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return str2[i]
    
    return str2[-1]

print(extra_char("eueiieo", "iieoedue"))

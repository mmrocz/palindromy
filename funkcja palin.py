def palindromy(word):
    txt = word[::-1]
    if word == txt:
        return True
    return False
print(palindromy('zakaz'))
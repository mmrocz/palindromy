def palindromy(word):
    word = word.lower()
    txt = word[::-1]
    if word == txt:
        return True
    return False
print(palindromy('Zakaz'))
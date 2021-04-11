def palindromy(word):
    word = word.lower()
    punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    new_word = ""
    for i in word:
        if i not in punctuation:
            new_word = new_word + i
    txt = new_word[::-1]
    if new_word == txt:
        return True
    return False
print(palindromy('Kobyła ma mały  ,bok'))
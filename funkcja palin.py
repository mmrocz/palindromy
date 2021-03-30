def palindromy(word):
 txt = word[::-1]
 if word == txt:
   return True
 else:
   return False
print(palindromy('warka'))
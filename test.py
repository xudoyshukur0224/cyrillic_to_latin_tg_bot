from transliterate import to_cyrillic, to_latin
# print(to_cyrillic("Assalom alaykum"))
# print(to_latin("калайсиз, ака?")) 
# print(to_cyrillic("O'zbekiston mening oooooooooooooo"))
# string.isascii()
# print("Assalom".isascii())
# print("Калайсиз".isascii())
s = input()
if s.isascii():
    print(to_cyrillic(s))
else:
    print(to_latin(s))
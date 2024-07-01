from M16STR import M16STR
from settings import WORDS, PASSWORD
hash = M16STR(words=WORDS)
result = hash.encode(text="Hello how are you",password=PASSWORD)
print(result.text)
print(result.data)
print(result.type, result.password)
print(result.words)

result = hash.decode(result, password=PASSWORD)
print(result.text)
print(result.data)
print(result.type, result.password)
print(result.words)
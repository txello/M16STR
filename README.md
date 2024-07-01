# M16STR

### Цель проекта: 

* Создать простое ассимитричное шифрование с использованием пароля в качестве закрытого ключа.

### Установка:
```bash
pip install numpy
```

#### settings.py
```python
WORDS = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26', 'a':'27','b':'28','c':'29','d':'30','e':'31','f':'32','g':'33','h':'34','i':'35','j':'36','k':'37','l':'38','m':'39','n':'40','o':'41','p':'42','q':'43','r':'44','s':'45','t':'46','u':'47','v':'48','w':'49','x':'50','y':'51','z':'52', ' ': '53'}
# {'Символ': Число }

PASSWORD = 'Ttest t'
# Пароль должен содержать символы из WORDS
```

#### main.py
```python
hash = M16STR(words=WORDS)
result = hash.encode(text="Hello how are you",password=PASSWORD)
print(result.text) # 8129c728436021f129c7284360226129c7284360226129c7284360229129c7284360235129c7284360222129c7284360229129c7284360231129c7284360235129c728436021b129c728436022c129c728436021f129c7284360235129c7284360233129c728436022912af0ef6ba3831
print(result.data) # Hello how are you
print(result.type, result.password) # HashType.ENCODE Ttest t
print(result.words) # Словарь из settings.py

result = hash.decode(result, password=PASSWORD)
print(result.text) # Hello how are you
print(result.data) # 8129c728436021f129c7284360226129c7284360226129c7284360229129c7284360235129c7284360222129c7284360229129c7284360231129c7284360235129c728436021b129c728436022c129c728436021f129c7284360235129c7284360233129c728436022912af0ef6ba3831
print(result.type, result.password) # HashType.DECODE Ttest t
print(result.words) # Словарь из settings.py
```

import numpy as np
from .errors import PasswordError, WordsError

class Magic:
    def __init__(self, data, password:str, words:dict[str, str|int]) -> None:
        self.data = data
        self.words = words
        self.password = password
    
    def __settings(self):
        try:
            password = int(''.join([self.words[i] for i in self.password]))
        except KeyError as e:
            raise WordsError('В Символьном словаре отсутcтвует символ в пароле: '+ str(e))
        values = np.array(list(self.words.values()), dtype=np.int64)
        values += password * ~-1
        arr = dict(zip(self.words.keys(), values))
        password = hex(password)[2:]
        
        return (password, arr)
        
    
    def encode(self):
        password, arr = self.__settings()
        try:
            data = [hex(arr[i])[2:] for i in list(self.data)]
        except KeyError as e:
            raise WordsError('В Символьном словаре отсутcтвует символ в тексте: '+ str(e))
        result = hex(int(password.join(data), 16)+int(password, 16))[2:]
        
        return result
    
    def decode(self):
        password, arr = self.__settings()
        
        result = hex(int(self.data, 16) - int(password, 16))[2:]
        
        s = bytearray(result, 'utf-8')
        for i in [i for i in range(len(result)) if result.startswith(password, i)]:
            for x in range(0,len(password)):
                s[i+x] = bytes('_', 'utf-8')[0]
        result = str(s, 'utf-8')

        text = result.split('_'*len(password))
        
        result = ''
        try:
            for row in text:
                result += str(list(arr.keys())[list(arr.values()).index(int(row, 16))])
        except ValueError: raise PasswordError('Пароль не подошел')
        return result
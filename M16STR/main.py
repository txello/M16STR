from .lib import M2Result
from .enums import HashType
class M16STR:
    def __init__(self,words:dict[str,str|int]) -> None:
        self.words = words
        
    def encode(self, text:str, password:str) -> M2Result:
        data = text
        return M2Result(HashType.ENCODE, data, password, words=self.words)
    
    def decode(self, data:M2Result|str, password:str):
        if type(data) == M2Result:
            data = data.text
        return M2Result(HashType.DECODE, data, password, words=self.words)
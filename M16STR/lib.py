from .enums import HashType
from .magic import Magic
class M2Result:
    def __init__(self, typing:HashType, data, password:str, words:dict[str, str|int]) -> None:
        self.type = typing
        self.data = data
        self.password = password
        self.words = words
    
    @property
    def text(self) -> str:
        if self.type == HashType.ENCODE:
            result = Magic(self.data, self.password, words=self.words).encode()
        if self.type == HashType.DECODE:
            result = Magic(self.data, self.password, words=self.words).decode()
        return result
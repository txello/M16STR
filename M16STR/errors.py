class PasswordError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class WordsError(KeyError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
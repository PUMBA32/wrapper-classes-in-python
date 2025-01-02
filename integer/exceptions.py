class SymbolException(Exception): 
    def __init__(self, s: str) -> None:
        self.letters: str = "0123456789abcdefghijklmnopqrstuvwxyz"
        self.s: str = s

    def __str__(self) -> str:
        return f'there is no symbol "{self.s}" in this list: {self.letters}'
    

class IntegerLimitException(Exception): 
    def __init__(self, value: int) -> None:
        self.MAX_VALUE: int = 2147483647
        self.MIN_VALUE: int = -2147483648
        self.value: int = value

    def __str__(self) -> str:
        return f'Integer value must be between {self.MIN_VALUE} and {self.MAX_VALUE}!\nYour value: {self.value}'
class Boolean: 
    FALSE: bool = False
    TRUE: bool = True

    def __init__(self, value: bool | str) -> None:
        if type(value) not in (str, bool):
            raise TypeError

        self.value: bool = value if isinstance(value, bool) else (True if value.lower() == 'true' else False) 


    def __str__(self) -> str:
        return f'<class: Boolean, value: {self.value}>'

# ======== Attribute methods =============================

    def boolean_value(self) -> bool: 
        return Boolean(self.value)


    def compare_to(self, b: bool) -> int: 
        return self.value == b


    def to_string(self) -> str:
        return "True" if self.value else "False"


    def hash_code(self) -> int: 
        return self.value.__hash__


# ======== Static methods ================================

    @staticmethod
    def compare(x: bool, y: bool) -> int: 
        if not isinstance(x, bool) or not isinstance(y, bool):
            raise TypeError

        return x == y


    @staticmethod
    def get_boolean(name: str) -> bool: ...


    @staticmethod
    def hash_code(value: bool) -> int:
        if not isinstance(value, bool):
            raise TypeError

        return value.__hash__


    @staticmethod
    def logical_and(a: bool, b: bool) -> bool: 
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise TypeError

        return a & b


    @staticmethod
    def logical_or(a: bool, b: bool) -> bool: 
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise TypeError

        return a | b


    @staticmethod
    def logical_xor(a: bool, b: bool) -> bool: 
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise TypeError

        return a ^ b


    @staticmethod
    def parse_boolean(s: str) -> bool:
        if not isinstance(s, str):
            raise TypeError

        return True if s.lower() == 'true' else False


    @staticmethod
    def to_string(b: bool) -> str:
        if not isinstance(b, bool):
            raise TypeError

        return "True" if b else "False"


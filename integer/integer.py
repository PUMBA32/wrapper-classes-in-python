from exceptions import (
    SymbolException, 
    IntegerLimitException
)


class Integer:
    SIZE: int = 32
    BYTES: int = 4
    MAX_VALUE: int = 2147483647
    MIN_VALUE: int = -2147483648
    TYPE = int
    

    def __init__(self, value: int | str) -> None:
        if type(value) not in (str, int):
            raise TypeError

        if value > Integer.MAX_VALUE or value < Integer.MIN_VALUE:
            raise IntegerLimitException

        self.value: int = value if isinstance(value, int) else Integer.parse_int(value)    

    
    def __str__(self) -> str:
        return f'<class: Integer, value: {self.value}>'
    
    
# ======== Attribute methods =============================

    def float_value(self) -> float:
        '''Convert value from Integer to float'''

        return float(self.value)
    

    def get_hash_code(self) -> int:
        '''Returns a hash code for this Integer'''

        return self.value.__hash__()
    

    def get_bit_count(self) -> int:
        '''Returns count of bits of this number'''

        return len(bin(self.value)[2:])


    def to_str(self) -> str:
        '''Returns str representation of this Integer'''

        return str(self.value)
    

    def to_bin(self) -> str:
        '''Translate from decimal system to binary system number'''
        
        return Integer.convert_to_any(self.value, 2)


    def to_hex(self) -> str:
        '''Translate from decimal to hexadecimal system number'''
        
        return Integer.convert_to_any(self.value, 16)


    def to_oct(self) -> str:
        '''Translate from decimal to octal system number'''
        
        return Integer.convert_to_any(self.value, 8)
    

# ======== Static methods =============================
    
    @staticmethod
    def __to_decimal(value: str, system: int) -> int:
        letters: str = "0123456789abcdefghijklmnopqrstuvwxyz"
        r: int = 0
        for i, el in enumerate(value):
            if el.lower() not in letters:
                raise SymbolException(el)
            r += int(letters.index(value[::-1][i]))*system**i
        return r


    @staticmethod
    def parse_int(value: str, system: int = 10) -> int:
        '''Converts str value in any digit system into int type'''

        if not isinstance(value, str) or not isinstance(system, int): 
            raise TypeError

        if not 2 <= system <= 36:
            raise ValueError

        temp: int = 1
        if value[0] == "-" and system == 10:
            value = value[1:]
            temp = -1

        return Integer.__to_decimal(value, system)*temp


    @staticmethod
    def min(x: int, y: int) -> int: 
        '''Returns minimum of two number'''

        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError
        
        return x if x < y else y


    @staticmethod
    def max(x: int, y: int) -> int: 
        '''Returns maximum of two numbers'''

        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError

        return x if x > y else y


    @staticmethod
    def sum(x: int, y: int) -> int:
        '''Returns the sum of two values'''

        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError
        
        return x+y


    @staticmethod
    def bit_count(value: int) -> int:
        '''Returns the number of one-bits in the binary representation of the specified int value'''
        
        if not isinstance(value, int):
            raise TypeError

        return len(bin(value)[2:])


    @staticmethod
    def compare(x: int, y: int) -> int:
        '''Compares two int values numerically.
        \n-1 first number less than second\n
0 x equals y\n
1 first number more than second'''
        
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError
        
        return -1 if x < y else (0 if x == y else 1)


    @staticmethod
    def convert_to_any(value: int, system: int) -> str:
        if not isinstance(value, int) or not isinstance(value, int):
            raise TypeError
        
        letters: str = "0123456789abcdefghijklmnopqrstuvwxyz".upper()
        r: str = ""
        while value >= 1:
            r += letters[value%system]
            value //= system
        return r[::-1]


    @staticmethod
    def convert_to_bin(value: int) -> str:
        '''Returns str with binary representation of int value'''

        if not isinstance(value, int):
            raise TypeError
        
        return Integer.convert_to_any(value, 2)
            

    @staticmethod
    def convert_to_hex(value: int) -> str:
        '''Returns str with binary representation of int value'''
        
        if not isinstance(value, int):
            raise TypeError
        
        return Integer.convert_to_any(value, 16)


    staticmethod
    def convert_to_oct(value: int) -> str:
        '''Returns str with octal representation of int value'''

        if not isinstance(value, int):
            raise TypeError
        
        return Integer.convert_to_any(value, 8)


# Методы экземпляра класса Integer
a: Integer = Integer(10)
print(a.to_bin())
print(a.to_hex())
print(a.to_oct())
print(a.float_value())
print(a.get_hash_code())
print(a.to_str())
print(a.get_bit_count())

# Статические методы класса Integer 
print(Integer.parse_int("100"))
print(Integer.bit_count(100))
print(Integer.convert_to_bin(10))
print(Integer.convert_to_oct(10))
print(Integer.convert_to_hex(10))
print(Integer.convert_to_any(2, 3))
print(Integer.min(2,3))
print(Integer.max(2,3))
print(Integer.sum(2,3))
print(Integer.compare(2,2))

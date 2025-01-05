from typing import List, Any, Callable


class String: 
    def __init__(self, value: str) -> None: 
        self.value: str = value
        self.length: int = len(value)
        self.__l_let: str = "abcdefghijklmnopqrstuvwxyz"
        self.__u_let: str = "ABCDEFGHIJKLMNOPQRSTUVWXY"


    def __str__(self) -> str:
        return self.value


# ====== Exemplar methods =================================
    
    def split(self, sep: str = " ") -> List[str]:
        result: List[str] = []
        el = ""
        i = 0
        sep_length = len(sep)
        value_length = len(self.value)
        
        while i != value_length:
            if self.value[i:i+sep_length] == sep:
                result.append(el)
                el = ""
                i += sep_length
            else:
                if i < value_length:
                    el += self.value[i]
                i += 1            
        if el != "": result.append(el)
        return result


    def replace(self, s: str, to_s: str) -> str: 
        arr: List[str] = list(self.value)
        for i in range(len(arr)):
            if arr[i] == s:
                arr[i] = to_s
        return "".join(arr)
        

    def index(self, s: str) -> int: 
        if s not in self.value: return -1

        for i in range(len(self.value)):
            if self.value[i] == s:
                return i


    def title(self) -> str: 
        if len(self.value) == 0: return ""
        
        arr: List[str] = self.value.split()
        
        for i, w in enumerate(arr):
            arr_w: List[str] = list(w)
            s_n = ord(w[0])
            if s_n != s_n-32 and w[0] in self.__l_let:
                arr_w[0] = chr(s_n-32)
                arr[i] = "".join(arr_w)
        
        return " ".join(arr)


    def __change_case(self, up_or_low: int = 0) -> str:
        if len(self.value) == 0: return ""
        arr: List[str] = list(self.value)

        for i, el in enumerate(arr):
            s_n = ord(el)
            if el in (self.__l_let if up_or_low else self.__u_let):
                arr[i] = chr(s_n+(-32 if up_or_low == 1 else 32))
        
        return "".join(arr)


    def to_upper(self) -> str: 
        return self.__change_case(1)


    def to_lower(self) -> str: 
        return self.__change_case(0)


# ====== Static methods =================================

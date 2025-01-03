import unittest

from exceptions import IntegerLimitException
from integer import Integer as Int
from typing import Callable, List, Any



class TestInteger(unittest.TestCase):
    def test_integer(self) -> None:
        self.assertRaises(TypeError, Int, None)
        self.assertRaises(TypeError, Int, 2+4j)
        self.assertRaises(TypeError, Int, 34.5)
        self.assertRaises(TypeError, Int, True)

        self.assertRaises(IntegerLimitException, Int, 2147483648)
        self.assertRaises(IntegerLimitException, Int, -2147483649)

# ===== Object methods ====================================================

    def test_to_bin(self) -> None:
        self.assertEqual(Int.to_bin(Int(10)), '1010')
        self.assertEqual(Int.to_bin(Int(100)), '1100100') 
        self.assertEqual(Int.to_bin(Int(1)), '1')
        self.assertEqual(Int.to_bin(Int(0)), '0') 

    
    def test_to_hex(self) -> None: 
        self.assertEqual(Int.to_hex(Int(10)), "A")
        self.assertEqual(Int.to_hex(Int(100)), "64")
        self.assertEqual(Int.to_hex(Int(1)), "1")
        self.assertEqual(Int.to_hex(Int(0)), "0")


    def test_to_oct(self) -> None: 
        self.assertEqual(Int.to_oct(Int(10)), "12")
        self.assertEqual(Int.to_oct(Int(100)), "144")
        self.assertEqual(Int.to_oct(Int(1)), "1")
        self.assertEqual(Int.to_oct(Int(0)), "0")


    def test_float_value(self) -> None:
        self.assertEqual(Int.float_value(Int(10)), 10.0)
        self.assertEqual(Int.float_value(Int(1324)), 1324.0)
        self.assertEqual(Int.float_value(Int(0)), 0.0)
        self.assertEqual(type(Int.float_value(Int(1))), float)

    
    def test_to_str(self) -> None:
        self.assertEqual(Int.to_str(Int(10)), "10")
        self.assertEqual(type(Int.to_str(Int(10))), str)
        self.assertEqual(Int.to_str(Int(1)), "1")


    def test_get_bit_count(self) -> None:
        self.assertEqual(type(Int.get_bit_count(Int(3))), int)
        self.assertEqual(Int.get_bit_count(Int(1)), 1)
        self.assertEqual(Int.get_bit_count(Int(10)), 4)
        self.assertEqual(Int.get_bit_count(Int(100)), 7)
        self.assertEqual(Int.get_bit_count(Int(53)), 6)

# ===== Static methods ====================================================

    def __check(self, error: Exception, func: Callable, types: List[Any]) -> None: 
        for t in types:
            self.assertRaises(error, func, t)


    def test_parse_int(self) -> None: 
        self.assertEqual(Int.parse_int("1234"), 1234)
        self.assertEqual(Int.parse_int("0"), 0)
        self.assertEqual(Int.parse_int("-10"), -10)
        self.assertEqual(Int.parse_int("-429834"), -429834)
        
        self.assertEqual(Int.parse_int("1010", 2), 10)
        self.assertEqual(Int.parse_int("111000", 2), 56)
        self.assertEqual(Int.parse_int("A", 16), 10)
        self.assertEqual(Int.parse_int("12", 8), 10)

        self.__check(TypeError, Int.parse_int, [23, None, 2+3j, [], (), {}])
        self.assertRaises(TypeError, Int.parse_int, "101", None)
        self.assertRaises(TypeError, Int.parse_int, "101", 3.45)
        self.assertRaises(TypeError, Int.parse_int, "101", 4+5j)

        self.assertRaises(ValueError, Int.parse_int, "101", 1)
        self.assertRaises(ValueError, Int.parse_int, "101", 37)

    
    def test_bit_count(self) -> None:
        self.assertEqual(type(Int.get_bit_count(Int(3))), int)
        self.assertEqual(Int.bit_count(1), 1)
        self.assertEqual(Int.bit_count(10), 4)
        self.assertEqual(Int.bit_count(100), 7)
        self.assertEqual(Int.bit_count(53), 6)

        self.__check(TypeError, Int.bit_count, [23.3, "234", 4+5j, [], {}, ()])

    
    def test_convert_to_bin(self) -> None: 
        self.assertEqual(Int.convert_to_bin(10), "1010")
        self.assertEqual(Int.convert_to_bin(1), "1")
        self.assertEqual(Int.convert_to_bin(0), "0")
        self.assertEqual(Int.convert_to_bin(54), "110110")

        self.__check(TypeError, Int.bit_count, [23.3, "234", 4+5j, [], {}, (), 23.4])


    def test_convert_to_oct(self) -> None: 
        self.assertEqual(Int.convert_to_oct(10), "12")
        self.assertEqual(Int.convert_to_oct(1), "1")
        self.assertEqual(Int.convert_to_oct(0), "0")
        self.assertEqual(Int.convert_to_oct(54), "66")

        self.__check(TypeError, Int.convert_to_oct, [23.3, "234", 4+5j, [], {}, (), 23.4])


    def test_convert_to_hex(self) -> None:
        self.assertEqual(Int.convert_to_hex(10), "A")
        self.assertEqual(Int.convert_to_hex(1), "1")
        self.assertEqual(Int.convert_to_hex(0), "0")
        self.assertEqual(Int.convert_to_hex(54), "36")

        self.__check(TypeError, Int.convert_to_hex, [23.3, "234", 4+5j, [], {}, (), 23.4])

    
    def test_convert_to_any(self) -> None: 
        self.__check(TypeError, Int.convert_to_any, [23.3, "234", 4+5j, [], {}, (), 23.4])


    def test_min(self) -> None:
        self.assertEqual(Int.min(2, 3), 2)
        self.assertEqual(Int.min(22342, 3), 3)
        self.assertEqual(Int.min(2, -1324), -1324)
        self.assertEqual(Int.min(0, 0), 0)
        self.assertEqual(Int.min(32, 33), 32)

        self.assertRaises(TypeError, Int.min, "34", 34)
        self.assertRaises(TypeError, Int.min, None, 34)
        self.assertRaises(TypeError, Int.min, 3+4j, 34)
        self.assertRaises(TypeError, Int.min, 34.5, 34)
        self.assertRaises(TypeError, Int.min, 34, "34")
        self.assertRaises(TypeError, Int.min, 34, None)
        self.assertRaises(TypeError, Int.min, 34, 34.5)
        self.assertRaises(TypeError, Int.min, 34, 3+4j)


    def test_max(self) -> None:
        self.assertEqual(Int.max(2, 3), 3)
        self.assertEqual(Int.max(22342, 3), 22342)
        self.assertEqual(Int.max(2, -1324), 2)
        self.assertEqual(Int.max(-4, -3), -3)
        self.assertEqual(Int.max(32, 33), 33)

        self.assertRaises(TypeError, Int.max, "34", 34)
        self.assertRaises(TypeError, Int.max, None, 34)
        self.assertRaises(TypeError, Int.max, 3+4j, 34)
        self.assertRaises(TypeError, Int.max, 34.5, 34)
        self.assertRaises(TypeError, Int.max, 34, "34")
        self.assertRaises(TypeError, Int.max, 34, None)
        self.assertRaises(TypeError, Int.max, 34, 34.5)
        self.assertRaises(TypeError, Int.max, 34, 3+4j)


    def test_compare(self) -> None: 
        self.assertEqual(Int.compare(2,2), 0)
        self.assertEqual(Int.compare(2,1), 1)
        self.assertEqual(Int.compare(1,2), -1)

        self.assertRaises(TypeError, Int.compare, "34", 34)
        self.assertRaises(TypeError, Int.compare, None, 34)
        self.assertRaises(TypeError, Int.compare, 3+4j, 34)
        self.assertRaises(TypeError, Int.compare, 34.5, 34)
        self.assertRaises(TypeError, Int.compare, 34, "34")
        self.assertRaises(TypeError, Int.compare, 34, None)
        self.assertRaises(TypeError, Int.compare, 34, 34.5)
        self.assertRaises(TypeError, Int.compare, 34, 3+4j)
        

if __name__ == '__main__':
    unittest.main()
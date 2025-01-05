import unittest

from boolean import Boolean
from typing import Callable, List, Any


class TestBoolean(unittest.TestCase): 
    def __check_types(self, er: Exception, func: Callable, types: List[Any], is_two_args=False) -> None:
        if not is_two_args:
            for t in types:
                self.assertRaises(er, func, t)
        else:
            for t1 in types:
                for t2 in types:
                    self.assertRaises(er, func, t1, t2)


    def test_boolean_constructor(self) -> None:
        self.__check_types(TypeError, Boolean,  [None, 1.0, 3+4j, [], (), {}, 1])
    

# ======== Class methods ========================

    def test_boolean_value(self) -> None: 
        self.assertEqual(type(Boolean("true")), Boolean)
        self.assertEqual(type(Boolean("false")), Boolean)
        self.assertEqual(type(Boolean("False")), Boolean)
        self.assertEqual(type(Boolean("True")), Boolean)
        self.assertEqual(type(Boolean(True)), Boolean)
        self.assertEqual(type(Boolean(False)), Boolean)


    def test_compare_to(self) -> None: 
        self.assertEqual(Boolean.compare_to(Boolean(True), True), True)
        self.assertEqual(Boolean.compare_to(Boolean(False), False), True)
        self.assertEqual(Boolean.compare_to(Boolean(True), False), False)
        self.assertEqual(Boolean.compare_to(Boolean(False), True), False)


    def test_to_string(self) -> None: 
        self.assertEqual(Boolean.to_string(Boolean(True)), "True")
        self.assertEqual(Boolean.to_string(Boolean(False)), "False")
        self.assertEqual(Boolean.to_string(Boolean("true")), "True")
        self.assertEqual(Boolean.to_string(Boolean("false")), "False")
    

# ======== Static methods =======================

    def test_compare(self) -> None: 
        self.__check_types(TypeError, Boolean.compare, [None, 1.0, 1, 3+4j, [], {}, ()], is_two_args=True)

        self.assertEqual(Boolean.compare(True, True), True)
        self.assertEqual(Boolean.compare(True, False), False)
        self.assertEqual(Boolean.compare(False, True), False)
        self.assertEqual(Boolean.compare(False, False), True)


    def test_get_boolean(self) -> None: ...        


    def test_logical_and(self) -> None: 
        self.__check_types(TypeError, Boolean.logical_and, ["true", None, 1.0, 1, 3+4j, [], {}, ()], is_two_args=True)

        self.assertEqual(Boolean.logical_and(True, True), True)
        self.assertEqual(Boolean.logical_and(True, False), False)
        self.assertEqual(Boolean.logical_and(False, True), False)
        self.assertEqual(Boolean.logical_and(False, False), False)


    def test_logical_or(self) -> None:
        self.__check_types(TypeError, Boolean.logical_or, ["true", None, 1.0, 1, 3+4j, [], {}, ()], is_two_args=True)

        self.assertEqual(Boolean.logical_or(True, True), True)
        self.assertEqual(Boolean.logical_or(True, False), True)
        self.assertEqual(Boolean.logical_or(False, True), True)
        self.assertEqual(Boolean.logical_or(False, False), False)


    def test_logical_xor(self) -> None: 
        self.__check_types(TypeError, Boolean.logical_xor, ["true", None, 1.0, 1, 3+4j, [], {}, ()], is_two_args=True)

        self.assertEqual(Boolean.logical_xor(True, True), False)
        self.assertEqual(Boolean.logical_xor(True, False), True)
        self.assertEqual(Boolean.logical_xor(False, True), True)
        self.assertEqual(Boolean.logical_xor(False, False), False)


    def test_parse_boolean(self) -> None: 
        self.__check_types(TypeError, Boolean.parse_boolean, [False, None, 1.0, 1, 3+4j, [], {}, ()])

        self.assertEqual(Boolean.parse_boolean("false"), False)
        self.assertEqual(Boolean.parse_boolean("False"), False)
        self.assertEqual(Boolean.parse_boolean("true"), True)
        self.assertEqual(Boolean.parse_boolean("True"), True)
        self.assertEqual(Boolean.parse_boolean("something another"), False)


    def test_to_string(self) -> None: 
        self.__check_types(TypeError, Boolean.to_string, [None, 1.0, 1, 3+4j, [], {}, ()])

        self.assertEqual(Boolean.to_string(True), "True")
        self.assertEqual(Boolean.to_string(False), "False")


if __name__ == '__main__':
    unittest.main()

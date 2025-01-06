import unittest

from string import String as Str


class TestString(unittest.TestCase): 
    def test_split(self) -> None: 
        self.assertEqual(Str.split(Str("a b")), ["a", "b"])
        self.assertEqual(Str.split(Str("aaa")), ["aaa"])
        self.assertEqual(Str.split(Str("a-a-a-a-"), "-"), ['a', 'a', 'a', 'a'])
        self.assertEqual(Str.split(Str("00el000el00"), "el"), ['00', '000', '00'])
        self.assertEqual(Str.split(Str(""), "-"), [])
        self.assertEqual(Str.split(Str("a"), ""), ['a'])


    def test_replace(self) -> None: 
        self.assertEqual(Str.replace(Str("100"), '0', "p"), '1pp')
        self.assertEqual(Str.replace(Str("nigger"), 'i', "I"), 'nIgger')
        self.assertEqual(Str.replace(Str(""), 's', "p"), '')
        self.assertEqual(Str.replace(Str("I love programming"), 'I', "Everybody"), 'Everybody love programming')


    def test_index(self) -> None: 
        self.assertEqual(Str.index(Str("100"), "1"), 0)
        self.assertEqual(Str.index(Str("welcome"), "c"), 3)
        self.assertEqual(Str.index(Str("100"), "0"), 1)
        self.assertEqual(Str.index(Str(""), "1"), -1)


    def test_title(self) -> None: 
        self.assertEqual(Str.title(Str("name")), "Name")
        self.assertEqual(Str.title(Str("tooLongName")), "TooLongName")
        self.assertEqual(Str.title(Str("first second")), "First Second")
        self.assertEqual(Str.title(Str("")), "")
        self.assertEqual(Str.title(Str("f")), "F")
        self.assertEqual(Str.title(Str("3")), "3")
        self.assertEqual(Str.title(Str("1 2 3 4")), "1 2 3 4")


    def test_to_upper(self) -> None: 
        self.assertEqual(Str.to_upper(Str("name")), "NAME")
        self.assertEqual(Str.to_upper(Str("two names")), "TWO NAMES")
        self.assertEqual(Str.to_upper(Str("NAME")), "NAME")
        self.assertEqual(Str.to_upper(Str("")), "")
        self.assertEqual(Str.to_upper(Str("+-0name")), "+-0NAME")
        self.assertEqual(Str.to_upper(Str("Two Names")), "TWO NAMES")


    def test_to_lower(self) -> None: 
        self.assertEqual(Str.to_lower(Str("name")), "name")
        self.assertEqual(Str.to_lower(Str("Two Names")), "two names")
        self.assertEqual(Str.to_lower(Str("NAME")), "name")
        self.assertEqual(Str.to_lower(Str("")), "")
        self.assertEqual(Str.to_lower(Str("+-0name")), "+-0name")


if __name__ == '__main__':
    unittest.main() 







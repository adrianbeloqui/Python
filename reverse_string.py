import unittest


def reverse_string(string):
    characters = list(string)
    characters.reverse()
    return "".join(characters)


def run():
    print(reverse_string("Hello"))
    print(reverse_string("Adrian"))
    print(reverse_string("November"))


class Test(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(reverse_string("Hello"),"olleH")

    def test_name(self):
        self.assertEqual(reverse_string("Adrian"),"nairdA")

    def test_month(self):
        self.assertEqual(reverse_string("November"),"rebmevoN")

if __name__ == '__main__':
    #unittest.main()
    run()

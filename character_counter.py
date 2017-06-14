import unittest


def char_counter(string):
    counter = dict()
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    result= ""
    for key in counter:
        result += key + ": " + str(counter[key]) + ", "
    return result[0: len(result) - 2]


def run():
    print(char_counter("abacca"))
    print(char_counter("aadfafadsffabacca"))
    print(char_counter("abaadfbfjdhjffgndsgfgsfdgscca"))


class Test(unittest.TestCase):

    def test_one(self):
        self.assertEqual(char_counter("abacca"), "a: 3, b: 1, c: 2")


if __name__ == '__main__':
    #unittest.main()
    run()
        
            
        
        

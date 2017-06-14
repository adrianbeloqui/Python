
import copy

# words = ['foo', 'aaf', 'oof', 'lake', 'bud', 'kale','ofo']
# anagram = [['foo', 'oof'], ['aaf'], ['lake', 'kale], ['bud']]

# words = ['oof', 'foo', 'foo', 'ofo', 'aaf', 'foo', 'lake', 'kale', 'bud', 'ofo']
# anagram = [['oof', 'foo', 'ofo'], ['aaf'], ['lake', 'kale'], ['bud']]


# SOLUTION 1
##
def calculate_anagram(words):
    anagram = list()
    working_copy = copy.deepcopy(words)
    for word in words:
        if word in working_copy:
            inner_anagram = set([word])
            word_list = list(word)
            word_list.sort()
            temp_list = list()
            working_copy.remove(word)
            for item in working_copy:
                word_list2 = list(item)
                word_list2.sort()
                if word_list == word_list2:
                    inner_anagram.add(item)
                    continue
                temp_list.append(item)
            working_copy = copy.deepcopy(temp_list)
            anagram.append(list(inner_anagram))
    return anagram


print (calculate_anagram(['oof', 'foo', 'foo', 'ofo', 'aaf', 'foo', 'lake',
                          'kale', 'bud', 'ofo']))

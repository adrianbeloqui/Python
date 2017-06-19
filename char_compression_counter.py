#input: "aaaaabbbbccccccaaaaaaa" 
#output: "5a4b6c7a"


def string_compression(string):
    result_string = ""
    if not string:
        return result_string
    current_char = string[0]
    count = 1
    for char in xrange(1, len(string)):
        if string[char] != current_char:
            result_string += str(count) + current_char
            count = 1
            current_char = string[char]
        else:
            count += 1
    result_string += str(count) + current_char
    return result_string

print(string_compression("aaaaabbbbccccccaaaaaaa"))
print(string_compression("a"))

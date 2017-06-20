def count_substring(string, sub_string):
    count = start = 0
    while True:
        start = string.find(sub_string, start) + 1
        if start > 0:
            count += 1
        else:
            return count


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    count = count_substring(string, sub_string)
    print(count)
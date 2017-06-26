LETTERS = ['a', 'b', 'c', 'd', 'e',
           'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't',
           'u', 'v', 'x', 'y', 'z'
           ]


def print_rangoli(size):
    printed = list()
    width = ((size * 2) - 1) + (size - 1) * 2
    for i in range(size - 1, -1, -1):
        result = "-".join(printed) + "-" + LETTERS[i] + "-" + "-".join(reversed(printed))
        print(result.center(width, "-"))
        printed.append(LETTERS[i])
    printed.pop()
    last_letter = printed.pop()
    for i in range(1, size):
        result = "-".join(printed) + "-" + last_letter + "-" + "-".join(reversed(printed))
        print(result.center(width, "-"))
        if printed:
            last_letter = printed.pop()

import string

def sol2(N):
    mid = N - 1

    for i in range(N-1, -1, -1):
        row = ['-'] * (2 * N - 1)
        for j in range(N - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print '-'.join(row)

    for i in range(0, N):
        row = ['-'] * (2 * N - 1)
        for j in range(0, N - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print '-'.join(row)

if __name__ == '__main__':
    n = int(raw_input())
    #print_rangoli(n)
    sol2(n)

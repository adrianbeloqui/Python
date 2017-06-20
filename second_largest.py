"""You are given N numbers. Store them in a list and find the second largest number.

Input Format
The first line contains N. The second line contains an array A[] of N integers each separated by a space.

Constraints
    2 <= N <= 10
    -100 <= A[i] <= 100

Output Format
Output the value of the second largest number.

"""


def second_largest(*args):
    arr = args[0]
    largest, second_large = arr.__next__(), -100
    for num in arr:
        if num > second_large:
            if num > largest:
                second_large, largest = largest, num
            elif num == largest:
                continue
            else:
                second_large = num
    return second_large


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(second_largest(arr))
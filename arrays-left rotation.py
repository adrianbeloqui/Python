def array_left_rotation(a, n, k):
    # n = number of elements
    # k = left turns
    # a = initial array
    if k == n:
        return a
    if k < n:
        if k == 1:
            return a[k:n] + [a[0]]
        else:
            return a[k:n] + a[0:k]
    ##else:
      #  for num in xrange(k):
       #     a = a[1:n] + [a[0]]
    return a
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

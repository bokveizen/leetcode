def read(seq):
    cnt = 0
    cur = ''
    index = 0
    res = ''
    while index < len(seq):
        if seq[index] != cur:
            if cur:
                res += str(cnt) + cur
            cur = seq[index]
            cnt = 1
        else:
            cnt += 1
        index += 1
    res += str(cnt) + cur
    return res

read('1')
def combos(A, K):
    result = []
    A.sort()
    stk = [(0, 0, [])]
    while stk:
        idx, curr_sum, l = stk.pop()
        if curr_sum == K:
            result.append(l)
            continue
        for i in range(idx, len(A)):
            if curr_sum + A[i] > K:
                break
            if i > idx and A[i] == A[i - 1]:
                continue
            stk.append((i + 1, curr_sum + A[i], l + [A[i]]))
    return result
if __name__ == '__main__':
    x = [9, 6, 1, 5, 0, 7, 2, 3]
    sum = 8
    combo = combos(x, sum)
    for i in combo:
        print(', '.join(map(str, i)))
data = list(map(int, input().split(', ')))


def palindrome(nums: list):
    res = []
    for num in nums:
        st = set()
        num_s = str(num)
        st.add(num_s)
        st.add(num_s[::-1])
        res.append(True) if len(st) == 1 else res.append(False)
    return res


print(*palindrome(data), sep='\n')

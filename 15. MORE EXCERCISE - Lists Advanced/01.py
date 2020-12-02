nums = list(map(int, input().split()))
string = input()
message = ''

for num in nums:
    d_sum = sum(map(int, str(num)))
    while d_sum >= len(string):
        d_sum -= len(string)
    message += string[d_sum]
    string = string[:d_sum] + string[(d_sum + 1):]

print(message)
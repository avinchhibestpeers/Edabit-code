# https://edabit.com/challenge/q7rHnH9Jhf35NqSjG


def trailing_zeros(n):
    cnt = 0
    temp = n

    while temp:
        cnt += temp // 5
        temp //= 5

    print(f"After removing trailing commas - {temp}")
    return cnt


result = trailing_zeros(12344000)
print(result)

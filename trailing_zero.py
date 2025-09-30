# https://edabit.com/challenge/q7rHnH9Jhf35NqSjG

def trailing_zeros(n):
    cnt = 0
    temp = n

    while temp:
        cnt += temp // 5
        tmep //= 5

    return cnt

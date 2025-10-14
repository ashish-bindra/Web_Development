# def max_profit(prices: list[int]) -> float:

#     max_diff = 0
#     pre = prices[0]

#     for price in prices:
#         diff = price - pre
#         print(diff)
#         if diff > max_diff:
#             max_diff = diff
#         pre = price
#     return float(max_diff)


# prices = [7, 1, 5, 3, 6, 4]
# assert max_profit(prices) == 4.0
# print()
# prices = [7, 6, 4, 3, 1]
# assert max_profit(prices) == 0.0


from typing import List

def shift_array(arr: List[int], n: int) -> List[int]:
    c = []
    n = n+1
    if n > len(arr):
        n = n // len(arr)
    for i,v in enumerate(arr,start = n):
        if i< len(arr):
            print(".",i)
            c.append(arr[i])
        else:
            c.append(arr[i - len(arr)])
    return c

arr = [0,1, 2, 3, 4, 5]
n = 4

print(shift_array(arr, n))
assert shift_array(arr, n) == [2, 3, 4, 5, 0, 1]
import heapq

nums=[1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

portfolio=[
    {'name':'IBM', 'shares':100, 'price':92.1},
    {'name': 'Sky', 'shares': 3, 'price': 10},
    {'name': 'LB', 'shares': 54, 'price': 52.1},
    {'name': 'Samsung', 'shares': 456, 'price': 924.1},
    {'name': 'Monkeys', 'shares': 4, 'price': 2.1}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print("cheap", cheap)
print("expensive", expensive)

heap=list(nums)
heapq.heapify(heap)
print("heap", heap)
# https://www.hackerrank.com/challenges/collections-counter/problem

shoes_hash   = {}
money_earned = 0

_     = input()
shoes = input().split()

for shoe in shoes:
    shoes_hash[shoe] = shoes_hash.get(shoe, 0) + 1

inquiry_count = int(input())

for i in range(inquiry_count):
    size, amount = input().split()
    
    if shoes_hash.get(size, 0) > 0:
        money_earned     += int(amount)
        shoes_hash[size] -= 1

print(money_earned)
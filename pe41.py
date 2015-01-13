from itertools import permutations
from functions import is_prime
print max(filter(lambda x: is_prime(int(x)), [''.join(i) for i in permutations('1234567')]))
# ANS: 7652413 (can't have 8 or 9 digits because 36/45 are divisible by 3)
from functions import is_prime, sieve, product

LIMIT = 5000
primes = [i for i in sieve(LIMIT)]

# p1p2 and p2p1 are prime
def commute(p1, p2):
	return (is_prime(int(str(p1)+str(p2))) and is_prime(int(str(p2)+str(p1))))

# all doubles of commuting primes
# two_commute = filter(lambda tup: commute(tup[0], tup[1]), product(primes,primes))

commute_dict = {prime: filter(lambda x: commute(prime, x), primes) for prime in primes}
commute_dict = {key: commute_dict[key] for key in filter(lambda x: len(commute_dict[x]) > 0, commute_dict.keys())}
print commute_dict
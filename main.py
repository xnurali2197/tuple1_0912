import math


tuple1 = tuple(i * i for i in range(1, 21) if i % 2 == 0)


tuple2 = tuple(i for i in range(1, 51) if i % 3 == 0)


words = ["hello", "world", "python"]
tuple3 = tuple(len(s) for s in words)


def digit_sum(n):
	return sum(int(d) for d in str(abs(n)))

tuple4 = tuple(i for i in range(1, 101) if digit_sum(i) % 2 == 0)


tuple5 = tuple(w[0] for w in ["python", "tuple", "set", "loop"])

def is_prime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	r = int(n**0.5)
	for j in range(3, r+1, 2):
		if n % j == 0:
			return False
	return True
tuple6 = tuple(i for i in range(1, 31) if is_prime(i))


nums = [-3, 0, 5, -1, 8]
tuple7 = tuple(n for n in nums if n > 0)


tuple8 = tuple((i, i * i) for i in range(1, 16))

text = "hello world python"
tuple9 = tuple(w[-1] for w in text.split() if w)

tuple10 = tuple((i * i) for idx, i in enumerate(range(1, 21)) if idx % 2 == 1)

vowels = set("aeiouAEIOU")
given = ["apple", "banana", "pear", "orange", "umbrella"]

tuple11 = tuple(w for w in given if w and w[0] in vowels)

tuple12 = tuple(i for i in range(1, 51) if str(i) == str(i)[::-1])

sample = "ABC"
tuple13 = tuple(ord(ch) for ch in sample)

tuple14 = tuple(i**3 for i in range(1, 21) if i % 5 == 0)
words_list = ["one", "three", "seven", "fourteen", "code"]

tuple15 = tuple(w for w in words_list if len(w) > 4)

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4[:10])
print(tuple5)
print(tuple6)
print(tuple7)
print(tuple8)
print(tuple9)
print(tuple10)
print(tuple11)
print(tuple12)
print(tuple13)
print(tuple14)
print(tuple15)


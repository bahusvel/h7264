__author__ = 'denislavrov'
from random import randint

data = [randint(0, 255) for x in xrange(8)]


def parity(arr, start, stop, bit):
	ret = 0
	arr = list(enumerate(arr, start=1))
	for index, ibit in arr[start:stop]:
		if index & bit:
			ret ^= ibit
	return ret


def par_pos(num):
	return [2 ** y for y in range(num)]


def bit_arr(data):
	ret_buffer = []
	i = 0
	while i < (len(data) * 8):
		ret_buffer.append((data[i // 8] & (1 << (7 - (i % 8)))) >> (7 - (i % 8)))
		i += 1
	return ret_buffer


def compute():
	br = bit_arr(data)
	br[64:72] = br[56:64]
	pp = list(par_pos(7).__reversed__())
	for index, par in enumerate(pp):
		br[par] = parity(br, par, 72, par)
		br[pp[index + 1]:par] = br[pp[index]]
		print("Doing parity for:" + str(par))


print(compute())


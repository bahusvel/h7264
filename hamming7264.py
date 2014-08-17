__author__ = 'denislavrov'
from random import randint

# data = [randint(0, 255) for x in xrange(8)]
data = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
		0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1]


def bit_arr(data):
	ret_buffer = []
	i = 0
	while i < (len(data) * 8):
		ret_buffer.append((data[i // 8] & (1 << (7 - (i % 8)))) >> (7 - (i % 8)))
		i += 1
	return ret_buffer


def compute(inp):
	pdata = [[], [], [], [], [], [], [], []]
	result = [0, 0, 0, 0, 0, 0, 0, 0]
	buff = []
	barr = data
	posarr = [1, 2, 4, 8, 16, 32, 64]
	di = 0
	for i in xrange(1, 73):
		if i in posarr:
			buff.append(0)
		elif i == 72:
			buff.append(0)
		else:
			buff.append(barr[di])
			di += 1
	for i in range(7):
		for index, bit in enumerate(buff):
			if (index + 1) & posarr[i] and (index + 1) != posarr[i]:
				pdata[i].append(bit)
		for bit in pdata[i]:
			result[i] ^= bit
	return result


hamming = compute(data)
data = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
		0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1]
recham = compute(data)
print(hamming)
print(recham)
hi = int(''.join([str(x) for x in hamming]), 2)
ri = int(''.join([str(x) for x in recham]), 2)
print(hi)


# Python implementation of Fast Fourier
# Tranform (FFT) algorithm for polynomial
# multiplication. Time complex: O(n log n)
# but slightly faster and more efficient
# than recursive version.

import cmath

# Utility function for reversing the bits
# of given index x


def bitReverse(x, log2n):
	n = 0
	for i in range(log2n):
		n <<= 1
		n |= (x & 1)
		x >>= 1
	return n

# Iterative FFT function to compute the DFT
# of given coefficient vector


def fft(a, A, log2n):
	n = 4

	# bit reversal of the given array
	for i in range(n):
		rev = bitReverse(i, log2n)
		A[i] = a[rev]

	# j is iota
	J = complex(0, 1)
	for s in range(1, log2n + 1):
		m = 1 << s # 2 power s
		m2 = m >> 1 # m2 = m/2 -1
		w = complex(1, 0)

		# principle root of nth complex
		# root of unity.
		wm = cmath.exp(J * (cmath.pi / m2))
		for j in range(m2):
			for k in range(j, n, m):

				# t = twiddle factor
				t = w * A[k + m2]
				u = A[k]

				# similar calculating y[k]
				A[k] = u + t

				# similar calculating y[k+n/2]
				A[k + m2] = u - t
			w *= wm


a = [1, 2, 3, 4]
A = [0, 0, 0, 0]
fft(a, A, 2)
for i in range(4):
	print(A[i])

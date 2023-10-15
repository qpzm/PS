import math

# theta = 2pi * n/N
# return cos(theta) + i sin(theta)
def calc_omega(n, N, inverse):
    if inverse:
        theta = - (2 * math.pi) * (float(n) / N)
        real = math.cos(theta)
        imag = math.sin(theta)
        return complex(real, imag)
    else:
        theta = (2 * math.pi) * (float(n) / N)
        real = math.cos(theta)
        imag = math.sin(theta)
        return complex(real, imag)


def _fft(coefficients, inverse=False):
    N = len(coefficients)
    if (N == 1):
        return coefficients

    # convert coefficients repr -> point-val repr
    # odds means odd exponent: 1 + x + x^3 ...
    evens = _fft(coefficients[0::2], inverse)
    odds = _fft(coefficients[1::2], inverse)

    # list of (real, imag)
    y = [complex(0, 0) for j in range(N)]

    print("N: ", N)
    print("evens ", evens)
    print("odds: ", odds)

    for i in range(0, N // 2):
        w = calc_omega(i, N, inverse)
        print("w: ", w)
        y[i] = evens[i] + w * odds[i]
        y[i + N // 2] = evens[i] - w * odds[i]

    return y

def fft(coefficients):
    return _fft(coefficients, inverse=False)

def ifft(points):
    N = len(points)
    return [x * 1 / N for x in _fft(points, inverse=True)]

# f(x) = 1 + 2x + x^2
# evaluation points: 1, i, -1, -i
# [(4+0j), (1.2246467991473532e-16+2j), 0j, (-1.2246467991473532e-16-2j)]
print(fft([complex(1, 0), complex(2, 0), complex(1, 0), complex(0, 0)]))
print(ifft([complex(4, 0), complex(0, 2), complex(0, 0), complex(0, -2)]))

# f(x) = (x + 1)^4 = 1 + 4x + 6x^2 + 4x^3 + x^4
print(fft([complex(1, 0), complex(4, 0), complex(6, 0), complex(4, 0), complex(1, 0), complex(0, 0), complex(0, 0), complex(0, 0)]))
print(ifft(fft([complex(1, 0), complex(4, 0), complex(6, 0), complex(4, 0), complex(1, 0), complex(0, 0), complex(0, 0), complex(0, 0)])))

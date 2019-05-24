values = [50, 100, 250, 300, 350, 400, 450, 500]
frequency = [4, 2, 5, 8, 9, 7, 6, 5]


# Formula: Mean(X)
# X = xs + (E fi di) / E fi
#
# Sum = Sigma
# xs = Rata-rata sementara (nilai tengah dari salah satu interval kelas)
# xi = Nilai tengah pada interval kelas ke-i
# di = xi - xs
# fi = Frequency kelas ke-i


def sigma(val, freq):
    result = 0
    for v, f in zip(val, freq):
        result += v * f

    return result


def average(sm, n):
    return sm / n


print(" --- 01 Average Group Data ---")
print()

print("Sum \t= ", sigma(values, frequency))
print("n \t\t= ", len(frequency))
print()
print("Avg \t= ", average(sigma(values,frequency), len(frequency)))

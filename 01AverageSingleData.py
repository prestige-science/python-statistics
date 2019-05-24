values = [50, 100, 250, 300, 350, 400, 450, 500]


# Formula: Mean(X)
# x = E xi / n
#
# E     = Sum
# xi    = values entity
# n     = len

def find_sum(val):
    for v in val:
        v += v

    return v


def average(sm, n):
    return sm / n


print(" --- 01 Average Single Data ---")
print()

print("Sum \t= ", find_sum(values))
print("n \t\t= ", len(values))
print()

fSum = find_sum(values)
lVal = len(values)
print("Avg \t= ", average(fSum, lVal))
# OR
print("Avg \t= ", average(find_sum(values), len(values)))
# OR
print("Avg \t= ", sum(values) / len(values))

print()

print("Why different?")


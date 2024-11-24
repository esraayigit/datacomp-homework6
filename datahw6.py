def initialize_pmf(num_symbols, V):
    initial_value = (2**V) // num_symbols 
    pmf = [initial_value] * num_symbols
    leftover = (2**V) - sum(pmf)
    for i in range(leftover):
        pmf[i % num_symbols] += 1

    return pmf

def update_pmf(pmf, symbol, V, increment=1):
    pmf[symbol] += increment
    total = sum(pmf)

    if total > 2**V:
        scale_factor = (2**V) / total
        pmf = [max(1, int(p * scale_factor)) for p in pmf]  # All possibilities >= 1

    total = sum(pmf)
    if total < 2**V:
        leftover = (2**V) - total
        for i in range(leftover):
            pmf[i % len(pmf)] += 1

    return pmf

def arithmetic_coding(pmf, symbol):
    print(f"Encoding symbol: {symbol} with PMF: {pmf}")

# Parameters
V = 16
num_symbols = 4

# starts pmf
pmf = initialize_pmf(num_symbols, V)
print(f"Initial PMF: {pmf}")

input_stream = [0, 1, 2, 3, 0, 1, 0]

for symbol in input_stream:
    pmf = update_pmf(pmf, symbol, V)
    arithmetic_coding(pmf, symbol)
    print(f"Updated PMF: {pmf}")

a = [0] * 15

for i in range(13):
    a[ (i * 4) % 16 : (i * 4) % 16 + 4] += i / 2 + 1
    a[ i + 4 : sum(a[i : i + 12]) - sum(a[i + 1 :i+3])] = i

print(a)
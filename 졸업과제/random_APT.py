import random

APT_pool = "ACGU"

result = ""
results = []
for j in range(100):
    for i in range(30) :
        result += random.choice(APT_pool)
    results.append(result)
    result = ""

f = open('data/random_apt8.csv', 'w')
for i in range(100):
    f.write(str(i) + ',' + results[i] + '\n')

f.close()
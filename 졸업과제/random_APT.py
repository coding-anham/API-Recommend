import random
from hyperparams import *

APT_pool = "ACGU"

result = ""
results = []
for j in range(100):
    for i in range(30) :
        result += random.choice(APT_pool)
    results.append(result)
    result = ""
for i in range(10):
    f = open(PAIRS_PATH["rand"][i], 'w')
    for j in range(100):
        f.write(str(j) + ',' + results[j] + '\n')
    f.close()
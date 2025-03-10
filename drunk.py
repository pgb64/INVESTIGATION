'''
Pruebas drunkard's walk
'''

import random
import numpy as np
import pandas as pd

def random_walk(n):
    mean_moves = []
    for _ in range(n):
        y = 2
        moves = 0
        while y > 0 and y < 4:
            y += random.choice([-1, 1])
            moves += 1
        mean_moves.append(moves)

    return np.mean(mean_moves), max(mean_moves)


def data_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)



data = []
for _ in range(100):
    data.append(random_walk(1_000_000))
    print(f"\r{_}/100", end="", flush=True)

data_to_csv(data)
print(data)

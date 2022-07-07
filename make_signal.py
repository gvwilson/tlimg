import random
import sys

signal = [random.randint(0, 15) for _ in range(int(sys.argv[1]))]
print(signal)

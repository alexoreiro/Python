#!/usr/bin/python3

import random
import math

print([x for x in [random.randint(1, 1000) for i in range(50)] if x % 9 == 0])

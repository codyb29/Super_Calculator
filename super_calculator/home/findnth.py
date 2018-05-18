from __future__ import division 
from decimal import *
import math

# Will implment Chudnovsky algorithm
def getPi (k) :
    # Error checking and zero case 
    if (k <= 0 or k > 100000) :
        return str(3)
    # Attribute setup per wikipedia.org/wiki/Chudnovsky_algorithm
    limit = math.ceil(k / 14)
    getcontext().prec = (limit * 14)
    L = Decimal (13591409)
    X = Decimal (1)
    M = Decimal (1)
    K = Decimal (6)
    total = Decimal (0) 

    # Should iterate once every k % 14 == 0
    for ctr in range (0, limit + 1) :
        total += (Decimal(M * L) / X)
        # In order to prevent a needless calculation @ the end
        if (ctr < limit) : 
            L += 545140134
            X *= -262537412640768000
            M *= ((K**3) - (16 * K)) / ((ctr + 1)**3)
            K += 12

    # Define the constant to be divided at the end
    C = 426880 * Decimal(10005).sqrt()
    # return the final computed value of pi
    return str(C / total)[:k+2]

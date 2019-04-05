                                          ###################
                                          # !!! WARNING !!! #
                                          ###################

                                        #########################
                                        # !!! CODE SOLUTION !!! #
                                        #########################
                                        
                                          ###################
                                          # !!! WARNING !!! #
                                          ###################
                                          
#!/bin/python3

import math
import os
import random
import re
import sys

def arrays(arr):
  """Finds the max sum per hourglass in square array"""
  n = len(arr) - 2
  r = []

  for j in range(n):
    for i in range(n):
      r.append(sum(arr[i][j:j+3] + [arr[i+1][j+1]] + arr[i+2][j:j+3]))

  return max(r)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

print(arrays(arr))

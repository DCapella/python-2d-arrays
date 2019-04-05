# Pyton 2D Arrays

#### [HackerRank](www.hackerrank.com)

> Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

## PreWork

The 1's are what create the hourglass that we need to sum up. And it needs to be repeated for each column and row.

|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **0** | **1** | **1** | **1** | 0 | 0 | 0 |
| **1** | 0 | **1** | 0 | 0 | 0 | 0 |
| **2** | **1** | **1** | **1** | 0 | 0 | 0 |
| **3** | 0 | 0 | 0 | 0 | 0 | 0 |
| **4** | 0 | 0 | 0 | 0 | 0 | 0 |
| **5** | 0 | 0 | 0 | 0 | 0 | 0 |

* Repeat for each column.

|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **0** | 0 | **1** | **1** | **1** | 0 | 0 |
| **1** | 0 | 0 | **1** | 0 | 0 | 0 |
| **2** | 0 | **1** | **1** | **1** | 0 | 0 |
| **3** | 0 | 0 | 0 | 0 | 0 | 0 |
| **4** | 0 | 0 | 0 | 0 | 0 | 0 |
| **5** | 0 | 0 | 0 | 0 | 0 | 0 |

* Repeat for each row.

|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** | **1** | **1** | **1** | 0 | 0 | 0 |
| **2** | 0 | **1** | 0 | 0 | 0 | 0 |
| **3** | **1** | **1** | **1** | 0 | 0 | 0 |
| **4** | 0 | 0 | 0 | 0 | 0 | 0 |
| **5** | 0 | 0 | 0 | 0 | 0 | 0 |


Two repeats means two `for` loops.

For the set up, lets solve the very first one.

* In order to grab those numbers:

A[0][:3] + A[1][1] + A[2][:3]

* Append the sum to `r`

* All the numbers need to be replaced with i and j in order to keep looping.

* We will need to keep looping until (n-2) because it needs two more spaces since hourglass is length of 3.

* Since it will be a square, we can just do the loop twice.

## Steps

* Define function arrays that takes arr
* Declare n as length of arr - 2
* Declare r as empty array
* Loop through twice as i, j
* Append sum{ A[0][:3] + A[1][1] + A[2][:3] } to r
* Return max{ r }
* Get arr from input
* Print calling function arrays with parameter arr

## Code

```python
# Given from hackerrank
#!/bin/python3

import math
import os
import random
import re
import sys

# Define function arrays that takes arr
def arrays(arr):
  """Finds the max sum per hourglass in square array"""
  
  # Declare n as length of arr - 2 and r as empty array
  n = len(arr) - 2
  r = []

  # Loop through twice as i, j
  for i in range(n):
    for j in range(n):
      # Append sum{ A[0][:3] + A[1][1] + A[2][:3] } to r
      r.append(sum(arr[i][j:j+3] + [arr[i+1][j+1]] + arr[i+2][j:j+3]))

  # Return max{ r }
  return max(r)

# Given from hackerrank
if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

# Print calling function arrays with parameter arr
print(arrays(arr))
```

# Conclustion

Probably the hardest one yet. Loved it! Had to really get the pre-writing down. Very fun warm up and glad to be able to work with 2D arrays.




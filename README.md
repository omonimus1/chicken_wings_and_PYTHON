## Data Science in Python notes
[Online course](https://app.dataquest.io/m/289/introduction-to-numpy/3/understanding-vectorization)


## Bytecode

Bytecode, aslo temred portable code or-pce is a form of instrucion set designed for efficient execution by a software interpreter. 

### NummPy and Pandas

The core data structure in NumPy is the ndarray or n-dimensional array. 


'''
import numpy as np
data_ndarray = np.array([10,20,30])
'''

List of list in python are usually sufficient for working with small data sets. 

two-dimensional(2D) ndarrays.`1

```
my_numbers = [
                [6,5]
                [1,9]
                [3,45]
                [2,5]
             ]

sums = []

for row in my_numbers:
    row_sum = row[0] + row[1]
    sums.append(row_sum)
```

The NUmPy library takes advantage of a processor feature called SingleInstruction Multiple Data (SIMD) to process data faster. SIMD allows a processor to perform the same operation on multiple data points in a single process cycle. 


the concepts of replacing for loops with operations applied to multiple data points at once is called vectorization and ndarrays make vectorization possible. 

[Continue here](https://app.dataquest.io/m/289/introduction-to-numpy/5/array-shapes)
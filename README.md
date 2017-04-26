# cydtw

DTW computation made efficient using Cython

## Installation

`pip install cydtw`

## Usage and example

See file `test_compare.py`

This module basically provides two main functions:

```python
from cydtw import dtw, dtw_path

s1 = ...
s2 = ...

path, dtw_dist = dtw_path(s1, s2)
dtw_dist = dtw_path(s1, s2)
```
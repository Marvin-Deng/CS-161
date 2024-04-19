# HW 3
Warehouse game solver

## Running
```shell
python3 hw3.py
```

## Tests

Vince Lin's [tests](https://gist.github.com/vinlin24/5379704763a06952d91c0af0f52ddbb3):
```shell
# Basic Tests
python3 test_hw3.py

# Optimality Test h0
python3 test_hw3.py -s

# Optimality Test h1
python3 test_hw3.py -s h1

# Extreme Tests
python3 test_hw3.py -xs hUID

# Test Goal State
python -m unittest test_hw3.TestGoalTest

# Test Next State
python -m unittest test_hw3.TestNextStates

# Test H1
python -m unittest test_hw3.TestH1
```

#!/usr/bin/env python
# coding: utf-8

# # Task 1: Terminal, VS Code and Jupyter
# 
# ## Objective
# Practise Python loops and compare execution time.
# 
# ## Concepts
# - List comprehension
# - For loop
# - Execution time using %timeit

# 

# In[2]:


numbers = list(range(1000))

def using_list_comprehension():
    return [number * 2 for number in numbers]

def using_for_loop():
    result = []
    for number in numbers:
        result.append(number * 2)
    return result

print(using_list_comprehension()[:5])
print(using_for_loop()[:5])





# ## When to Use Jupyter and Python Files
# 
# 1. Jupyter notebooks are useful for data analysis and experiments.
# 2. Notebooks let us run code cell by cell and see results immediately.
# 3. Python `.py` files are useful for reusable programs and automation.
# 4. `.py` files are suitable for running complete scripts and larger projects.


import timeit

print("List comprehension time:")
print(timeit.timeit(
    "[number * 2 for number in numbers]",
    globals=globals(),
    number=1000
))

print("For loop time:")
print(timeit.timeit(
    "using_for_loop()",
    globals=globals(),
    number=1000
))
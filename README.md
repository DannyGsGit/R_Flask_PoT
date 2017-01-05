# R_Flask_PoT

This PoT explores the use of Python's subprocess library and the Flask API framework to wrap R processes, thus exposing R scripts as webservices through a unified approach (i.e. R + Python exposed through Flask, rather than a standalone API layer for R like OpenCPU).


## Example 1
```
File:
Ex1_Py_R_Integration.py
```
Demonstrates basic communication between R and Python. In the first section, we receive a hello world message from R. The second section demonstrates the passing of arguments into R for a simple addition of numerics.

## Example 2
```
Files:
Ex2_R_Flask_API.py
Ex2_Test_Script.py
```
Takes the simple addition function from Example 1 and wraps it with a Flask API (in the Ex2_R_Flask_API.py script). A test script, Ex2_Test_Script.py, is also included to test the operation of the API.

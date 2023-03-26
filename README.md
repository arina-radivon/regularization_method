## About the method

This paper presents the implementation of the regularization method described in the article

IAN KNOWLES, ROBERT J. RENKA "METHODS FOR NUMERICAL DIFFERENTIATION OF NOISY DATA"

It allows you to search for derivatives and their errors for noisy data.
For more information look [Differentiation of noisy data](https://ejde.math.txstate.edu/conf-proc/21/k3/knowles.pdf)

## Table of contents

This repository contains several files:

*regularization.py* - main file with method implementation

*documentation.md* - documentation for regularization.py file functions and variables

*example_solar.ipynb* - an example of using the method for constructing kinematic curves of coronal mass ejections for the event of February 25, 2014

*example_func.ipynb* - example of using the method on a mathematical function


## Installation

This package is to be used with Python 3.x.x

To install tha package write

```python
pip install regularization-derivatives
```

## Usage

To use the package in your project, import it in by writing

```python
from regularization_derivatives import regularization_derivatives
```
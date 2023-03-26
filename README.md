## О методе

This paper presents the implementation of the regularization method described in the article

IAN KNOWLES, ROBERT J. RENKA "METHODS FOR NUMERICAL DIFFERENTIATION OF NOISY DATA"

It allows you to search for derivatives and their errors for noisy data.
For more information look [Differentiation of noisy data](https://ejde.math.txstate.edu/conf-proc/21/k3/knowles.pdf)

## Содержание

This repository contains several files:

*regularization.py* - main file with method implementation

*documentation.md* - documentation for regularization.py file functions and variables

*example_solar.ipynb* - an example of using the method for constructing kinematic curves of coronal mass ejections for the event of February 25, 2014

*example_func.ipynb* - example of using the method on a mathematical function

## Необходимые библиотеки

In order for the file to run on your local machine, you need to install the following libraries:

+ numpy
+ scipy
+ tqdm

To install these libraries, write the appropriate commands on the command line:

```python
pip install numpy
pip install scipy
pip install tqdm
```

> **Note**
> Позже здесь появится функция установки этого пакета через pip install
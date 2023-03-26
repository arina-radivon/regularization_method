
## Parameters of the function

### regularization(*height, t_height, err_height, alpha, ord, print_parameters=True, mk=False, num_mk=100*)


Based on a set of coordinates of points and errors, it obtains the coordinates of points of derivatives by the regularization method, as well as the errors of these points by the Monte Carlo method.

Parameters:

+ **height** : *array_like*

Array of y-coordinates of points by which the derivative will be calculated

+ **t_height** : *array_like*

Array of x-coordinates of points by which the derivative will be calculated

+ **err_height** : *array_like*

Array of error y-coordinates of points by which the derivative will be calculated

+ **alpha** : *float*

Regularization parameter

+ **ord** : *int (1, 2 or 3)*

Order of differentiation operator

+ **print_parametrs** : *boolean*

Displays the parameters needed to select the regularization parameter *alpha*

+ **mk** : *boolean*

Calculates the errors of the obtained points-derivatives by the Monte Carlo method

+ **num_mk** : *int*

Number of iterations in the Monte Carlo method

## Recommendations for use

### Selection of the regularization parameter *alpha*

The main problem of using this method is the selection of the *alpha* parameter.
To choose it correctly, you need to look at the value indicated in the program as *quotient*

$$ 
quotient = \frac{\textbardbl A \vec{u} - \stackrel{\wedge}{y} \textbardbl^2}{\textbardbl \delta y \textbardbl ^2}
$$

In theory, the optimal value of the above expression is equal to one. But in practice it is often difficult to obtain such an ideal case, and sometimes it is not only impossible, but also unnecessary. In this case, you should be guided by the principle:

> **Note** :
The closer *quotient* is to zero, the better the resulting curve will fit the data. The closer *quotient* is to one, the smoother the resulting curve will be.

For more information look the article [Radivon A.V., Zimovets I.V.](https://kmu.cosmos.ru/docs/2022/KMU-2022-Proceedings-v4.pdf) (*DOI: 10.21046/KMU-2022-112-119*)

> **Warning** :
> *alpha* for any particular task can be very different from about *1e1* to *1e20*, so when choosing, first determine the power.

See **example** in this repository for clarification on alpha parameter selection

### Choice of the order of the differentiation operator ord

As part of our task, we wanted to obtain a smooth acceleration function from the distance versus time data. The curve is smooth if the function has a continuous derivative, then in our case the order of the differentiation operator *ord* is 3, since the acceleration is the second derivative of the coordinate, and it must be smooth. Accordingly, to speed up the order of the differentiation operator *ord = 2*.


### Using the Monte Carlo method

The regularization method is not provided with tools for estimating the errors of derivatives, so the Monte Carlo method was used for these purposes. To use it a large number of times, a set of points is created for the distance within the error limits, and then the speed is calculated by the regularization method.

To use it, you need to set the function parameters *mk = True* and set the number of iterations *num_mk*

> **Warning** :
> Due to the peculiarities of the method of searching for smooth functions, the errors on the "tails" are much larger than in the middle. If you have a lot of points, then you can remove such points at the ends from consideration, since their errors will be somewhat overestimated.


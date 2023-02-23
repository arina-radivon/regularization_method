import numpy as np
from scipy.optimize import minimize
from tqdm import tqdm


def A(t_values, t_derivatives, dt):
    """
    Linear system matrix for different ratios t_values and t_derivatives
    """
    out = np.zeros((len(t_values)-1, len(t_derivatives)))
    for i in range(len(t_values)-1):
        for j in range(len(t_derivatives)):
            if t_values[i+1] < t_derivatives[j]:
                out[i,j] = 0
            elif (t_derivatives[j] < t_values[i+1]) and (t_values[i+1] < t_derivatives[j]+dt):
                out[i,j] = t_values[i+1] - t_derivatives[j]
            elif t_derivatives[j]+dt < t_values[i+1]:
                out[i,j] = dt
    return out


def D(u, dt, order):
    """
    Calculation of the differential operator D depending on its order.
    """
    if order == 0:
        return u
    elif order == 1:
        return np.diff(u)/dt
    elif order == 2:
        return np.diff(np.diff(u))/dt**2
    elif order == 3:
        return np.diff(np.diff(np.diff(u)))/dt**3


def integral(matrix, derivative, constant):
    return np.insert(matrix.dot(derivative) + constant, 0, constant)


def E(derivative, alpha, values, matrix, dt, order):
    """
    Minimized functional E with non-negative regularization parameter alpha.
    """
    return ((np.linalg.norm(integral(matrix, derivative, values[0]) - values))**2
            + alpha*(np.linalg.norm(D(derivative, dt, order)))**2)
    

def regularization(height, t_height, err_height, alpha, ord, print_parameters=True, mk=False, num_mk=100):
    """
    The function you will be using.
    Input:
        height - array of values along the y-axis
        t_height - array of values along the x-axis
        err_height - array of error values along the y-axis
        alpha - non-negative regularization parameter
        ord - order of the differential operator
        print_parametrs - responsible for printing parameters when fitting the
                          regularization parameter.
        mk - responsible for running the Monte Carlo method
        num_mk - number of iterations in the Monte Carlo method
    Output:
        mk=False:
            t_vel - array of derivative values obtained by regularization method
                    along the x-axis
            vel - array of derivative values obtained by regularization method
                  along the y-axis
        mk=True:
            t_vel - array of derivative values obtained by Monte Carlo method
                    along the x-axis
            vel_mk.mean(0) - array of derivative values obtained by Monte Carlo
                             method along the y-axis
            err_vel - errors in the values of the derivatives along the y-axis
                      obtained by the Monte Carlo method
    """

    t_vel, dt_vel = np.linspace(t_height[0],t_height[-1],len(t_height), retstep=True)
    t_vel = t_vel + dt_vel/2
    t_vel = t_vel[:-1]


    vel0 = np.diff(height)/np.diff(t_height)
    A_vel = A(t_height, t_vel, dt_vel)
    optim = minimize(E,vel0,args=(alpha,height,A_vel,dt_vel,ord),method='SLSQP',options={'maxiter':300})
    vel = optim.x
    height_back = integral(A_vel,vel,height[0])
    if print_parameters:
        print(optim.message)
        print('quotient =', E(vel,0,height,A_vel,dt_vel,3)/np.linalg.norm(err_height)**2)
        print('Difference between initial data and integrated regularization results',
             (((height_back-height)/err_height)**2).sum()/len(height))

    if mk:
        vel_mk = np.zeros((num_mk,len(vel)))
        # for i in range(num_mk):    
        for i in tqdm(range(num_mk)):
            height_temp = np.random.normal(height,err_height)
            optim = minimize(E,vel0,args=(alpha,height_temp,A_vel,dt_vel,ord),method='SLSQP',options={'maxiter':300})
            # print(i, end=' ')
            vel_mk[i] = optim.x
        err_vel = vel_mk.std(0)
        return t_vel, vel_mk.mean(0), err_vel

    return t_vel, vel


if __name__ == '__main__':
    pass

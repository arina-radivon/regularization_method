import reg_func as reg
import numpy as np
import matplotlib.pyplot as plt


height = np.array([ 911.95361291,  916.01218277,  916.8771258 ,  919.58187432,
        921.91924057,  923.64333833,  931.27159974,  940.01358455,
        957.48597758,  977.79619177,  996.63108858, 1016.81112428,
    1033.42725673, 1046.2278114 , 1066.04335898, 1088.19337867,
    1101.97747826, 1118.34772448, 1135.69862147, 1148.86945256,
    1167.94734145, 1183.08526237, 1203.02230599, 1219.14377184,
    1235.26813183, 1251.14371144, 1264.43893272, 1277.24238154,
    1296.80914874, 1321.54242091])

t_height = np.array([   9.60075   ,   79.23960887,  141.40067339,  219.56571371,
        281.88806855,  368.49864516,  422.77868952,  469.41964919,
        526.95471976,  570.50194355,  612.6781996 ,  644.20228024,
        683.68802621,  721.56086895,  766.96293145,  804.10996774,
        848.38299798,  874.87785887,  911.91503024,  940.45523992,
        976.36337903, 1007.96810484, 1045.27643145, 1080.29747379,
    1108.88910887, 1141.13899597, 1167.79514718, 1187.37672984,
    1213.3070746 , 1234.01768952])

err_height = np.array([ 7.19401087,  6.04300115,  5.52013216,  6.24957474,  7.94482722,
        7.48237897, 10.5301334 ,  7.40113466, 12.93183918,  9.94548249,
        9.52313272,  7.79114099,  7.48237897,  8.87918292, 10.15602405,
    10.22721201,  5.7350031 ,  9.2787442 ,  9.53582177,  8.2068558 ,
    10.61590837,  8.22892717,  8.94701571,  9.75520884, 12.64821174,
        9.38242053,  9.42742041, 11.80253901, 10.58739393, 10.06633118])


# t_vel, vel = first_regularization(height, t_height, err_height, alpha=6e19)
# print(vel)
t_vel, vel = reg.regularization(height, t_height, err_height, alpha=6e19, ord=3, print_parameters=True, mk=False)
t_vel, vel_mk, err_vel = reg.regularization(height, t_height, err_height, alpha=6e19, ord=3, print_parameters=False, mk=True)

t_acc, acc = reg.regularization(vel, t_vel, err_vel, alpha=9.697e14, ord=2, print_parameters=True, mk=False)
t_acc, acc_mk, err_acc = reg.regularization(vel, t_vel, err_vel, alpha=9.697e14, ord=2, print_parameters=True, mk=True)

plt.subplot(1,2,1)
plt.plot(t_vel,vel*725, label = 'velocity by regularization')
plt.errorbar(t_vel,vel_mk*725,err_vel*725,fmt='.', label = 'velocity with errors by Monte-Karlo')

plt.subplot(1,2,2)
plt.plot(t_acc,acc*725, label = 'velocity by regularization')
plt.plot(t_acc, np.diff(vel)/np.diff(t_vel)*725)
plt.errorbar(t_acc,acc_mk*725,err_acc*725,fmt='.', label = 'velocity with errors by Monte-Karlo')

plt.grid()
plt.show()
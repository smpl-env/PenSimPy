import GPy
import GPyOpt
from math import log


def f(x):
    x0, x1, x2, x3, x4, x5 = x[:, 0], x[:, 1], x[:, 2], x[:, 3], x[:, 4], x[:, 5],
    f0 = 0.2 * log(x0)
    f1 = 0.3 * log(x1)
    f2 = 0.4 * log(x2)
    f3 = 0.2 * log(x3)
    f4 = 0.5 * log(x4)
    f5 = 0.2 * log(x5)
    return -(f0 + f1 + f2 + f3 + f4 + f5)


bounds = [
    {'name': 'x0', 'type': 'discrete', 'domain': (1, 1000000)},
    {'name': 'x1', 'type': 'discrete', 'domain': (1, 1000000)},
    {'name': 'x2', 'type': 'discrete', 'domain': (1, 1000000)},
    {'name': 'x3', 'type': 'discrete', 'domain': (1, 1000000)},
    {'name': 'x4', 'type': 'discrete', 'domain': (1, 1000000)},
    {'name': 'x5', 'type': 'discrete', 'domain': (1, 1000000)}
]
constraints = [
    {
        'name': 'constr_1',
        'constraint': '(x[:,0] + x[:,1] + x[:,2] + x[:,3] + x[:,4] + x[:,5]) - 100000000 - 0.1'
    },
    {
        'name': 'constr_2',
        'constraint': '100000000 - (x[:,0] + x[:,1] + x[:,2] + x[:,3] + x[:,4] + x[:,5]) - 0.1'
    }
]
myBopt = GPyOpt.methods.BayesianOptimization(f=f, domain=bounds, constraints=constraints)
myBopt.run_optimization(max_iter=100)
print(myBopt.x_opt)
print(myBopt.fx_opt)

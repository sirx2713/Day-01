import numpy as np

myData = np.random.permutation(5000)
x_tr, x_tes, y_tr, y_tes = x[:6], x[6:], y[:6], y[6:]
x_tr, y_tr = x_tr[myData], y_tr[myData]
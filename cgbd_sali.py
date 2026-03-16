import os

data_dir = "data"
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

import numpy as np
from joblib import Parallel, delayed
from pynamicalsys import DiscreteDynamicalSystem as dds

ds = dds(model="extended standard nontwist map")

x0 = 0.5
y_ranges = [(0.0, 0.4), (-0.45, 0.0)]
c_range = [1e-16, 0.5]
a = 0.53
b = 0.53
m = 0.80
max_time = int(1e6)
grid_size = 1000


def compute_point(j, k, y, c, max_time):
    u = [x0, y[j, k]]
    parameters = [a, b, c[j, k], m]
    sali = ds.SALI(u, max_time, parameters=parameters)
    return j, k, sali


for i in range(len(y_ranges)):
    print(i)
    y_range = y_ranges[i]

    datafile = f"{data_dir}/cgbd_sali_a={a:.5f}_b={b:.5f}_m={m:.5f}_crange={c_range[0]:.16f}_{c_range[1]:.16f}_yrange={y_range[0]:.5f}_{y_range[1]:.5f}_time={max_time}_grid_size={grid_size}.dat"

    c = np.linspace(*c_range, grid_size)
    y = np.linspace(*y_range, grid_size)
    c, y = np.meshgrid(c, y, indexing="ij")

    result = np.zeros((grid_size, grid_size))

    jobs = [(j, k) for j in range(grid_size) for k in range(grid_size)]

    out = Parallel(n_jobs=-1)(
        delayed(compute_point)(j, k, y, c, max_time) for j, k in jobs
    )

    for j, k, val in out:
        result[j, k] = val

    data = np.zeros((grid_size**2, 3))
    data[:, 0] = c.ravel()
    data[:, 1] = y.ravel()
    data[:, 2] = result.ravel()

    np.savetxt(datafile, data, fmt="%.16e %.16f %.16e", delimiter=" ")

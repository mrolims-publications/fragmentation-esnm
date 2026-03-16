import os

data_dir = "data"
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

import numpy as np
from joblib import Parallel, delayed
from pynamicalsys import DiscreteDynamicalSystem as dds

ds = dds(model="extended standard nontwist map")

x_range = (0.38, 0.62)
y_ranges = [(-0.1, 0.5), (-0.45, 0.05)]
a = 0.53
b = 0.53
c_vals = [5e-5, 1e-4, 5e-4, 1e-3][::-1]
m = 0.80
max_time = int(1e6)
grid_size = 1000


def compute_point(j, k, x, y, max_time):
    u = [x[j, k], y[j, k]]
    return j, k, ds.SALI(u, max_time)


for c in c_vals:
    parameters = [a, b, c, m]
    ds.set_parameters(parameters)

    for i in range(len(y_ranges)):
        print(c, i)
        y_range = y_ranges[i]

        datafile = f"{data_dir}/grid_sali_a={a:.5f}_b={b:.5f}_c={c:.5f}_m={m:.5f}_xrange={x_range[0]:.5f}_{x_range[1]:.5f}_yrange={y_range[0]:.5f}_{y_range[1]:.5f}_time={max_time}_grid_size={grid_size}.dat"

        x = np.linspace(*x_range, grid_size)
        y = np.linspace(*y_range, grid_size)
        x, y = np.meshgrid(x, y, indexing="ij")

        result = np.zeros((grid_size, grid_size))

        jobs = [(j, k) for j in range(grid_size) for k in range(grid_size)]

        out = Parallel(n_jobs=-1)(
            delayed(compute_point)(j, k, x, y, max_time) for j, k in jobs
        )

        for j, k, val in out:
            result[j, k] = val

        data = np.zeros((grid_size**2, 3))
        data[:, 0] = x.ravel()
        data[:, 1] = y.ravel()
        data[:, 2] = result.ravel()

        np.savetxt(datafile, data, fmt="%.16f %.16f %.16e", delimiter=" ")

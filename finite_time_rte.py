import os

data_dir = "data"
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

import numpy as np
from pynamicalsys import DiscreteDynamicalSystem as dds, TimeSeriesMetrics

ds = dds(model="extended standard nontwist map")
a = 0.53
b = 0.53
m = 0.8
c = 1e-4
ds.set_parameters([a, b, c, m])

datafile = f"{data_dir}/elliptic_points.dat"
x0, y0 = np.loadtxt(datafile, unpack=True)

total_time = int(5e9)
finite_time = 200
num_windows = total_time // finite_time
rr = 0.05
rte_lims = {"U": (0, 1.6), "L": (0.0, 1.6)}  # rte.min(), rte.max()

for i, region in enumerate(["U", "L"]):
    rte_vals = np.zeros(num_windows)
    x0_vals = np.zeros(num_windows)
    y0_vals = np.zeros(num_windows)
    u = [x0[i], y0[i]]
    for window in range(num_windows):
        x0_vals[window] = u[0]
        y0_vals[window] = u[1]
        rte_vals[window], u = ds.recurrence_time_entropy(
            u, finite_time, threshold_mode="rr", threshold=rr, return_final_state=True
        )

        if u[1] > 1 or u[1] < -1:
            print(f"escaped in {window} iterations")
            break

    data = np.zeros((window, 3))
    data[:, 0] = x0_vals[:window]
    data[:, 1] = y0_vals[:window]
    data[:, 2] = rte_vals[:window]
    datafile = f"{data_dir}/finite_time_rte_{region}_a={a:.5f}_b={b:.5f}_c={c:.5f}_m={m:.5f}_time={total_time}_ftime={finite_time}_rr={rr:.3f}.dat"
    np.savetxt(datafile, data, fmt="%.16f", delimiter=" ")

import os

data_dir = "data"
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

import numpy as np
from joblib import Parallel, delayed
from pynamicalsys import DiscreteDynamicalSystem as dds

datafile = f"{data_dir}/elliptic_points.dat"
x0, y0 = np.loadtxt(datafile, unpack=True)

c_list = [0, 1e-5, 5e-5, 1e-4, 5e-4, 1e-3]
a = 0.53
b = 0.53
m = 0.80
total_time = int(1e12)

sample_times = np.unique(
    np.logspace(
        np.log10(1),
        np.log10(total_time),
        100000,
    ).astype(int)
)


def compute_and_save(i, region, c):
    ds = dds(model="extended standard nontwist map")

    parameters = [a, b, c, m]
    u = [x0[i], y0[i]]

    lle_history = ds.lyapunov(
        u,
        total_time,
        parameters,
        return_history=True,
        sample_times=sample_times,
        num_exponents=1,
    )

    datafile = (
        f"{data_dir}/mle_history_{region}_a={a:.5f}_b={b:.5f}"
        f"_c={c:.5f}_m={m:.5f}_time={total_time}.dat"
    )

    data = np.zeros((lle_history.shape[0], 2))
    data[:, 0] = sample_times
    data[:, 1] = lle_history
    np.savetxt(datafile, data, fmt="%d %.16e")

    return region, c


jobs = [(i, region, c) for i, region in enumerate(["U", "L"]) for c in c_list]

Parallel(n_jobs=-1)(delayed(compute_and_save)(i, region, c) for i, region, c in jobs)

import os

data_dir = "data"
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

import numpy as np
from pynamicalsys import DiscreteDynamicalSystem as dds

ds = dds(model="extended standard nontwist map")
ds.set_parameters([0.53, 0.53, 0, 0.80])


def symmetry_line(y, parameters):
    return 0.5 * np.ones_like(y)


period = 2
num_points = 10000
tolerance = 2 / num_points


datafile = f"{data_dir}/elliptic_points.dat"
with open(datafile, "w") as file:
    for y_range in [(0.2, 0.4), (-0.4, -0.2)]:
        points = np.linspace(*y_range, num_points)

        periodic_orbit = ds.find_periodic_orbit(
            points,
            period,
            tolerance=tolerance,
            verbose=False,
            symmetry_line=symmetry_line,
            axis=1,
        )

        print(f"x = {periodic_orbit[0]:.16f}")
        print(f"y = {periodic_orbit[1]:.16f}")

        file.write(f"{periodic_orbit[0]:.16f} {periodic_orbit[1]:.16f}\n")

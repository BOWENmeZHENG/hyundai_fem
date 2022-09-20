import analysis_for_one as one
import numpy as np
import os
import shutil

radii = np.linspace(0.05, 0.15, 4)
centers_x = np.linspace(-0.5, 0.5, 4)
centers_y = np.linspace(-0.075, 0.075, 4)

for radius in radii:
    for center_x in centers_x:
        for center_y in centers_y:
            folder = one.analysis(width=1.5, height=0.5,
                                  radius=radius, center_x=center_x, center_y=center_y,
                                  E=1.0e8, nu=0.3, load=20.0e3
                                  )
            os.makedirs("data", exist_ok=True)
            shutil.copyfile(f"{folder}/{folder}_elements.csv", f"data/{folder}_elements.csv")
            shutil.copyfile(f"{folder}/{folder}_nodes.csv", f"data/{folder}_nodes.csv")


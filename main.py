import analysis_for_one as one
import numpy as np
import os
import shutil

# Define parameters of training data
radii = np.linspace(0.05, 0.1, 4)
centers_x = np.linspace(-0.1, 0.1, 4)
centers_y = np.linspace(-0.05, 0.05, 4)

# Write .csv files for ML training
for radius in radii:
    for center_x in centers_x:
        for center_y in centers_y:
            folder = one.analysis(width=1.5, height=0.5,
                                  radius=radius, center_x=center_x, center_y=center_y,
                                  E=1.0e8, nu=0.3, load=20.0e3
                                  )
            data_folder = "try"
            os.makedirs(data_folder, exist_ok=True)
            shutil.copyfile(f"{folder}/{folder}_elements.csv", f"{data_folder}/{folder}_elements.csv")
            shutil.copyfile(f"{folder}/{folder}_nodes.csv", f"{data_folder}/{folder}_nodes.csv")
            shutil.rmtree(folder)


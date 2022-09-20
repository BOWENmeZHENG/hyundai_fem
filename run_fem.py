import preprocess
from solidspy import solids_GUI
import matplotlib.pyplot as plt


def run(width=1, height=0.5, radius=0.1, center_x=0, center_y=0,
        E=1.0e8, nu=0.3, load=20.0e3,
        plot_contours=False, compute_strains=True):
    mesh = preprocess.meshing(width=width, height=height, radius=radius, center_x=center_x, center_y=center_y)
    folder = f"w{width:.3}_h{height:.3}_r{radius:.3}_cx{center_x:.3}_cy{center_y:.3}"
    preprocess.write_files(mesh, folder, E=E, nu=nu, load=load)
    disp_complete, strain_nodes, stress_nodes = solids_GUI(plot_contours=plot_contours,
                                                           compute_strains=compute_strains,
                                                           folder=folder + '/')
    if plot_contours:
        plt.show()

    return disp_complete, strain_nodes, stress_nodes, folder

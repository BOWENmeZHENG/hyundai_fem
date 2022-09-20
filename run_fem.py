import preprocess
from solidspy import solids_GUI
import matplotlib.pyplot as plt


def run(width=1, height=0.5, radius=0.1,
        E=1.0e8, nu=0.3, load=20.0e3,
        plot_contours=False, compute_strains=True):
    mesh = preprocess.meshing(width=width, height=height, radius=radius)
    folder = f"w{width}_h{height}_r{radius}"
    preprocess.write_files(mesh, folder, E=E, nu=nu, load=load)
    disp_complete, strain_nodes, stress_nodes = solids_GUI(plot_contours=plot_contours,
                                                           compute_strains=compute_strains,
                                                           folder=folder + '/')
    if plot_contours:
        plt.show()

    return disp_complete, strain_nodes, stress_nodes, folder

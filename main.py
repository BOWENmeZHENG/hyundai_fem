import fem
from solidspy import solids_GUI
import solidspy.preprocesor as pre
import solidspy.postprocesor as post
import matplotlib.pyplot as plt


def run_fem(width=1, height=0.5, radius=0.1,
            E=1.0e8, nu=0.3, load=20.0e3,
            plot_contours=False, compute_strains=True):
    mesh = fem.meshing(width=width, height=height, radius=radius)
    folder = f"w{width}_h{height}_r{radius}/"
    fem.write_files(mesh, folder, E=E, nu=nu, load=load)
    disp_complete, strain_nodes, stress_nodes = solids_GUI(plot_contours=plot_contours,
                                                           compute_strains=compute_strains,
                                                           folder=folder)
    if plot_contours:
        plt.show()

    return disp_complete, strain_nodes, stress_nodes

disp, strain, stress = run_fem(plot_contours=False)
# nodes, mats, elements, loads = pre.readin(folder="")
# tri = post.mesh2tri(nodes, elements)

# def plot_result(tri, disp, strain, stress):
#     plt.figure(figsize=(8, 6))
#     plt.tricontourf(tri, stress[:, 0])
#     plt.axis("image")
#     plt.show()







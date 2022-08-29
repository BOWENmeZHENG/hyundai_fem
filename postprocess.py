import solidspy.preprocesor as pre
import solidspy.postprocesor as post
import matplotlib.pyplot as plt


def plot_results(folder, disp, strain, stress):
    nodes, _, elements, _ = pre.readin(folder=folder)
    tri = post.mesh2tri(nodes, elements)

    # S_xx
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    c = ax.tricontourf(tri, stress[:, 0], levels=12)
    cbar = fig.colorbar(c, orientation="horizontal")
    cbar.ax.tick_params(labelsize=16)
    cbar.set_label(r"$\sigma_{xx}$ (MPa)", fontsize=18, labelpad=8)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.axis("image")
    plt.show()

    # S_yy
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    c = ax.tricontourf(tri, stress[:, 1], levels=12)
    cbar = fig.colorbar(c, orientation="horizontal")
    cbar.ax.tick_params(labelsize=16)
    cbar.set_label(r"$\sigma_{yy}$ (MPa)", fontsize=18, labelpad=8)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.axis("image")
    plt.show()

    # tau_xy
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    c = ax.tricontourf(tri, stress[:, 2], levels=12)
    cbar = fig.colorbar(c, orientation="horizontal")
    cbar.ax.tick_params(labelsize=16)
    cbar.set_label(r"$\tau_{xy}$ (MPa)", fontsize=18, labelpad=8)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.axis("image")
    plt.show()

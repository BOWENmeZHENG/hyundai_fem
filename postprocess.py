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


def output_csv(folder, disp, strain, stress):
    """

    :return:
    """
    nodes, _, elements, _ = pre.readin(folder=folder+'/')
    nodes_x = nodes[:, 1]
    nodes_y = nodes[:, 2]
    disp_x = disp[:, 0]
    disp_y = disp[:, 1]
    strain_xx = strain[:, 0]
    strain_yy = strain[:, 1]
    strain_xy = strain[:, 2]
    stress_xx = stress[:, 0]
    stress_yy = stress[:, 1]
    stress_xy = stress[:, 2]

    with open(f"{folder}/{folder}.csv", "w") as f:
        f.write("coorx,coory,dispx,dispy,strainxx,strainyy,strainxy,stressxx,stressyy,stressxy\n")
        for i in range(len(nodes_x)):
            f.write(f"{nodes_x[i]},{nodes_y[i]},{disp_x[i]:.5},{disp_y[i]:.5},{strain_xx[i]:.5},{strain_yy[i]:.5},{strain_xy[i]:.5},{stress_xx[i]:.5},{stress_yy[i]:.5},{stress_xy[i]:.5}\n")
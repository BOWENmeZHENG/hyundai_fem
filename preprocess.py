import os
import pygmsh


def meshing(width=1, height=0.5, radius=0.1, mesh_size=0.02):
    with pygmsh.occ.Geometry() as geom:
        geom.characteristic_length_max = mesh_size
        outer = geom.add_polygon([
            [-width / 2, -height / 2],
            [width / 2, -height / 2],
            [width / 2, height / 2],
            [-width / 2, height / 2],
        ])

        inner = geom.add_disk([0.0, 0.0], radius)
        geom.boolean_difference(outer, inner)
        mesh = geom.generate_mesh()
    return mesh


def write_files(mesh, folder, E=1.0e8, nu=0.3, load=20.0e3):
    mesh_pts = mesh.points
    elements = mesh.cells_dict['triangle']

    os.makedirs(folder, exist_ok=True)

    # Write nodes.txt
    # fix bottom
    with open(f'{folder}nodes.txt', 'w') as f_nodes:
        for i, point in enumerate(mesh_pts):
            if point[0] == min(mesh_pts[:, 0]):
                bc_x, bc_y = -1, -1
            else:
                bc_x, bc_y = 0, 0
            f_nodes.write(f"{i:4} {point[0]:8.4f} {point[1]:8.4f}  {bc_x:4}  {bc_y:4} \n")

    # Write eles.txt
    with open(f'{folder}eles.txt', 'w') as f_eles:
        for i, element in enumerate(elements):
            f_eles.write(f"{i:4}   3   0  {element[0]:4} {element[1]:4}  {element[2]:4} \n")

    # Write mater.txt
    with open(f'{folder}mater.txt', 'w') as f_mater:
        f_mater.write(f"{E:8.4f} {nu:8.4f}")

    # Write loads.txt
    with open(f'{folder}loads.txt', 'w') as f_loads:
        for i, point in enumerate(mesh_pts):
            if point[0] == max(mesh_pts[:, 0]):
                f_loads.write(f"{i:4} {load:8.4f} {0.0:8.4f} \n")



import run_fem
import postprocess


def analysis(width=1.5, height=0.5, radius=0.15, center_x=0.5, center_y=0.075, E=1.0e8, nu=0.3, load=20.0e3,
             plot=False, csv=True):
    disp, strain, stress, folder = run_fem.run(width=width, height=height, radius=radius,
                                               center_x=center_x, center_y=center_y,
                                               E=E, nu=nu, load=load)
    stress /= 1e6  # Unit: MPa

    if plot:
        postprocess.plot_results(folder, disp, strain, stress)
    if csv:
        postprocess.output_csv(folder, disp, strain, stress)

    return folder

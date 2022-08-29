import run_fem
import postprocess

disp, strain, stress, folder = run_fem.run(width=1, height=0.5, radius=0.1,
                                           E=1.0e8, nu=0.3, load=20.0e3)
stress /= 1e6  # Unit: MPa

postprocess.plot_results(folder, disp, strain, stress)
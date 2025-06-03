import numpy as np
from matplotlib.path import Path

def initial_positions(n, r=1):

    # Shift everything by +r to move square to first quadrant
    x_bottom = np.linspace(0, r, n)
    v_bottom = np.zeros_like(x_bottom)

    v_right = np.linspace(0, r, n)
    x_right = r * np.ones_like(v_right)

    x_top = np.linspace(r, 0, n)
    v_top = r * np.ones_like(x_top)

    v_left = np.linspace(r, 0, n)
    x_left = np.zeros_like(v_left)

    # Combine in correct order
    x0s = np.concatenate([x_bottom, x_right, x_top, x_left])
    v0s = np.concatenate([v_bottom, v_right, v_top, v_left])

    return x0s, v0s

def compute_area(xs, vs):
    points = np.column_stack((xs, vs))

    # Ensure closed path
    if not np.allclose(points[0], points[-1]):
        points = np.vstack([points, points[0]])

    path = Path(points)
    area = 0.5 * np.abs(np.sum(points[:-1, 0] * points[1:, 1] - points[1:, 0] * points[:-1, 1]))
    print("Enclosed area:", area)

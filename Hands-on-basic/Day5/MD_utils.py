import numpy as np

def read_xyz_file(filename):
    timesteps = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    i = 0
    n_lines = len(lines)
    while i < n_lines:
        line = lines[i].strip()
        if line.isdigit():
            n_atoms = int(line)
            i += 1
            # Skip any blank lines after the atom count
            while i < n_lines and lines[i].strip() == '':
                i += 1

            positions = []
            for _ in range(n_atoms):
                parts = lines[i].strip().split()
                coords = list(map(float, parts[1:4]))  # skip element symbol
                positions.append(coords)
                i += 1

            timesteps.append(positions)
        else:
            i += 1

    return np.array(timesteps, dtype=float)  # shape: (num_timesteps, n_atoms, 3)

def trajectory_to_xyz(trajectory, filename=None):
    """
    Convert a trajectory array [N_frames, N_atoms, 3] to XYZ format.
    
    Parameters:
        trajectory: np.ndarray
            Trajectory array of shape (N_frames, N_atoms, 3)
        filename: str or None
            If given, the output will be written to this file. If None, a string is returned.

    Returns:
        If filename is None, returns the full XYZ string. Otherwise, writes to file.
    """
    N_frames, N_atoms, _ = trajectory.shape
    lines = []

    for frame in range(N_frames):
        lines.append(str(N_atoms))
        lines.append("")  # Blank line after atom count

        for atom_pos in trajectory[frame]:
            x, y, z = atom_pos
            lines.append(f"Ar {x:.6f} {y:.6f} {z:.6f}")

    xyz_str = "\n".join(lines)

    if filename:
        with open(filename, "w") as f:
            f.write(xyz_str)
    else:
        return xyz_str

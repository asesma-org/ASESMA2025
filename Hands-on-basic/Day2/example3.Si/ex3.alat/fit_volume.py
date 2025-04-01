#%%
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define the Murnaghan equation of state
def murnaghan(V, E0,V0, B0, Bp):
    """
    Murnaghan equation of state

    Parameters:
    V : float or array-like
        Volume
    E0 : float
        Minimum energy
    B0 : float
        Bulk modulus at equilibrium volume
    Bp : float
        Pressure derivative of the bulk modulus

    Returns:
    E : float or array-like
        Energy
    """
    E = E0 + B0*V0 * ( 1/(Bp*(Bp-1)) * (V/V0)**(1-Bp) + 1/Bp*(V/V0)- 1/(Bp-1))
    return E

# Define the quadratic function
def quadratic(V, a, b, c):
    """
    Quadratic function

    Parameters:
    V : float or array-like
        Volume
    a, b, c : float
        Quadratic coefficients

    Returns:
    E : float or array-like
        Energy
    """
    E = a * V**2 + b * V + c
    return E

# Load data from file
data = np.loadtxt('data.dat', delimiter=',', skiprows=1)
# constant ry to joules
RytoJ = 2.1798741e-18
# constant bohr to meters
BohrtoM = 5.2917721e-11
#%%
# Extract the lattice parameter, volume, and total energy
alat = data[:, 0]
V = data[:, 1]
Etot = data[:, 2]

# Initial guess for the fit parameters
V0 = np.mean(V)
E0 = np.min(Etot)
B0 = 0.5
Bp = 0.5

# Fit the data using the Murnaghan equation of state
popt_murnaghan, pcov_murnaghan = curve_fit(murnaghan, V, Etot, p0=[E0,V0, B0, Bp])

# Fit the data using the quadratic function
popt_quadratic, pcov_quadratic = curve_fit(quadratic, V, Etot, p0=[0.0, 0.0, E0])

# Extract the fitted parameters for Murnaghan equation of state
E0_fit_murnaghan, V0_fit_murnaghan, B0_fit_murnaghan, Bp_fit_murnaghan = popt_murnaghan

# Extract the fitted parameters for quadratic fit
a_fit_quadratic, b_fit_quadratic, c_fit_quadratic = popt_quadratic

# Calculate the fitted energy using the Murnaghan equation of state
V_fit = np.linspace(np.min(V), np.max(V), 100)
E_fit_murnaghan = murnaghan(V_fit,  E0_fit_murnaghan,V0_fit_murnaghan, B0_fit_murnaghan, Bp_fit_murnaghan)
# convert ry to joules



# Calculate the fitted energy using the quadratic fit
E_fit_quadratic = quadratic(V_fit, a_fit_quadratic, b_fit_quadratic, c_fit_quadratic)
print(f"Bulk modulus Murnaghan fit: {B0_fit_murnaghan*RytoJ/(BohrtoM**3)/(10**9) :.2f} GPa")
bulk_modules_quad = np.min(V)*2*a_fit_quadratic*RytoJ/(BohrtoM**3)/(10**9)
print(f"Bulk modulus quadratic fit: {bulk_modules_quad} GPa")

# Set up the plot
plt.grid(True)
plt.xlabel('Volume (Bohr^3)', size =16)
plt.ylabel('Total energy (Ry)', size = 16)

# Plot the data
plt.plot(V, Etot, 'bo', label='Data', markersize=10)

# Plot the fitted curve using Murnaghan equation of state
plt.plot(V_fit, E_fit_murnaghan, 'r-', label='Murnaghan Fit')

# Plot the fitted curve using quadratic fit
plt.plot(V_fit, E_fit_quadratic, 'g-', label='Quadratic Fit')

# Show the legend
plt.legend()
plt.savefig("fit.png", dpi=300, bbox_inches='tight')
plt.show()

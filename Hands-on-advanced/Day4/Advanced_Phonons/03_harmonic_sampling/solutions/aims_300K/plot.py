import pandas as pd

s = pd.read_csv("sigmaA_mode_Si.csv", index_col=0)

ax = s.plot(marker=".", lw=0)

ax.set_xlim(0, 20)
ax.set_ylim(0, 0.5)

ax.set_xlabel("$\omega_s$ (THz)")
ax.set_ylabel(r"$\sigma^{\rm A}_s$")
fig = ax.get_figure()
fig.savefig("Mode_resolved_sigma.png")

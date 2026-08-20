import numpy as np
import matplotlib.pyplot as plt

file_path = "../si_dos.dat"
data = np.loadtxt(file_path)

energy, dos = data[1:, 0], data[1:, 1]

plt.figure(figsize=(8, 6))
plt.scatter(energy, dos, s=1, color="blue", label="DOS")

plt.title("Silicon density of states", fontsize=14)
plt.xlabel("Energy [eV]", fontsize=12)
plt.ylabel("Density of states", fontsize=12)
plt.xlim(-6, 16)
plt.grid(True, alpha=0.3)
plt.savefig("silicon_dos.png", dpi=300)
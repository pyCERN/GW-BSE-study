import numpy as np
import matplotlib.pyplot as plt

file_path = './Si.bands.gnu'
with open(file_path, 'r') as f:
    blocks = f.read().strip().split('\n\n')

bands = []
k_points = None

for block in blocks:
    # each block represents one band line
    lines = block.strip().split('\n')
    data = np.array([list(map(float, line.split())) for line in lines if line.strip()])
    
    if len(data) == 0:
        continue
    
    if k_points is None:
        k_points = data[:, 0]  # x축 (k-path)
        
    bands.append(data[:, 1])   # y축 (에너지 eV)

bands = np.array(bands) # Shape: (전체 밴드 수, k점 개수)

# 2 Si atoms -> 8 electrons -> 4 valence bands
num_valence_bands = 4
vbm = np.max(bands[num_valence_bands - 1])
cbm = np.min(bands[num_valence_bands])
band_gap = cbm - vbm

print(f"====================================")
print(f"VBM : {vbm:.4f} eV")
print(f"CBM : {cbm:.4f} eV")
print(f"Band gap  : {band_gap:.4f} eV")
print(f"====================================")

plt.figure(figsize=(6, 8))

for band in bands:
    plt.plot(k_points, band - vbm, color='black', linewidth=1.2)

plt.axhline(0, color='red', linestyle='--', linewidth=1, label='VBM (0 eV)')

high_sym_pos = [0.0000, 0.8660, 1.8660, 2.6566, 3.7173]
high_sym_label = ['L', r'$\Gamma$', 'X', 'K', r'$\Gamma$']
for pos in high_sym_pos:
    plt.axvline(pos, color='gray', linestyle=':')

plt.xticks(high_sym_pos, high_sym_label)
plt.xlabel('k-vector')
plt.ylabel('Energy (eV)')
plt.title('Si Diamond Band Structure')
plt.ylim(-10, 10)
plt.xlim(min(k_points), max(k_points))
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')

# plt.show()
plt.savefig('./si_band.png')
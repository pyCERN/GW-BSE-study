# Density Functional Theory (DFT)
There are two main concepts of DFT:
1. Hohenberg-Kohn theorem
2. Kohn-Sham equation

Two concepts are closely related. With sole Hohenberg-Kohn theorem, one cannot know band or orbital from electron density $n(\textbf{r})$. And with only $n(\textbf{r})$, one cannot solve kinetic energy term in hamiltonian. \
This is where the Kohn-Sham equation kicks in. It separates the kinetic energy into two terms.
$$
T = T_s + (T - T_s)
$$
$T_s$ :  kinetic energy of non-interacting system, which substitutes real system whose electrons are interacting in complicated way.
$$
T_s = -\frac{\hbar^2}{2m_e}\sum_{i}{\int{d\textbf{r}\Phi_{i}^{*}(\textbf{r})\nabla^{2}\Phi_{i}(\textbf{r})}}
$$
$T - T_s$ : small term of kinetic energy difference between real and new system. This goes into exchange-correlation (xc) term. \
Adding potential terms:
$$
E = \langle\hat{H}\rangle = \langle\hat{T}\rangle + \langle\hat{V}_{\mathrm{int}}\rangle + \langle\hat{V}_{\mathrm{ext}}\rangle + E_{II}
$$
$\hat{V}_{\mathrm{int}}$ is represents an interaction between electron-electron. $\hat{V}_{\mathrm{int}}$ is very complex in real, including not only classical Coulomb interaction but also quantum mechanical exchange-correlation effect. \
On the other hand, we can treat electrons as charge distribution with density $n(\textbf{r})$ (mean-field). This term is then called Hartree term. \
So, $\langle \hat{V}_{\mathrm{int}} \rangle - E_{\mathrm{Hartree}}$ is a energy difference when we treat electrons in two ways:
1. Real electrons that exist in discrete way that they create real time repulsive force each other and exchange-correlation hole.
2. Electron gas. Two gases are pulling each other with classical Coulomb potential.
This term also goes into xc term.

These lead to Kohn-Sham equation where non-interacting electron assumption holds (but considering exchange-correlation effect).
$$
\left( -\frac{\hbar^{2}}{2m_{e}} \nabla^2 + V_{\textrm{eff}}(\textbf{r}) \right) \psi_{i}(\textbf{r}) = \epsilon_{i} \psi_{i}(\textbf{r})
$$

However, eigenvalues of the Kohn-Sham equation don't indicate the real system energy, but the energy of each single electron under effective potential.

To get the real energy, one needs to solve this functional:

$$
E[n] = T_{s}[n] + \int{d\textbf{r} V_{\mathrm{ext}} n(\textbf{r})} + E_{\textrm{Hartree}}[n] + E_{II} + E_{\textrm{xc}}[n]
$$

$$
\textrm{where, } V_{\textrm{eff}} = V_{\textrm{ext}} + V_{\textrm{Hartree}} + V_{\textrm{xc}}
$$

---
## Self-consistent loop to get ground state energy
1. Initial guess of electron density $n_{0}(\textbf{r})$
2. Calculate effective potential
$$
V_{\textrm{eff}}(\textbf{r}) = V_{\textrm{ext}}(\textbf{r}) + \int{d\textbf{r}' \frac{n(\textbf{r}')} {|r - r'|}} + V_{\textrm{xc}}(\textbf{r})
$$
3. Solve Kohn-Sham equation and get orbitals $\psi_{i}(\textbf{r})$
4. Derive new density
    - $n_{\textrm{new}}(\textbf{r}) = \sum_{i=1}^{N} |\psi_{i}(\textbf{r})|^{2}$
5. Self-consistency check
    - Compare the old and new density, $|n_{\textrm{new}} - n_{\textrm{old}}| < \textrm{conv\_thr}$
6. Finally get total energy

---
## exchange-correlation term approximation
- LDA (Local density approximation) \
LDA assumes the system as homogeneous electron gas. Then xc term depends only on the density $n(\textbf{r})$.
$$
E_{\textrm{xc}}^{\textrm{LDA}}[n] = \int{d\textbf{r} n(\textbf{r}) \epsilon_{\textrm{xc}}^{\textrm{unif}}}
$$
- GGA (Generalized gradient approximation) \
Electron density changes violently near the core or surface. In this case, we need to consider the derivative of density as well.
$$
E_{\textrm{xc}}^{\textrm{GGA}} = \int{d\textbf{r}} f \left( n(\textbf{r}), \nabla n(\textbf{r}) \right)
$$
- Hybrid functional \
Hartree-Fock approximation only considers exchange effect and successfully cancels out the self-interaction error. Let's say its exchange energy to be $E_{\textrm{x}}^{\textrm{HF}}$ (exact exchange).
$$
E_{\textrm{xc}}^{{\textrm{hybrid}}} = a E_{\textrm{x}}^{\textrm{HF}} + (1 - a) E_{\textrm{x}}^{\textrm{GGA}} + E_{\textrm{c}}^{\textrm{GGA}}
$$
---
## How to solve KS equation and how to assure convergence
How to assure convergence? $\to$ mixing
- Due to the electronic density calculated in iteration $i$, there will be repulsive energy and more density in the other side. This will be oscillating and deteriorate convergence.
- Linear mixing
$$
n_{in}^{i+1} = (1 - \alpha) n_{in}^{i} + \alpha n_{out}^{i}
$$
- Broyden mixing
---
## Pseudopotential
There are two motivations to use pseudopotential:
1. Physical properties are solely determined by valence electrons.
2. Core electrons $(r < r_{c})$ are tightly bound to nuclues and the potential is so intense that the wavefunction oscillates rapidly.

Therefore, the wavefunction of a core electron is spatially localized and has many nodes. To represent this as plane wave basis by performing Fourier transform, the resultant function has long range of momentum (and thus wavevector). And because of rapid oscillation, it is dominated by high frequency component and cutoff energy becomes higher.

Pseudopotential makes the core part smooth. How hard is it to make smooth function?
- Transferability
    - Pseudopotential must apply to general situations of multiple atoms.
- Phase shift
    - It can be treated as scattering process when an electron passes through nucleus. When scattering, angle and phase changes.
    - If pseudopotential does not consider this properly, it will predict absolutely difference physical property.
- Norm-conserving
    - Pseudopotential must give same charge in core region as the real charge.

### Ultrasoft Pseudopotential (USPP)
- Limitation on norm-conserving constraint
    - What if electrons are extremely localized near nucleus and smoothing does not work?
    - Then give up norm-conserving constraint.
    - This will underestimate the total charge and it needs to add augmented charge somewhere.
    - This leads to generalized eigenvalue problem.
        - $\hat{H}^{\textrm{KS}} \psi_{i} = \epsilon_{i} \hat{S} \psi_{i}$, where $\hat{S}$ is overlap operator.

### Projector Augmented Wave (PAW)

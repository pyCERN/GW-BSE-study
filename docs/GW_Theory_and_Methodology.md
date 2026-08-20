# GW approximation
GW approximation is motivated by limitations of DFT.
- Predict exact band gap
    - DFT only checks one electron's orbital and energy. And complex quantum mechanical interaction between electrons is approximated by exchange-correlation term. This approximation induces self-interaction error.
    - DFT methods such as LDA and GGA approximates Hartree-Fock approximation and contain self-interaction error. Then electrons feel additional repulsive potential by themselves and tend to delocalize. This underestimates real band gap significantly.
- Predict exact energy in excited state

GW approximation considers not just one electron but its surrounding polarization effect when the electron propagates through dielectric material. The polarization effect weakens the effective potential applying to electron by inverse dielectric constant: $V = \frac{V_{0}} {\epsilon}$. This weakening replaces with exchange-correlation approximation in DFT and more accurately calculate the energy.

This energy represents the real energy when an electron is being emitted or absorbing, unlike the unphysical property of Kohn-Sham equation eigenvalue.

## Quasiparticle
GW approximation solves these problems by handling the state of quasiparticle. Electrons move in the matter repelling other electrons. This creates temporary change in charge density, which is called polarization. This polarization is seen as cloud at the point of view of the electron just like a car kicking up dust. This electron and the polarization cloud act as a particle.

DFT calculates ground state density and energy of electron. Now GW method focuses on calculating energy of quasiparticle.

GW approximation is theoretical framework of system's response to perturbation, which is consistent with photoemission spectroscopy.

## Screening effect and dielectric matrix
In material, the electrostatic potential between two electrons is weakend by other surrounding electrons. This effect is represented by dielectric function $\epsilon$. Dielectric function indicates how much the system will be polarized in response of external electric field. The dielectric function is formulated as a matrix if the system is anisotropic and polarization happens in other direction.

In many-body theory and GW calculation, it needs to calculate this term to know the true potential that one electron feels. 
this is termed as $W$ representing screened Coulomb interaction.

## Green function
Green function helps understand the response of the solution of differential equation to some source. Electrons keep moving. In GW approximation, the Green function $G(\textbf{r}, \textbf{r}')$ indicates the propagation of probability of the electron to be at $\textbf{r}'$ when applying energy to the electron at $\textbf{r}$. This describes the situation of photon hitting the electron and it goes up to conduction band.

## Self-energy
Our goal is to get self-energy $\Sigma$. This is an energy that one electron feels by interacting with surrounding polarization cloud.

The self-energy is formally expressed as:
$$
\Sigma = iGW
$$
where $G$ is the Green's function that describes how electrons propagate, and $W$ is the screened Coulomb interaction that describes how the surrounding environment dynamically screens the interaction.
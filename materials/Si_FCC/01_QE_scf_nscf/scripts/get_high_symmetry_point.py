from ase.build import bulk
from ase.dft.kpoints import bandpath

si = bulk('Si', 'diamond', a=5.431)
# path = si.cell.bandpath(path="LGXKG", npoints=80)
path = si.cell.bandpath(npoints=80)
path.write("bandpath_for_si_diamond.json")
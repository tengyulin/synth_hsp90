# Cryo-EM Synthethic Generation for Hsp90 Molecule.
We used the [same workflow](https://github.com/tengyulin/synth_nlrp3.git) for the Hsp90 molecule, which was the molecule used in the original work by Seitz, E. For our experiment, we followed the original work and used PyMOL to create the second conformational change using the command: `pymol -cq CM2_pymol.py`.


## Refences
This workflow is highly inspired by the [cryoEM_synthetic_generation](https://github.com/evanseitz/cryoEM_synthetic_generation) reposity from [Evan Seitz](https://github.com/evanseitz). Further details can be found in their paper **Simulation of Cryo-EM Ensembles from Atomic Models of Molecules Exhibiting Continuous Conformations** by Seitz, Acosta-Reyes, Schwander, and Frank, available at:  https://www.biorxiv.org/content/10.1101/864116v1.

We changed the occupancy map for the purpose of our experiment. 
import os
from chimera import runCommand as rc

# INSTRUCTIONS: run this file from same directory as your PDB file are located... 
	# CM1 states will output to CMs folder

pyDir = os.path.dirname(os.path.abspath(__file__)) #python file location
parDir = os.path.abspath(os.path.join(pyDir, os.pardir))
outDir = os.path.join(pyDir, 'CM1')
monoA = os.path.join(pyDir, 'monoA_snip.pdb')
monoB = os.path.join(pyDir, 'monoB_snip.pdb')

rc('open' + monoB)
rc('open' + monoA)
rc('select :677.a') #select central hinge atom (LEU 674)

rot = 1.0
states = 20
for i in range(1,states+1): # numbers of states to generate
    if i == 1: #don't rotate for state 1
        rc('combine #0-1, name CM1_%s' % i)
        rc('write relative #0 format pdb #2 %s/CM1_0%s.pdb' % (outDir,i))
    else:
        rc('turn 0,1,0 %f center sel models #0' % rot)
        rc('combine #0-1, name CM1_%s' % i)
        if i < 10:
            rc('write relative #0 format pdb #2 %s/CM1_0%s.pdb' % (outDir,i))
        else:
            rc('write relative #0 format pdb #2 %s/CM1_%s.pdb' % (outDir,i))
    rc('close #2')
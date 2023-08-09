# script to re-center all PDBs based on common center-of-mass coordinates

for i in /home/danlin/synth_hsp90/1_CMs/CM2/*.pdb
do
    out=`basename $i`
    outFile=/home/danlin/synth_hsp90/1_CMs/align_CMs/$out
    echo "$outFile"
    phenix.pdbtools "${i}" output.file_name=$outFile sites.translate="115.40 58.36 -39.54" #replace with CoM of your pdb
done


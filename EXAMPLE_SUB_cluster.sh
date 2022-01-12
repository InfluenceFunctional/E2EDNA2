#!/bin/bash
#SBATCH --account=ACCOUNT
#SBATCH --gres=gpu:v100:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=0-4:00
#SBATCH --mail-user=YOUR EMAIL
#SBATCH --mail-type=END

# put your MMB path here. Don't use ~
export LD_LIBRARY_PATH="/home/taoliu/projects/def-simine/programs/MMB/Installer.2_14.Linux64"

module load python/3.7
#module load StdEnv/2020
#module load gcc/9.3.0
#module load openmpi/4.0.3
#module load cuda/11.0

# To load AmberTools21 (from https://docs.computecanada.ca/wiki/AMBER)
# to use tleap to generate .prmtop file
#module load StdEnv/2020 gcc/9.3.0 cuda/11.0 openmpi/4.0.3 ambertools/21
#source $EBROOTAMBERTOOLS/amber.sh
# Or load AmberTools20 (GPU version)
module load StdEnv/2020  gcc/9.3.0  cuda/11.0  openmpi/4.0.3 amber/20.9-20.15

module load python openmm

virtualenv --no-download $SLURM_TMPDIR/env  # need to load a Python module before running virtualenv
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip
pip install --no-index MDAnalysis
pip install --no-index lightdock
pip install --no-index -r requirements.txt

#pip install numpy==1.20.2
#pip install --no-index numpy==1.20.2  # why didn't Michael use --no-index here?
#pip install /cvmfs/soft.computecanada.ca/custom/python/wheelhouse/gentoo/generic/numpy-1.20.2+computecanada-cp37-cp37m-linux_x86_64.whl

#ambertools21 and ambertools20 seems to contain numpy already: numpy-1.21.2
pip install --no-index --upgrade numpy
# Without this upgrade, numpy tends to give error for some packages such as mdtraj on beluga (2021-10-08)

pip install ~/projects/def-simine/programs/opendnaWheels/seqfold-0.7.7-py3-none-any.whl
pip install ~/projects/def-simine/programs/opendnaWheels/PeptideBuilder-1.1.0-py3-none-any.whl 
# https://pypi.org/project/PeptideBuilder/1.1.0/
# https://www.wheelodex.org/projects/peptidebuilder/
pip install ~/projects/def-simine/programs/opendnaWheels/nupack-4.0.0.23-cp37-cp37m-linux_x86_64.whl
python -c "import simtk.openmm"

date -u
# seq1:
python ./main.py --run_num=1 --sequence='AACGCTTTTTGCGTA' --peptide='A' --walltime=10 --temperature=310 --pH=7.4 --ionicStrength=0.163 --Mg=0.05 --impSolv='HCT'

date -u

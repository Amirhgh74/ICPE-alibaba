#!/bin/bash
#SBATCH --mail-user=haghshenas.amir74@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --account=def-naser2
#SBATCH --cpus-per-task=6
#SBATCH --mem=120G
#SBATCH --time=0-10:00:00
module load python/3.8.10
source ~/venv/bin/activate

python read_files.py





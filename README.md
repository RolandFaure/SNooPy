# SNooPy
metagenomic SNP caller

## Installation
SNooPy is a python file, which does not need compilation. You will need to have an environment with python3, scipy, numpy, pandas, pysam and sklearn installed. You can create such an environment in conda:
```
conda create -n snoopy_env -y -c bioconda -c conda-forge numpy scipy scikit-learn pysam pandas
```

## Usage
```
python snoopy.py --help

usage: snoopy.py [-h] -r REFERENCE -b BAM -o OUT [-t THREADS]
                     [--window WINDOW] [--benchmark]

optional arguments:
  -h, --help            show this help message and exit
  -r REFERENCE, --reference REFERENCE
                        Reference genome in FASTA format
  -b BAM, --bam BAM     Alignment file in BAM format
  -o OUT, --out-folder OUT
                        Name of the output folder
  -t THREADS, --threads THREADS
                        Number of threads to use [1]
  --window WINDOW       Size of window to perform read separation. Must be at
                        least twice shorter than average read length. 0 for
                        auto [0]
  --benchmark           Use if benchmarking to compare against other variant
                        callers [False]
```

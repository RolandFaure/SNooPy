# SNooPy
metagenomic SNP caller for long-read sequencing data. Preprint: [https://www.biorxiv.org/content/biorxiv/early/2025/12/02/2025.12.01.691549.full.pdf](https://www.biorxiv.org/content/biorxiv/early/2025/12/02/2025.12.01.691549.full.pdf). SNooPy relies on a statistical model tailored for metagenomics. At the moment where we ran our tests, it greatly outperformed other callers such as DeepVariant, Longshot and Bcftools on metagenomic datasets.

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
### Input
SNooPy expects as input a reference genome (FASTA format) and a set of reads aligned to this reference in [BAM format](https://samtools.github.io/hts-specs/SAMv1.pdf), as provided e.g. by [minimap2](https://github.com/lh3/minimap2). You can obtain the BAM file by running, for example:
```
minimap2 -ax map-ont reference.fa reads.fq | samtools view -Sb | samtools sort -o alignment.bam
```

## Citation
Please cite SNooPy using the preprint:
```
Faure, Roland & Faure, Ulysse & Truong, Tam & Derzelle, Alessandro & Lavenier, Dominique & Flot, Jean-François & Quince, Christopher. (2025). SNooPy: a statistical framework for long-read metagenomic variant calling. 10.64898/2025.12.01.691549. 
```

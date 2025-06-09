import subprocess
import sys
import os

def run_qe(input_file):
    output_file = os.path.splitext(input_file)[0] + ".out"
    command = f"pw.x < {input_file} > {output_file}"
    subprocess.run(command, shell=True)

# Get input file from command line
if len(sys.argv) != 2:
    print("Usage: python3 run_qe.py inputfile")
    sys.exit(1)

# Run QE calculation
run_qe(sys.argv[1])


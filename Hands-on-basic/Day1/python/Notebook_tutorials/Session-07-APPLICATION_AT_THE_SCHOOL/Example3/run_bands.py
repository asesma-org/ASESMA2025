import subprocess
import sys
import os

def run_bands(input_file):
    output_file = os.path.splitext(input_file)[0] + ".out"
    command = f"bands.x < {input_file} > {output_file}"
    subprocess.run(command, shell=True)

# Get input file from command line
if len(sys.argv) != 2:
    print("Usage: python3 run_qe.py inputfile")
    sys.exit(1)

# Run bands calculation
run_bands(sys.argv[1])


import os
import subprocess

N_REPLICATES = 20
TREE_OUT_DIR = os.path.join('indelible', 'trees')
ALIGN_OUT_DIR = os.path.join('results', 'alignments')
SEQGEN_EXE = os.path.join('bin', 'seq-gen.exe')  # Use .exe for Windows
N_SITES = 1000
INDELIBLE_EXE = os.path.join('bin', 'INDELible.exe')

os.makedirs(ALIGN_OUT_DIR, exist_ok=True)

for rep in range(1, N_REPLICATES + 1):
    tree_file = os.path.join(TREE_OUT_DIR, f'rep_{rep}.tree')
    align_file = os.path.join(ALIGN_OUT_DIR, f'rep_{rep}.phy')
    if os.path.exists(align_file):
        print(f"Replicate {rep}: Alignment already exists, skipping.")
        continue
    if not os.path.exists(tree_file):
        print(f"Replicate {rep}: Tree file not found, skipping.")
        continue
    print(f"Running Seq-Gen for replicate {rep}...")
    with open(tree_file, 'r') as tf:
        tree_str = tf.read().strip()
    # Run Seq-Gen
    result = subprocess.run([
        SEQGEN_EXE,
        '-m', 'JC',
        '-l', str(N_SITES),
        '-n', '1',
        '-of',  # Output in PHYLIP format
    ], input=tree_str.encode(), capture_output=True)
    
    if result.returncode != 0:
        print(f"  ❌ Seq-Gen failed for replicate {rep}:")
        print(f"  stderr: {result.stderr.decode()}")
        continue
        
    with open(align_file, 'wb') as af:
        af.write(result.stdout)
    print(f"  ✅ Successfully generated alignment for replicate {rep}")
print("Seq-Gen runs complete.") 
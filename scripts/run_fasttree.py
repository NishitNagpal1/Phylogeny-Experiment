import os
import subprocess

N_REPLICATES = 20
ALIGN_OUT_DIR = os.path.join('results', 'alignments')
TREE_EST_OUT_DIR = os.path.join('results', 'fasttree_trees')
FASTTREE_EXE = os.path.join('bin', 'FastTree.exe')

os.makedirs(TREE_EST_OUT_DIR, exist_ok=True)

for rep in range(1, N_REPLICATES + 1):
    align_file = os.path.join(ALIGN_OUT_DIR, f'rep_{rep}.phy')
    tree_file = os.path.join(TREE_EST_OUT_DIR, f'rep_{rep}.tree')
    if os.path.exists(tree_file) and os.path.getsize(tree_file) > 0:
        print(f"Replicate {rep}: Estimated tree already exists, skipping.")
        continue
    if not os.path.exists(align_file):
        print(f"Replicate {rep}: Alignment file not found, skipping.")
        continue
    print(f"Running FastTree for replicate {rep}...")
    
    with open(align_file, 'r') as af:
        result = subprocess.run([
            FASTTREE_EXE,
            '-nt',  # nucleotide
            '-quiet',  # reduce output
        ], stdin=af, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"  ❌ FastTree failed for replicate {rep}:")
        print(f"  stderr: {result.stderr}")
        continue
    
    if result.stdout.strip():
        with open(tree_file, 'w') as tf:
            tf.write(result.stdout)
        print(f"  ✅ Successfully generated tree for replicate {rep}")
    else:
        print(f"  ⚠️  FastTree produced no output for replicate {rep}")

print("FastTree runs complete.") 
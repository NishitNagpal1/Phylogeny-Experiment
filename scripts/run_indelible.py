import os
import subprocess
import shutil

N_REPLICATES = 20
CONTROL_DIR = os.path.join('indelible')
TREE_OUT_DIR = os.path.join('indelible', 'trees')
INDELIBLE_EXE = os.path.join('bin', 'INDELible.exe')  # Use .exe for Windows

os.makedirs(TREE_OUT_DIR, exist_ok=True)

for rep in range(1, N_REPLICATES + 1):
    control_file = os.path.join(CONTROL_DIR, f'control_{rep}.txt')
    rep_out_dir = os.path.join(TREE_OUT_DIR, f'rep_{rep}')
    os.makedirs(rep_out_dir, exist_ok=True)
    # Copy control file as control.txt in output dir
    control_dest = os.path.join(rep_out_dir, 'control.txt')
    shutil.copyfile(control_file, control_dest)
    # INDELible outputs to current directory, so run in rep_out_dir
    if os.path.exists(os.path.join(rep_out_dir, f'output{rep}.fas')):
        print(f"Replicate {rep}: Output already exists, skipping.")
        continue
    print(f"Running INDELible for replicate {rep}...")
    result = subprocess.run([
        INDELIBLE_EXE
    ], cwd=rep_out_dir, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"  ❌ INDELible failed for replicate {rep}:")
        print(f"  stdout: {result.stdout}")
        print(f"  stderr: {result.stderr}")
        continue
    
    # Check for trees.txt file and extract tree
    trees_file = os.path.join(rep_out_dir, 'trees.txt')
    if os.path.exists(trees_file):
        print(f"  ✅ Successfully generated tree for replicate {rep}")
        # Extract tree string from trees.txt and save as separate .tree file
        with open(trees_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('output') and not line.startswith('FILE'):
                    tree_string = line.strip().split('\t')[-1]  # Last column is tree string
                    tree_output = os.path.join(TREE_OUT_DIR, f'rep_{rep}.tree')
                    with open(tree_output, 'w') as tree_f:
                        tree_f.write(tree_string + '\n')
                    print(f"  📁 Tree saved to {tree_output}")
                    break
    else:
        print(f"  ⚠️  Trees file not found for replicate {rep}")

print("INDELible runs complete.") 
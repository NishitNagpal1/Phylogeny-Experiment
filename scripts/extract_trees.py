import os

N_REPLICATES = 20
TREE_OUT_DIR = os.path.join('indelible', 'trees')

for rep in range(1, N_REPLICATES + 1):
    rep_out_dir = os.path.join(TREE_OUT_DIR, f'rep_{rep}')
    trees_file = os.path.join(rep_out_dir, 'trees.txt')
    
    if os.path.exists(trees_file):
        print(f"Extracting tree for replicate {rep}...")
        with open(trees_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('output') and not line.startswith('FILE'):
                    tree_string = line.strip().split('\t')[-1]  # Last column is tree string
                    tree_output = os.path.join(TREE_OUT_DIR, f'rep_{rep}.tree')
                    with open(tree_output, 'w') as tree_f:
                        tree_f.write(tree_string + '\n')
                    print(f"  SUCCESS: Tree saved to {tree_output}")
                    break
    else:
        print(f"  ERROR: Trees file not found for replicate {rep}")

print("Tree extraction complete!") 
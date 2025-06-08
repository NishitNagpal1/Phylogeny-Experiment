import os
import shutil

N_REPLICATES = 20
TREE_OUT_DIR = os.path.join('indelible', 'trees')
ALIGN_OUT_DIR = os.path.join('results', 'alignments')

os.makedirs(ALIGN_OUT_DIR, exist_ok=True)

for rep in range(1, N_REPLICATES + 1):
    rep_out_dir = os.path.join(TREE_OUT_DIR, f'rep_{rep}')
    indelible_align = os.path.join(rep_out_dir, f'output{rep}_TRUE.phy')
    target_align = os.path.join(ALIGN_OUT_DIR, f'rep_{rep}.phy')
    
    if os.path.exists(indelible_align):
        shutil.copyfile(indelible_align, target_align)
        print(f"SUCCESS: Copied alignment for replicate {rep}")
    else:
        print(f"ERROR: Alignment not found for replicate {rep}")

print("Alignment copying complete! INDELible alignments are now ready for FastTree.") 
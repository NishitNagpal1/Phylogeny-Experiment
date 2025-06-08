#!/usr/bin/env python3
import os
import random

# -------------------- PARAMETERS --------------------
N_REPLICATES = 20
N_TAXA       = 10

IND_DIR      = 'indelible'            # where to put control files
CTRL_DIR     = IND_DIR
# ----------------------------------------------------

os.makedirs(CTRL_DIR, exist_ok=True)

# Generate different random tree for each replicate using seeds
# Reduced sequence length to make reconstruction more challenging
TEMPLATE = """[TYPE] NUCLEOTIDE 1

[MODEL] model0
    [submodel] JC

[TREE] tree0 
    [unrooted] {ntaxa}
    [seed] {seed}

[PARTITIONS] part0 [tree0 model0 200]

[EVOLVE] part0 1 output{rep}
"""

for rep in range(1, N_REPLICATES + 1):
    # Use different seed for each replicate to get different random trees
    seed = 1000 + rep * 123  # Different seed for each replicate
    control_content = TEMPLATE.format(
        rep=rep,
        ntaxa=N_TAXA,
        seed=seed
    )
    control_path = os.path.join(CTRL_DIR, f'control_{rep}.txt')
    with open(control_path, 'w') as fh:
        fh.write(control_content)

print(f"Generated {N_REPLICATES} INDELible control files with random trees")
print(f"Each replicate uses a different seed to generate varied tree topologies")
print(f"Parameters: ntaxa={N_TAXA}, sequence_length=200bp (reduced for more challenging reconstruction)")

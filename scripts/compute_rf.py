import os
import dendropy
import csv

N_REPLICATES = 20
TRUE_TREE_DIR = os.path.join('indelible', 'trees')
EST_TREE_DIR = os.path.join('results', 'fasttree_trees')
OUT_CSV = os.path.join('results', 'rf_distances.csv')

rows = [('replicate', 'rf_distance')]

for rep in range(1, N_REPLICATES + 1):
    true_tree_path = os.path.join(TRUE_TREE_DIR, f'rep_{rep}.tree')
    est_tree_path = os.path.join(EST_TREE_DIR, f'rep_{rep}.tree')
    if not (os.path.exists(true_tree_path) and os.path.exists(est_tree_path)):
        print(f"Replicate {rep}: Missing tree file(s), skipping.")
        continue
    try:
        # Create a shared taxon namespace
        tns = dendropy.TaxonNamespace()
        
        # Load both trees using the same taxon namespace
        true_tree = dendropy.Tree.get(path=true_tree_path, schema='newick', 
                                     taxon_namespace=tns, rooting='force-unrooted')
        est_tree = dendropy.Tree.get(path=est_tree_path, schema='newick', 
                                    taxon_namespace=tns, rooting='force-unrooted')
        
        # Compute Robinson-Foulds distance
        rf = dendropy.calculate.treecompare.symmetric_difference(true_tree, est_tree)
        rows.append((rep, rf))
        print(f"Replicate {rep}: RF distance = {rf}")
    except Exception as e:
        print(f"Replicate {rep}: Error processing trees - {e}")

with open(OUT_CSV, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print(f"RF distances written to {OUT_CSV}") 
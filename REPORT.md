# Phylogenetic Reconstruction Accuracy Assessment: A Simulation Study of FastTree Performance

## Abstract

We conducted a simulation study to evaluate the accuracy of FastTree phylogenetic reconstruction under the Jukes-Cantor model of sequence evolution. Using INDELible, we generated 20 random tree topologies with 10 taxa and simulated DNA sequence evolution with 200bp alignments. FastTree was used to reconstruct phylogenies from the simulated sequences, and topological accuracy was quantified using Robinson-Foulds (RF) distances. Our results show a mean RF distance of 3.0 (SE = 0.553) with a range of 0-8, indicating moderate reconstruction accuracy with considerable variation across different tree topologies.

## Introduction

Phylogenetic reconstruction is a fundamental task in evolutionary biology, with numerous methods available for inferring evolutionary relationships from molecular sequence data. FastTree is a widely-used approximate maximum-likelihood method designed for large-scale phylogenetic analysis. However, the accuracy of FastTree under different conditions remains an important question for practitioners.

Simulation studies provide a controlled framework for evaluating phylogenetic methods, as the true evolutionary history is known. By comparing reconstructed trees to the true trees used for simulation, we can quantify reconstruction accuracy and identify factors that influence performance.

The objective of this study was to assess FastTree's phylogenetic reconstruction accuracy using simulated DNA sequences evolving under the Jukes-Cantor substitution model on random tree topologies.

## Methods

### Experimental Design
We implemented a simulation pipeline consisting of tree generation, sequence evolution, phylogenetic reconstruction, and accuracy assessment. The experiment comprised 20 independent replicates, each using a different random tree topology.

### Tree Generation
Random unrooted trees with 10 taxa were generated using INDELible v1.03. Each replicate used a unique seed value (1000 + replicate × 123) to ensure topological diversity across replicates. Tree depth was standardized to 1.0 time units.

### Sequence Evolution
DNA sequence evolution was simulated using INDELible's built-in sequence evolution capabilities under the Jukes-Cantor model. Sequences of 200 base pairs were generated for each taxon. This sequence length was selected to provide sufficient phylogenetic signal while maintaining reconstruction challenge.

### Phylogenetic Reconstruction
FastTree v2.1.11 was used to reconstruct maximum-likelihood phylogenies from the simulated DNA alignments under the Jukes-Cantor model. Default parameters were used for all reconstructions.

### Accuracy Assessment
Topological accuracy was quantified using Robinson-Foulds (RF) distances between true and estimated trees. RF distances were calculated using the `symmetric_difference()` function from the DendroPy library, which computes twice the number of differing bipartitions between two trees.

### Statistical Analysis
Summary statistics (mean, standard error) were calculated for the distribution of RF distances across all replicates. Results were visualized using histograms and boxplots.

## Results

### Robinson-Foulds Distance Distribution
The RF distances between true and estimated trees ranged from 0 to 8, with a mean of 3.0 (SE = 0.553). The distribution showed considerable variation in reconstruction accuracy across replicates.

**RF Distance Summary:**
- Mean: 3.0
- Standard Error: 0.553
- Range: 0-8
- Perfect reconstructions (RF = 0): 4/20 (20%)
- Moderate errors (RF = 2-4): 12/20 (60%)
- Large errors (RF = 6-8): 4/20 (20%)

### Reconstruction Performance
FastTree achieved perfect topological reconstruction (RF = 0) in 20% of cases, indicating that under favorable conditions, the method can accurately recover the true phylogeny. However, 80% of reconstructions showed some degree of topological error, with RF distances of 2, 4, 6, or 8.

The observed RF distances are even-numbered, which is expected since RF distances represent twice the number of differing bipartitions and must be even for unrooted trees.

## Discussion

### Reconstruction Accuracy
Our results indicate that FastTree shows moderate accuracy for phylogenetic reconstruction of 10-taxon trees with 200bp sequences under the Jukes-Cantor model. The mean RF distance of 3.0 represents a relatively small number of topological differences, considering that the maximum possible RF distance for 10-taxon trees is 14.

### Sequence Length Impact
The choice of 200bp sequence length proved critical for creating an appropriate level of reconstruction challenge. Preliminary experiments with 1000bp sequences resulted in trivially easy reconstruction (RF distances of only 0 or 2), while 200bp sequences produced a more realistic range of reconstruction difficulties.

### Method Limitations
Several technical constraints influenced our experimental design:
1. Birth-death tree generation in INDELible encountered runtime errors, necessitating the use of random trees with fixed seeds
2. Random trees may not fully represent the diversity of phylogenetic signal found in real evolutionary scenarios
3. The Jukes-Cantor model represents the simplest case of sequence evolution and may not capture the complexity of real molecular evolution

### Implications
These results suggest that FastTree performs reasonably well for small phylogenies under simple evolutionary models, but practitioners should be aware that topological errors are common. The substantial variation in reconstruction accuracy (RF distances 0-8) indicates that phylogenetic signal varies considerably across different tree topologies and sequence realizations.

## Conclusion

Our simulation study demonstrates that FastTree achieves moderate accuracy for phylogenetic reconstruction of 10-taxon trees, with perfect reconstruction in 20% of cases and varying degrees of topological error in the remainder. The mean RF distance of 3.0 indicates generally good performance, but the range of 0-8 highlights the importance of assessing reconstruction uncertainty in empirical phylogenetic analyses.

Future work could extend this analysis to larger trees, different sequence lengths, more complex evolutionary models, and alternative reconstruction methods to provide a more comprehensive assessment of phylogenetic reconstruction accuracy.

## Technical Implementation

The complete experimental pipeline was implemented in Python, including:
- `generate_indelible_controls.py`: Control file generation for INDELible
- `run_indelible.py`: Automated INDELible execution
- `run_fasttree.py`: Automated FastTree reconstruction
- `compute_rf.py`: Robinson-Foulds distance calculation using DendroPy
- `analyze_results.py`: Statistical analysis and visualization

All code and results are available in the project repository for reproducibility.


# Phylogenetic Simulation Experiment

A simulation study evaluating FastTree phylogenetic reconstruction accuracy using randomly generated trees and synthetic DNA sequences.

## Overview

This project implements a complete phylogenetic simulation pipeline to assess the performance of FastTree under the Jukes-Cantor model of DNA sequence evolution. The study generates random tree topologies, simulates sequence evolution, reconstructs phylogenies, and quantifies accuracy using Robinson-Foulds distances.

## Key Results

- **Mean RF Distance**: 3.0 (SE = 0.553)
- **RF Range**: 0-8 across 20 replicates
- **Perfect Reconstruction**: 20% of cases (RF = 0)
- **Sequence Length**: 200bp (optimized for realistic reconstruction challenge)

## Project Structure

```
├── scripts/                          # Python pipeline scripts
│   ├── generate_indelible_controls.py    # Generate INDELible control files
│   ├── run_indelible.py                  # Execute INDELible simulations
│   ├── run_fasttree.py                   # Run FastTree reconstructions
│   ├── compute_rf.py                     # Calculate Robinson-Foulds distances
│   ├── analyze_results.py                # Statistical analysis and plotting
│   └── run_full_experiment.py            # Master pipeline script
├── results/                           # Experimental results
│   ├── rf_distances.csv                  # RF distance data
│   └── figures/                          # Generated plots
├── indelible/                         # INDELible configuration and output
├── requirements.txt                   # Python dependencies
├── REPORT.md                         # Detailed project report
└── README.md                         # This file
```

## Quick Start

### Prerequisites
- Python 3.x
- INDELible v1.03
- FastTree v2.1.11

### Installation
```bash
git clone https://github.com/yourusername/phylogenetic-simulation
cd phylogenetic-simulation
pip install -r requirements.txt
```

### Running the Experiment
```bash
# Generate control files
python scripts/generate_indelible_controls.py

# Run complete pipeline
python scripts/run_full_experiment.py

# Or run steps individually:
python scripts/run_indelible.py
python scripts/run_fasttree.py
python scripts/compute_rf.py
python scripts/analyze_results.py
```

## Methodology

1. **Tree Generation**: Random 10-taxon unrooted trees with unique seeds
2. **Sequence Evolution**: 200bp DNA sequences under Jukes-Cantor model
3. **Phylogenetic Reconstruction**: FastTree maximum-likelihood estimation
4. **Accuracy Assessment**: Robinson-Foulds distance calculation using DendroPy
5. **Statistical Analysis**: Summary statistics and visualization

## Key Findings

- FastTree shows moderate reconstruction accuracy for small trees
- Sequence length critically impacts reconstruction difficulty
- Substantial variation in performance across different topologies
- 20% perfect reconstruction rate indicates good performance under favorable conditions

## Technical Notes

- Used seeded random trees instead of birth-death trees due to INDELible compatibility issues
- INDELible handles both tree generation and sequence evolution in single pipeline
- Optimized sequence length (200bp) for realistic reconstruction challenge
- Robinson-Foulds distances calculated using DendroPy's `symmetric_difference()` function

## Dependencies

See `requirements.txt` for complete Python package requirements. Main dependencies:
- `dendropy` - Phylogenetic computing library
- `matplotlib` - Plotting and visualization
- `numpy` - Numerical computing

## Citation

If you use this code in your research, please cite:

```
[Your Name]. (2024). Phylogenetic Simulation Experiment: FastTree Accuracy Assessment. 
GitHub repository: https://github.com/yourusername/phylogenetic-simulation
```

## License

This project is available under the MIT License. See LICENSE file for details.

## Contact

[Your Name] - [your.email@example.com]

Project Link: [https://github.com/yourusername/phylogenetic-simulation](https://github.com/yourusername/phylogenetic-simulation) 
#!/usr/bin/env python3
"""
Master script to run the complete phylogenetic simulation experiment.
"""

import subprocess
import sys
import os

def run_script(script_name, description):
    """Run a script and check for errors."""
    print(f"\n{'='*60}")
    print(f"STEP: {description}")
    print(f"Running: {script_name}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print("Warnings:", result.stderr)
        print(f"SUCCESS: {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR in {description}:")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"ERROR: Unexpected error in {description}: {e}")
        return False

def main():
    print("PHYLOGENETIC SIMULATION EXPERIMENT")
    print("====================================")
    
    # Define the workflow steps
    steps = [
        ("scripts/extract_trees.py", "Extract trees from INDELible output"),
        ("scripts/copy_indelible_alignments.py", "Copy sequence alignments"),
        ("scripts/compute_rf.py", "Compute Robinson-Foulds distances"),
        ("scripts/analyze_results.py", "Analyze results and create figures")
    ]
    
    # Run each step
    for script, description in steps:
        if not run_script(script, description):
            print(f"\nEXPERIMENT FAILED at step: {description}")
            print("Please check the error messages above and fix any issues.")
            sys.exit(1)
    
    print(f"\n{'='*60}")
    print("EXPERIMENT COMPLETED SUCCESSFULLY!")
    print("Results are available in:")
    print("   - results/rf_distances.csv (Robinson-Foulds distances)")
    print("   - results/figures/ (plots and visualizations)")
    print(f"{'='*60}")

if __name__ == "__main__":
    main() 
import sys
import importlib.util


def check_dependencies():
    required_packages = ['pandas', 'numpy', 'matplotlib', 'requests']
    missing_packages = []

    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    for package in required_packages:
        spec = importlib.util.find_spec(package)

        if spec is None:
            print(f"[FAIL] {package} - Missing")
            missing_packages.append(package)
        else:
            try:
                module = importlib.import_module(package)
                version = getattr(module, '__version__', 'unknown')
                print(f"[OK] {package} ({version}) - Ready")
            except ImportError:
                print(f"[FAIL] {package} - Error loading")
                missing_packages.append(package)

    print()

    if missing_packages:
        print(f"CRITICAL ERROR: {len(missing_packages)} modules missing.")
        print("To fix this, choose your weapon (package manager):")
        print("1. Using pip (Standard):")
        print("   pip install -r requirements.txt")
        print("2. Using Poetry (Advanced):")
        print("   poetry install")
        print("   poetry run python loading.py")
        return False

    return True


def analyze_matrix_data():
    print("Analyzing Matrix data...")

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("Processing 1000 data points...")

    np.random.seed(42)
    data = {
        'Agent_Type': np.random.choice(['Smith', 'Brown', 'Jones'], 1000),
        'Signal_Strength': np.random.normal(50, 15, 1000),
        'Anomaly_Level': np.random.uniform(0, 1, 1000)
    }

    df = pd.DataFrame(data)

    summary = df.groupby('Agent_Type')['Signal_Strength'].mean()
    print("\nAverage Signal Strength by Agent:")
    print(summary)

    print("\nGenerating visualization...")
    plt.figure(figsize=(10, 6))

    plt.hist(df['Signal_Strength'], bins=30, color='green',
             alpha=0.7, edgecolor='black')
    plt.title('Matrix Signal Distribution')
    plt.xlabel('Signal Strength')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)

    output_file = 'matrix_analysis.png'
    plt.savefig(output_file)
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main():
    if check_dependencies():
        analyze_matrix_data()
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()

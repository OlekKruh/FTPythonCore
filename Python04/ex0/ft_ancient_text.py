filepath = "../data-generator-tools/ancient_fragment.txt"

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

try:
    data = open(filepath, 'r')

    print(f"Accessing Storage Vault: {filepath}")
    print("Connection established...\n")
    print(f"RECOVERED DATA:\n{data.read()}")

    data.close()

    print("\nData recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")

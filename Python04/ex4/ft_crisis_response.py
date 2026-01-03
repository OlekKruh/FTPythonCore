files_to_check = [
    "../data-generator-tools/lost_archive.txt",
    "../data-generator-tools/classified_vault.txt",
    "../data-generator-tools/standard_archive.txt"
]

print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

for filename in files_to_check:
    if filename == "../data-generator-tools/standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'")

    try:
        with open(filename, 'r') as archive:
            content = archive.read().strip()
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception as e:
        print(f"RESPONSE: Unexpected anomaly detected: {e}")
        print("STATUS: System calibration required\n")

print("All crisis scenarios handled successfully. Archives secure.")

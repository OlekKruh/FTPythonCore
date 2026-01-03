file_name = "../data-generator-tools/new_discovery.txt"

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

try:
    f = open(file_name, 'x')

    print(f"Initializing new storage unit: {file_name}")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    data = ("[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee\n")

    f.write(data)

    print(data)

    f.close()

    print("Data inscription complete. Storage unit sealed.\n"
          "Archive 'new_discovery.txt' ready for long-term preservation.")

except FileExistsError:
    print("ERROR: Storage unit already exists")

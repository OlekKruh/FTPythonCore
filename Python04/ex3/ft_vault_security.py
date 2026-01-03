class_data = "../data-generator-tools/classified_data.txt"
sec_protocol = "../data-generator-tools/security_protocols.txt"

print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

print("Initiating secure vault access...")
try:
    with open(class_data, 'r') as vault_read:
        print("Vault connection established with failsafe protocols\n")
        secret_data = vault_read.read()
        print("SECURE EXTRACTION:")
        print(secret_data)

    print("")
    print("SECURE PRESERVATION:")

    new_protocol = "[CLASSIFIED] New security protocols archived"
    sec_data = ("[CLASSIFIED] Archivist ID: ARCH_7742\n"
                "[CLASSIFIED] Status report: All systems nominal\n")
    with open(sec_protocol, 'a') as vault_write:
        vault_write.write("\n" + sec_data)

        print(new_protocol)

    print("\nVault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
except Exception as e:
    print(f"ERROR: A security breach occurred: {e}")

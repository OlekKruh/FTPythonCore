import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

# sys.stdout.write("Input Stream active. Enter archivist ID: ")
# sys.stdout.flush()
# archivist_id = sys.stdin.readline().strip()
#
# sys.stdout.write("Input Stream active. Enter status report: ")
# sys.stdout.flush()
# status_report = sys.stdin.readline().strip()

archivist_id = input("Input Stream active. Enter archivist ID: ")
status_report = input("Input Stream active. Enter status report: ")
print()

sys.stdout.write(f"[STANDARD] Archive status from {archivist_id}: {status_report}\n")
sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
sys.stdout.write("[STANDARD] Data transmission complete\n\n")

print("Three-channel communication test successful.")

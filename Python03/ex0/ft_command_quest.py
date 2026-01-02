import sys

print("=== Command Quest ===")

args_quantity = len(sys.argv)

if args_quantity <= 1:
    print("No arguments provided!")

print(f"Program name: {sys.argv[0]}")

if args_quantity > 1:
    print(f"Arguments received: {args_quantity - 1}")
    i = 1
    while i < args_quantity:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1

print(f"Total arguments: {args_quantity}")

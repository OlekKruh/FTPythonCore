import sys

print("=== Player Score Analytics ===")

args_quantity = len(sys.argv)

if args_quantity <= 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
elif args_quantity > 1:
    scores_list = []
    is_valid = True

    i = 1
    while i < args_quantity:
        arg = sys.argv[i]
        try:
            scores_list.append(int(arg))
        except ValueError:
            print(f"Argument #{i} '{arg}' not valid try decimal figure instead. Example: 1469, 4242")
            is_valid = False
        i += 1

    if is_valid:
        print(f"Scores processed: {scores_list}")
        print(f"Total players: {len(scores_list)}")
        print(f"Total score: {sum(scores_list)}")
        print(f"Average score: {sum(scores_list)/len(scores_list)}")
        print(f"High score: {max(scores_list)}")
        print(f"Low score: {min(scores_list)}")
        print(f"Score range: {max(scores_list) - min(scores_list)}")

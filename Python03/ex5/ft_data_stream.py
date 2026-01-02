import random
import time


def stream_events(n_events, stats):
    names = stats["players"]
    actions = stats["events"]

    for i in range(1, n_events + 1):
        current_player = random.choice(names)
        current_action = random.choices(actions, weights=[10, 20, 70], k=1)[0]

        stats["total_events"] += 1
        player_key = f"{current_player}_lvl"

        if current_action == "treasure_events":
            stats["treasure_events"] += 1
        elif current_action == "lvl_up_events":
            stats["lvl_up_events"] += 1
            stats[player_key] += 1
        elif current_action == "kill_mobs_events":
            stats["kill_mobs_events"] += 1

        current_lvl = stats[player_key]
        if current_lvl > stats["max_lvl"]:
            stats["max_lvl"] = current_lvl
            stats["max_lvl_player"] = current_player

        yield f"Event {i}: Player {current_player} (level {current_lvl}) {current_action}"


def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n):
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


# --- Основная логика ---
count = 0
n_events = 100
high_level_players = []
stats = {
        "players": ["Alice", "Bob", "Charlie"],
        "events": ["treasure_events", "lvl_up_events", "kill_mobs_events"],
        "Alice_lvl": 1,
        "Bob_lvl": 1,
        "Charlie_lvl": 1,
        "max_lvl": 1,
        "max_lvl_player": "alice",
        "total_events": 0,
        "treasure_events": 0,
        "lvl_up_events": 0,
        "kill_mobs_events": 0,
    }

print("=== Game Data Stream Processor ===")
print(f"Processing {n_events} game events...")

start_time = time.time()
event_stream = stream_events(n_events, stats)

for event in event_stream:
    count += 1
    if count <= 5:
        print(event)
    elif count == 6:
        print("...")
    elif count > n_events - 5:
        print(event)

for name in stats["players"]:
    lvl_key = f"{name}_lvl"
    lvl = stats[lvl_key]
    if lvl >= 10:
        high_level_players.append(f"{name} ({lvl})")
    if not high_level_players:
        high_level_players.append("None")

end_time = time.time()
duration = end_time - start_time

print("\n=== Stream Analytics ===")
print(f"Total events processed: {stats['total_events']}")
print(f"High-level players (10+): {', '.join(high_level_players)}")
print(f"Treasure events: {stats['treasure_events']}")
print(f"Level-up events: {stats['lvl_up_events']}")
print(f"Monster exterminates: {stats['kill_mobs_events']}")
print("Memory usage: Constant (streaming)")
print(f"Processing time: {duration:.4f} seconds")

print("\n=== Generator Demonstration ===")
fib_list = []
for num in fibonacci_generator(10):
    fib_list.append(str(num))
print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")

prime_list = []
for num in prime_generator(5):
    prime_list.append(str(num))
print(f"Prime numbers (first 5): {', '.join(prime_list)}")

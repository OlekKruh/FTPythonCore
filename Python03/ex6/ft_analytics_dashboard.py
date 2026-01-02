data = [
    {"user": "alice", "score": 2300,
     "region": "EU", "activities": True,
     "achievements": ["first_kill", "level_10", "boss_slayer"]},
    {"user": "bob", "score": 1800,
     "region": "US", "activities": True,
     "achievements": ["first_kill", "level_10"]},
    {"user": "charlie", "score": 2150,
     "region": "EU", "activities": True,
     "achievements": ["level_10", "boss_slayer", "speed_demon"]},
    {"user": "diana", "score": 2500,
     "region": "US", "activities": False,
     "achievements": ["first_kill", "speed_demon", "collector"]},
    {"user": "eve", "score": 1200,
     "region": "ASIA", "activities": False,
     "achievements": []}
]

print("=== Game Analytics Dashboard ===\n")
print("=== List Comprehension Examples ===")

high_score_platers = [p['user'] for p in data if p['score'] > 2000]
print(f"High scorers (>2000): {high_score_platers}")

score_dubled = [s['score']*2 for s in data]
print(f"Scores doubled: {score_dubled}")

activ_players = [a['user'] for a in data if a['activities'] is True]
print(f"Active players: {activ_players}")

print("")
print("=== Dict Comprehension Examples ===")

player_score = {p['user']: p['score'] for p in data}
print(f"Player scores: {player_score}")

ach_player = {a['user']: len(a['achievements']) for a in data}
print(f"Achievement counts: {ach_player}")

print("")
print("=== Set Comprehension Examples ===")
unique_regions = {p["region"] for p in data}
print(f"Active regions: {unique_regions}")

unique_achievements = {a for p in data for a in p["achievements"]}
print(f"Unique achievements: {unique_achievements}")

print("")
print("=== Combined Analysis ===")

print(f"Total players: {len(data)}")
print(f"Total unique achievements: {len(unique_achievements)}")

avg_score = sum(p["score"] for p in data) / len(data)
print(f"Average score: {avg_score}")

top_player = max(data, key=lambda p: p["score"])
print(f"Top performer: {top_player['user']} ({top_player['score']} points)")

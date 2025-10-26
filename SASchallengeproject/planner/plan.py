import random

# --- FOOD & DRINKS ---
food_drinks = [
    {"name": "Alston Bar & Beef", "type": "bar", "vibe": "classy", "activities": ["cocktails", "rooftop view"]},
    {"name": "Street Food Yard", "type": "food", "vibe": "chill", "activities": ["street eats", "games"]},
    {"name": "Slouch", "type": "pub", "vibe": "casual", "activities": ["beer", "pool"]},
    {"name": "Red Sky Bar", "type": "lounge", "vibe": "elegant", "activities": ["wine", "live jazz"]},
]

# --- ACTIVITIES ---
activities = [
    {"name": "Locked In Escape Room Glasgow", "type": "escape room", "vibe": "fun", "description": "Solve puzzles and break out together!"},
    {"name": "TeamSport Go Karting Glasgow Clydebank", "type": "go-karting", "vibe": "adventurous", "description": "Race your colleagues to the finish line "},
    {"name": "Laser Quest Glasgow", "type": "laser tag", "vibe": "energetic", "description": "Battle it out with laser blasters"},
    {"name": "Bowlarama", "type": "bowling", "vibe": "casual", "description": "Strike your way into the weekend"},
    {"name": "Pavilion Theatre", "type": "interactive show", "vibe": "classy", "description": "An Enchanting Play!"},
    {"name": "SuperCube", "type": "karaoke", "vibe": "fun", "description": "Sing your Hearts out!"},

]

# --- VIBE DETECTION ---
def get_vibe_from_prompt(prompt):
    """Detect vibe or mood from user input."""
    prompt = prompt.lower()
    if "fun" in prompt or "karaoke" in prompt or "party" in prompt:
        return "fun"
    elif "chill" in prompt or "relax" in prompt:
        return "chill"
    elif "adventure" in prompt or "race" in prompt or "kart" in prompt:
        return "adventurous"
    elif "classy" in prompt or "fancy" in prompt or "elegant" in prompt:
        return "classy"
    elif "casual" in prompt or "pub" in prompt or "beer" in prompt:
        return "casual"
    else:
        return random.choice(["fun", "chill", "casual"])

# --- PLAN GENERATION ---
def generate_plan(prompt):
    vibe = get_vibe_from_prompt(prompt)

    # Filter both lists based on vibe
    matched_food_drinks = [v for v in food_drinks if v["vibe"] == vibe] or food_drinks
    matched_activities = [a for a in activities if a["vibe"] == vibe] or activities


    # Pick one activity + one venue
    chosen_activity = random.choice(matched_activities)
    chosen_venue = random.choice(matched_food_drinks)

    plan = [
        {
            "time": "6:00 PM",
            "section": "Activity",
            "place": chosen_activity["name"],
            "description": chosen_activity["description"]
        },
        {
            "time": "8:00 PM",
            "section": "Food & Drinks",
            "place": chosen_venue["name"],
            "description": f"Enjoy {random.choice(chosen_venue['activities'])} at {chosen_venue['name']}."
        }
    ]

    return {
        "prompt": prompt,
        "vibe": vibe,
        "plan": plan,
        "notes": "Snout"
    }

# --- MAIN RUNNER ---
if __name__ == "__main__":
    user_prompt = input("Tell me about your nightout idea: ")
    result = generate_plan(user_prompt)

    print("\n Your Team Nightout Plan")
    print(f"Vibe: {result['vibe'].capitalize()}\n")
    for stop in result["plan"]:
        print(f"{stop['time']} — {stop['section']}: {stop['place']}")
        print(f"    {stop['description']}\n")
    print(result["notes"])

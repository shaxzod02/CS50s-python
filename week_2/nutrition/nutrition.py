calories={"apple":130,      "avocado california":50, "banana":110,
           "cantaloupe":50, "grapefruit": 60,        "grapes": 90,
          "honeydrew":50,   "kiwifriuit":90,         "lemon":15,
          "lime":20,        "noctarine":60,          "orange":80,
          "pear":100,        "pineapple":50,          "plums":70,
          "sweet cherries":100,  "tangerine":50,      "watermelon":80,
          "peach":60,}

item_user=input(f"Item: ").lower()
if item_user in calories:
    print(f"Calories: {calories[item_user]}")
else:
    print(f"")
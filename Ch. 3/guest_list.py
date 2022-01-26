# Abbi Kissee
# 01.25.22
# This program illustrates how to modify lists in various ways
invites = ['steve jobs', 'meryl streep', 'billie eilish']

# print(f"Hello {invites[0].title()}, It is my pleasure to invite you to a dinner at my residence. We will be having a cocktails, a meal, and some very thoughtful conversation.\n")

not_attending = invites.pop(0)
print(
    f"Unfortunately {not_attending.title()} cannot attend our dinner party.\n")

invites.insert(0, 'zendaya')
invites.insert(3, 'timothee chalamet')

print(f"Greetings {invites[1].title()}, I would like to formally invite you to a dinner party at my residence. We will be amoung inticing company and cocktails, dinner, and dessert will be provided. I do hope you will be able to join.\n")
print(f"Howdy {invites[2].title()}, I want to invite you to my place for a dinner party. We will be in the company of great minds with drinks, dinner, and desserts all on top of great conversation.\n")
print(f"Greetings {invites[0].title()}, It is my pleasure to invite you to my formal dinner party at my residence. It will be a night filled with laughter, good conversations, and mouthwatering food. I do hope you can join us.\n")
print(f"Hello {invites[3].title()}, I would like to formally invite you to a dinner party hosted at my residence. There will be cocktails, dinner, and desserts all alongside amazing company and conversations.\n")

num_attending = len(invites)
print(f"The guest list will include {num_attending} people.")

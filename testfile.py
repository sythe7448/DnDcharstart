import random

"""
@link http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
this function allows for you to weight the results of random.choice
"""


def weighted_choice(choices):
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"


for z in range(0,101):
    class_name = 'Monk'
    character_race = "Human"
    background_choices = [
        ('Acolyte',  50 if class_name in ['Cleric', 'Paladin'] else 0),  # From 5e Players Handbook
        ('Afflicted', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Antiquarian', 50 if class_name in ['Bard', 'Druid', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'] else 0),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Apothecary', 50 if class_name in ['Druid', 'Rogue', 'Wizard'] else 0), # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Battlemage', 50 if class_name in ['Bard', 'Sorcerer', 'Warlock', 'Wizard'] else 0),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Battlesmith', 50 if character_race in ['Mountain Dwarf', 'Hill Dwarf'] else 0), # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Bounty Hunter', 50 if class_name in ['Barbarian', 'Fighter', 'Rogue'] else 0),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Buckaroo', 50 if class_name in ['Barbarian', 'Druid', 'Ranger'] else 0),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Cavalryman', 50 if class_name in ['Paladin', 'Fighter'] else 0),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Charlatan', 50 if class_name in ['Bard', 'Rogue'] else 0),  # From 5e Players Handbook
        ('Clone', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Criminal', 50 if class_name in ['Rogue'] else 1),  # From 5e Players Handbook
        ('Cursed', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Dishonored Noble', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Doctor', 50 if class_name in ['Cleric', 'Druid', 'Paladin'] else 0), # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Entertainer', 50 if class_name in ['Bard'] else 1), # From 5e Players Handbook
        ('Executioner', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Exile', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Experiment', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Farmer', 10),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Feral Child', 50 if class_name in ['Barbarian', 'Druid', 'Ranger'] else 0),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Firefighter', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Folk Hero', 1),  # From 5e Players Handbook
        ('Gladiator', 50 if class_name in ['Barbarian', 'Fighter'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Guild Artisan', 1),  # From 5e Players Handbook
        ('Guild Merchant', 1),  # From 5e Players Handbook
        ('Gypsy', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Hellborn', 50 if character_race in ['Tiefling'] else 0), # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Hermit', 50 if class_name in ['Barbarian', 'Druid'] else 0),  # From 5e Players Handbook
        ('Inquirer', 50 if class_name in ['Bard', 'Paladin', 'Rogue'] else 0),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Monster Hunter', 50 if class_name in ['Barbarian', 'Ranger'] else 0),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Mystic',  50 if class_name in ['Monk', 'Cleric'] else 0),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Noble', 1),  # From 5e Players Handbook
        ('Outlander', 50 if class_name in ['Barbarian', 'Druid', 'Ranger'] else 1),  # From 5e Players Handbook
        ('Pirate', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Prospector', 50 if character_race in ['Mountain Dwarf', 'Hill Dwarf'] else 5),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Psychic', 50 if class_name in ['Bard', 'Monk'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Reaver', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Royalty', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Sage', 50 if class_name in ['Wizard'] else 0), # From 5e Players Handbook
        ('Sailor', 1),  # From 5e Players Handbook
        ('Scrounger', 1),   # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Slave', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Soldier', 50 if class_name in ['Fighter', 'Monk'] else 1),  # From 5e Players Handbook
        ('Spy', 50 if class_name in ['Bard', 'Rogue'] else 0),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Squire', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Student of Magic', 50 if class_name in ["Wizard"] else 0), # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Unknown', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
        ('Urchin', 1),  # From 5e Players Handbook
        ('Village Idiot', 2)  # From 5e Fan made backgrounds pdf

    ]

    print background_choices
    char_background = weighted_choice(background_choices)
    print char_background
    print 'Success' if char_background in ['Soldier', 'Mystic', 'Psychic'] else 'Failure'
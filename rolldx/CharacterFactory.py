import random
import Util
import pprint
from rolldx.Character import Character
import Factory

"""Base Character Class
"""
class CharacterFactory(object):

    generated_data = {}

    character = ''

    def __init__(self):
        self.create_dnd_character()
        self.character = Character(self.generated_data)

    def generate_base_stat_values(self):
        stat_names = [
            'Strength',
            'Dexterity',
            'Constitution',
            'Intelligence',
            'Wisdom',
            'Charisma'
        ]

        stat_values = {}
        for name in stat_names:
            math = []
            for i in [0] * 4:
                math.append(random.randrange(1, 7))
            math = sorted(math)
            stat_values[name] = sum(math[1:])

        #print stat_values
        self.generated_data['base_stat_values'] = stat_values
        return stat_values

    def generate_race(self):
        base_stat_values = self.generated_data['base_stat_values']
        race_values = [
            ("Hill Dwarf", (2 if base_stat_values['Constitution'] >= 15 else 0)+(1 if base_stat_values['Wisdom'] >= 13 else 0)),
            ("Mountain Dwarf", (2 if base_stat_values['Constitution'] >= 15 else 0)+(1 if base_stat_values['Strength'] >= 13 else 0)),
            ("High Elf", (2 if base_stat_values['Dexterity'] >= 15 else 0)+(1 if base_stat_values['Intelligence'] >= 13 else 0)),
            ("Wood Elf", (2 if base_stat_values['Dexterity'] >= 15 else 0)+(1 if base_stat_values['Wisdom'] >= 13 else 0)),
            ("Drow", (2 if base_stat_values['Dexterity'] >= 15 else 0)+(1 if base_stat_values['Charisma'] >= 13 else 0)),
            ("Lightfoot Halfling", (2 if base_stat_values['Dexterity'] >= 15 else 0)+(1 if base_stat_values['Charisma'] >= 13 else 0)),
            ("Stout Halfling", (2 if base_stat_values['Dexterity'] >= 15 else 0)+(1 if base_stat_values['Constitution'] >= 13 else 0)),
            ("Human", (2 if base_stat_values['Dexterity'] >= 14 or base_stat_values['Strength'] >= 14 or base_stat_values['Constitution'] >= 14 or base_stat_values['Wisdom'] >= 14 or base_stat_values['Intelligence'] >= 14 or base_stat_values['Charisma'] >= 14 else 0)),
            ("Variant Human", (2 if base_stat_values['Dexterity'] >= 14 or base_stat_values['Strength'] >= 14 or base_stat_values['Constitution'] >= 14 or base_stat_values['Wisdom'] >= 14 or base_stat_values['Intelligence'] >= 14 or base_stat_values['Charisma'] >= 14 else 0)),
            ("Dragonborn", (2 if base_stat_values['Strength'] >= 15 else 0)+(1 if base_stat_values['Charisma'] >= 13 else 0)),
            ("Forest Gnome", (2 if base_stat_values['Intelligence'] >= 15 else 0)+(1 if base_stat_values['Dexterity'] >= 13 else 0)),
            ("Rock Gnome", (2 if base_stat_values['Intelligence'] >= 15 else 0)+(1 if base_stat_values['Constitution'] >= 13 else 0)),
            ("Half-Elf", (2 if base_stat_values['Charisma'] >= 15 else 0)+(1 if base_stat_values['Dexterity'] >= 13 or base_stat_values['Strength'] >= 13 or base_stat_values['Constitution'] >= 13 or base_stat_values['Wisdom'] >= 13 or base_stat_values['Intelligence'] >= 13 or base_stat_values['Charisma'] >= 13 else 0)),
            ("Half-Orc", (2 if base_stat_values['Strength'] >= 15 else 0)+(1 if base_stat_values['Constitution'] >= 13 else 0)),
            ("Tiefling", (2 if base_stat_values['Charisma'] >= 15 else 0)+(1 if base_stat_values['Intelligence'] >= 13 else 0)),
            ("Aarakocra", (2 if base_stat_values['Dexterity'] >= 15 else 0)+(1 if base_stat_values['Wisdom'] >= 13 else 0)),
            ("Deep Gnome", (2 if base_stat_values['Intelligence'] >= 15 else 0)+(1 if base_stat_values['Dexterity'] >= 13 else 0)),
            ("Air Genasi", (2 if base_stat_values['Constitution'] >= 15 else 0)+(1 if base_stat_values['Dexterity'] >= 13 else 0)),
            ("Earth Genasi", (2 if base_stat_values['Constitution'] >= 15 else 0)+(1 if base_stat_values['Strength'] >= 13 else 0)),
            ("Fire Genasi", (2 if base_stat_values['Constitution'] >= 15 else 0)+(1 if base_stat_values['Intelligence'] >= 13 else 0)),
            ("Water Genasi", (2 if base_stat_values['Constitution'] >= 15 else 0)+(1 if base_stat_values['Wisdom'] >= 13 else 0)),
            ("Goliath", (2 if base_stat_values['Strength'] >= 15 else 0)+(1 if base_stat_values['Constitution'] >= 13 else 0))
        ]
        character_race = Util.weighted_choice(race_values)
        self.generated_data['character_race'] = character_race
        return character_race

    def generate_class_name(self):
        stat_values = self.generated_data['base_stat_values']
        class_names = [
            ("Barbarian", (2 if stat_values['Strength'] >= 15 else 0)+(1 if stat_values['Constitution'] >= 13 else 0)),
            ("Bard", (2 if stat_values['Charisma'] >= 15 else 0)+(1 if stat_values['Dexterity'] >= 13 else 0)),
            ("Cleric", (2 if stat_values['Wisdom'] >= 15 else 0)+(1 if stat_values['Charisma'] >= 13 else 0)),
            ("Druid", (2 if stat_values['Wisdom'] >= 15 else 0)+(1 if stat_values['Constitution'] >= 13 else 0)),
            ("Fighter", (2 if stat_values['Strength'] >= 15 else 0)+(1 if stat_values['Constitution'] >= 13 else 0)),
            ("Monk", (2 if stat_values['Dexterity'] >= 15 else 0)+(1 if stat_values['Wisdom'] >= 13 else 0)),
            ("Paladin",(2 if stat_values['Strength'] >= 15 else 0)+(1 if stat_values['Charisma'] >= 13 else 0)),
            ("Ranger", (2 if stat_values['Dexterity'] >= 15 else 0)+(1 if stat_values['Wisdom'] >= 13 else 0)),
            ("Rogue", (2 if stat_values['Dexterity'] >= 15 else 0)+(1 if stat_values['Charisma'] >= 13 else 0)),
            ("Sorcerer", (2 if stat_values['Charisma'] >= 15 else 0)+(1 if stat_values['Constitution'] >= 13 else 0)),
            ("Warlock", (2 if stat_values['Charisma'] >= 15 else 0)+(1 if stat_values['Charisma'] >= 13 else 0)),
            ("Wizard", (2 if stat_values['Intelligence'] >= 15 else 0)+(1 if stat_values['Constitution'] >= 13 else 0)),
            ("Commoner", 3)
        ]
        #print class_names
        class_name = Util.weighted_choice(class_names)
        self.generated_data['character_class'] = class_name
        return class_name

    def generate_race_stats(self):
        character_race = self.generated_data['character_race']
        race_stats = {
            'Strength':  (2 if character_race in ['Dragonborn', 'Half-Orc', 'Goliath', 'Mountain Dwarf'] else 0) + (1 if character_race in ['Human', 'Earth Genasi'] else 0 ),
            'Dexterity':  (2 if character_race in ['High Elf', 'Drow', 'Wood Elf',  'Lightfoot Halfling', 'Stout Halfling', 'Aarakocra'] else 0) + (1 if character_race in ['Human', 'Forest Gnome', 'Deep Gnome', 'Air Genasi'] else 0 ),
            'Constitution':  (2 if character_race in ['Hill Dwarf', 'Mountain Dwarf', 'Air Genasi', 'Earth Genasi', 'Fire Genasi', 'Water Genasi'] else 0) + (1 if character_race in ['Stout Halfling', 'Rock Gnome', 'Half-Orc', 'Goliath', 'Human'] else 0 ),
            'Intelligence': (2 if character_race in ['Forest Gnome', 'Rock Gnome', 'Deep Gnome'] else 0) + (1 if character_race in ['Human', 'High Elf', 'Tiefling', 'Fire Genasi'] else 0 ),
            'Wisdom': (2 if character_race in [] else 0) + (1 if character_race in ['Human', 'Hill Dwarf', 'Aarakocra', 'Fire Genasi', 'Wood Elf'] else 0 ),
            'Charisma': (2 if character_race in ['Half-Elf', 'Tiefling'] else 0) + (1 if character_race in ['Human', 'Drow', 'Lightfoot Halfling', 'Dragonborn'] else 0 ),
        }

        if character_race == 'Half-Elf':
            half_elf_race_stats = [
                'Strength',
                'Dexterity',
                'Constitution',
                'Intelligence',
                'Wisdom'
            ]
            for i in [0] * 2:

                pick = random.choice(half_elf_race_stats)
                race_stats[pick] += 1
                half_elf_race_stats.remove(pick)

        if character_race == 'Variant Human':
            Variant_Human_race_stats = [
                'Strength',
                'Dexterity',
                'Constitution',
                'Intelligence',
                'Wisdom',
                'Charisma'
            ]
            for i in [0] * 2:

                pick = random.choice(Variant_Human_race_stats)
                race_stats[pick] += 2
                Variant_Human_race_stats.remove(pick)


        #print race_stats
        self.generated_data['race_stats'] = race_stats
        return race_stats

    def generate_character_stats(self):
        base_stat_values = self.generated_data['base_stat_values']
        race_stats = self.generated_data['race_stats']
        character_stats = {
            'Strength': base_stat_values['Strength'] + race_stats['Strength'],
            'Dexterity': base_stat_values['Dexterity'] + race_stats['Dexterity'],
            'Constitution': base_stat_values['Constitution'] + race_stats['Constitution'],
            'Intelligence': base_stat_values['Intelligence'] + race_stats['Intelligence'],
            'Wisdom': base_stat_values['Wisdom'] + race_stats['Wisdom'],
            'Charisma': base_stat_values['Charisma'] + race_stats['Charisma'],
        }
        #print character_stats
        self.generated_data['character_stats'] = character_stats
        return character_stats

    def generate_race_modifier_stats(self):
        character_stat_values = self.generated_data['character_stats']
        race_stat_modifiers = {
            'Strength': ((character_stat_values['Strength'] - 10) / 2),
            'Dexterity': ((character_stat_values['Dexterity'] - 10) / 2),
            'Constitution': ((character_stat_values['Constitution'] - 10) / 2),
            'Intelligence': ((character_stat_values['Intelligence'] - 10) / 2),
            'Wisdom': ((character_stat_values['Wisdom'] - 10) / 2),
            'Charisma': ((character_stat_values['Charisma'] - 10) / 2),
        }
        self.generated_data['race_stat_modifiers'] = race_stat_modifiers
        return race_stat_modifiers

    def generate_char_skills_map(self):
        race_stat_modifiers = self.generated_data['race_stat_modifiers']
        #proficient = 2
        #expert = 4
        char_skills = {
            'Acrobatics': race_stat_modifiers['Dexterity'],
            'Animal Handling': race_stat_modifiers['Wisdom'],
            'Arcana': race_stat_modifiers['Intelligence'],
            'Athletics': race_stat_modifiers['Strength'],
            'Deception': race_stat_modifiers['Charisma'],
            'History': race_stat_modifiers['Intelligence'],
            'Insight': race_stat_modifiers['Wisdom'],
            'Intimidation': race_stat_modifiers['Charisma'],
            'Investigation': race_stat_modifiers['Intelligence'],
            'Medicine': race_stat_modifiers['Wisdom'],
            'Nature': race_stat_modifiers['Intelligence'],
            'Perception': race_stat_modifiers['Wisdom'],
            'Performance': race_stat_modifiers['Charisma'],
            'Persuasion': race_stat_modifiers['Charisma'],
            'Religion': race_stat_modifiers['Intelligence'],
            'Sleight of Hand': race_stat_modifiers['Dexterity'],
            'Stealth': race_stat_modifiers['Dexterity'],
            'Survival': race_stat_modifiers['Wisdom'],
        }
        self.generated_data['char_skills'] = char_skills
        return char_skills

    def generate_char_height(self):
        char_height_modifier = {
            "Hill Dwarf": (random.randrange(1, 5))+(random.randrange(1, 5)),
            "Mountain Dwarf": (random.randrange(1, 5)),
            "High Elf": (random.randrange(1, 11))+(random.randrange(1, 11)),
            "Wood Elf": (random.randrange(1, 11))+(random.randrange(1, 11)),
            "Drow": (random.randrange(1, 7))+(random.randrange(1, 7)),
            "Lightfoot Halfling": (random.randrange(1, 5))+(random.randrange(1, 5)),
            "Stout Halfling": (random.randrange(1, 5))+(random.randrange(1, 5)),
            "Human": (random.randrange(1, 11))+(random.randrange(1, 11)),
            "Variant Human": (random.randrange(1, 11))+(random.randrange(1, 11)),
            "Dragonborn": (random.randrange(1, 9))+(random.randrange(1, 9)),
            "Forest Gnome": (random.randrange(1, 5))+(random.randrange(1, 5)),
            "Rock Gnome": (random.randrange(1, 5))+(random.randrange(1, 5)),
            "Half-Elf": (random.randrange(1, 9))+(random.randrange(1, 9)),
            "Half-Orc": (random.randrange(1, 11))+(random.randrange(1, 11)),
            "Tiefling": (random.randrange(1, 9))+(random.randrange(1, 9)),
            "Aarakocra": (random.randrange(1, 7))+(random.randrange(1, 7)),
            "Deep Gnome": (random.randrange(1, 5))+(random.randrange(1, 5)),
            "Air Genasi": (random.randrange(1, 9))+(random.randrange(1, 9)),
            "Earth Genasi": (random.randrange(1, 9))+(random.randrange(1, 9)),
            "Fire Genasi": (random.randrange(1, 9))+(random.randrange(1, 9)),
            "Water Genasi": (random.randrange(1, 9))+(random.randrange(1, 9)),
            "Goliath": (random.randrange(1, 11))+(random.randrange(1, 11))
        }
        self.generated_data['char_height_modifier'] = char_height_modifier

        char_height = {
            "Hill Dwarf": (((44 + char_height_modifier["Hill Dwarf"])/12), ((44 + char_height_modifier["Hill Dwarf"])%12)),
            "Mountain Dwarf": (((48 + char_height_modifier["Mountain Dwarf"])/12), ((48 + char_height_modifier["Mountain Dwarf"])%12)),
            "High Elf": (((54 + char_height_modifier["High Elf"])/12), ((54 + char_height_modifier["High Elf"])%12)),
            "Wood Elf":(((54 + char_height_modifier["Wood Elf"])/12), ((54 + char_height_modifier["Wood Elf"])%12)),
            "Drow": (((53 + char_height_modifier["Drow"])/12), ((53 + char_height_modifier["Drow"])%12)),
            "Lightfoot Halfling": (((31 + char_height_modifier["Lightfoot Halfling"])/12), ((31 + char_height_modifier["Lightfoot Halfling"])%12)),
            "Stout Halfling": (((31 + char_height_modifier["Stout Halfling"])/12), ((31 + char_height_modifier["Stout Halfling"])%12)),
            "Human":  (((56 + char_height_modifier["Human"])/12), ((56 + char_height_modifier["Human"])%12)),\
            "Variant Human":  (((56 + char_height_modifier["Human"])/12), ((56 + char_height_modifier["Human"])%12)),
            "Dragonborn":(((66 + char_height_modifier["Dragonborn"])/12), ((66 + char_height_modifier["Dragonborn"])%12)),
            "Forest Gnome": (((35 + char_height_modifier["Forest Gnome"])/12), ((35 + char_height_modifier["Forest Gnome"])%12)),
            "Rock Gnome": (((35 + char_height_modifier["Rock Gnome"])/12), ((35 + char_height_modifier["Rock Gnome"])%12)),
            "Half-Elf": (((57 + char_height_modifier["Half-Elf"])/12), ((57 + char_height_modifier["Half-Elf"])%12)),
            "Half-Orc": (((58 + char_height_modifier["Half-Orc"])/12), ((58 + char_height_modifier["Half-Orc"])%12)),
            "Tiefling": (((57 + char_height_modifier["Tiefling"])/12), ((57 + char_height_modifier["Tiefling"])%12)),
            "Aarakocra": (((50 + char_height_modifier["Aarakocra"])/12), ((50 + char_height_modifier["Aarakocra"])%12)),
            "Deep Gnome": (((35 + char_height_modifier["Deep Gnome"])/12), ((35 + char_height_modifier["Deep Gnome"])%12)),
            "Air Genasi": (((60 + char_height_modifier["Air Genasi"])/12), ((60 + char_height_modifier["Air Genasi"])%12)),
            "Earth Genasi": (((60 + char_height_modifier["Earth Genasi"])/12), ((60 + char_height_modifier["Earth Genasi"])%12)),
            "Fire Genasi": (((60 + char_height_modifier["Fire Genasi"])/12), ((60 + char_height_modifier["Fire Genasi"])%12)),
            "Water Genasi": (((60 + char_height_modifier["Water Genasi"])/12), ((60 + char_height_modifier["Water Genasi"])%12)),
            "Goliath": (((80 + char_height_modifier["Goliath"])/12), ((80 + char_height_modifier["Goliath"])%12)),
        }
        self.generated_data['char_height'] = char_height[self.generated_data['character_race']]
        return char_height

    def generate_char_weight(self):
        char_height_modifier = self.generated_data['char_height_modifier']
        char_weight_modifier = {
            "Hill Dwarf": (random.randrange(1, 7))+(random.randrange(1, 7)),
            "Mountain Dwarf": (random.randrange(1, 7))+(random.randrange(1, 7)),
            "High Elf": (random.randrange(1, 5)),
            "Wood Elf": (random.randrange(1, 5)),
            "Drow": (random.randrange(1, 7)),
            "Lightfoot Halfling": 1,
            "Stout Halfling": 1,
            "Human": (random.randrange(1, 5)),
            "Variant Human": (random.randrange(1, 5)),
            "Dragonborn": (random.randrange(1, 7))+(random.randrange(1, 7)),
            "Forest Gnome": 1,
            "Rock Gnome": 1,
            "Half-Elf": (random.randrange(1, 5))+(random.randrange(1, 5)),
            "Half-Orc": (random.randrange(1, 7))+(random.randrange(1, 7)),
            "Tiefling": (random.randrange(1, 5))+(random.randrange(1, 5)),
            "Aarakocra": (random.randrange(1, 5))+(random.randrange(1, 5)),
            "Deep Gnome": (random.randrange(1, 7)),
            "Air Genasi": (random.randrange(1, 5)),
            "Earth Genasi": (random.randrange(1, 5)),
            "Fire Genasi": (random.randrange(1, 5)),
            "Water Genasi": (random.randrange(1, 5)),
            "Goliath": (random.randrange(1, 7))
        }
        self.generated_data['char_weight_modifier'] = char_weight_modifier

        char_weight = {
            "Hill Dwarf": 115 + (char_height_modifier["Hill Dwarf"] * char_weight_modifier["Hill Dwarf"]),
            "Mountain Dwarf": 130 + (char_height_modifier["Mountain Dwarf"] * char_weight_modifier["Mountain Dwarf"]),
            "High Elf": 90 + (char_height_modifier["High Elf"] * char_weight_modifier["High Elf"]),
            "Wood Elf": 100 + (char_height_modifier["Wood Elf"] * char_weight_modifier["Wood Elf"]),
            "Drow": 75 + (char_height_modifier["Drow"] * char_weight_modifier["Drow"]),
            "Lightfoot Halfling": 35 + (char_height_modifier["Lightfoot Halfling"] * char_weight_modifier["Lightfoot Halfling"]),
            "Stout Halfling": 35 + (char_height_modifier["Stout Halfling"] * char_weight_modifier["Stout Halfling"]),
            "Human": 110 + (char_height_modifier["Human"] * char_weight_modifier["Human"]),
            "Variant Human": 110 + (char_height_modifier["Variant Human"] * char_weight_modifier["Variant Human"]),
            "Dragonborn": 175 + (char_height_modifier["Dragonborn"] * char_weight_modifier["Dragonborn"]),
            "Forest Gnome": 35 + (char_height_modifier["Forest Gnome"] * char_weight_modifier["Forest Gnome"]),
            "Rock Gnome": 35 + (char_height_modifier["Rock Gnome"] * char_weight_modifier["Rock Gnome"]),
            "Half-Elf": 110 + (char_height_modifier["Half-Elf"] * char_weight_modifier["Half-Elf"]),
            "Half-Orc": 140 + (char_height_modifier["Half-Orc"] * char_weight_modifier["Half-Orc"]),
            "Tiefling": 110 + (char_height_modifier["Tiefling"] * char_weight_modifier["Tiefling"]),
            "Aarakocra": 75 + (char_height_modifier["Aarakocra"] * char_weight_modifier["Aarakocra"]),
            "Deep Gnome": 75 + (char_height_modifier["Deep Gnome"] * char_weight_modifier["Deep Gnome"]),
            "Air Genasi": 120 + (char_height_modifier["Air Genasi"] * char_weight_modifier["Air Genasi"]),
            "Earth Genasi": 120 + (char_height_modifier["Earth Genasi"] * char_weight_modifier["Earth Genasi"]),
            "Fire Genasi":  120 + (char_height_modifier["Fire Genasi"] * char_weight_modifier["Fire Genasi"]),
            "Water Genasi":  120 + (char_height_modifier["Water Genasi"] * char_weight_modifier["Water Genasi"]),
            "Goliath": 280 + (char_height_modifier["Goliath"] * char_weight_modifier["Goliath"]),
        }
        self.generated_data['char_weight'] = char_weight[self.generated_data['character_race']]
        return char_weight

    def generate_background(self):
        class_name = self.generated_data['character_class']
        character_race = self.generated_data['character_race']
        background_choices = [
            ('Acolyte', 50 if class_name in ['Cleric', 'Paladin'] else 1),  # From 5e Players Handbook
            ('Afflicted', 10 if class_name in ['Commoner'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Antiquarian', 50 if class_name in ['Bard', 'Druid', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Apothecary', 50 if class_name in ['Druid', 'Rogue', 'Wizard'] else 1), # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Battlemage', 50 if class_name in ['Bard', 'Sorcerer', 'Warlock', 'Wizard'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Battlesmith', 50 if character_race in ['Mountain Dwarf', 'Hill Dwarf'] else 1), # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Bounty Hunter', 50 if class_name in ['Barbarian', 'Fighter', 'Rogue'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Buckaroo', 50 if class_name in ['Barbarian', 'Druid', 'Ranger'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Cavalryman', 50 if class_name in ['Paladin', 'Fighter'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Charlatan', 50 if class_name in ['Bard', 'Rogue'] else 1),  # From 5e Players Handbook
            ('Clone', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Criminal', 50 if class_name in ['Rogue'] else 1),  # From 5e Players Handbook
            ('Cursed', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Dishonored Noble', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Doctor', 50 if class_name in ['Cleric', 'Druid', 'Paladin'] else 1), # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Entertainer', 50 if class_name in ['Bard'] else 1), # From 5e Players Handbook
            ('Executioner', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Exile', 25 if class_name in ['Barbarian', 'Druid', 'Commoner'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Experiment', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Farmer', 25 if class_name in ['Commoner'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Feral Child', 50 if class_name in ['Barbarian', 'Druid', 'Ranger'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Firefighter', 10 if class_name in ['Commoner'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Folk Hero', 1),  # From 5e Players Handbook
            ('Gladiator', 50 if class_name in ['Barbarian', 'Fighter'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Guild Artisan', 25 if class_name in ['Commoner'] else 1),  # From 5e Players Handbook
            ('Guild Merchant', 25 if class_name in ['Commoner'] else 1),  # From 5e Players Handbook
            ('Gypsy', 25 if class_name in ['Commoner'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Hellborn', 50 if character_race in ['Tiefling'] else 0), # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Hermit', 50 if class_name in ['Barbarian', 'Druid'] else 1),  # From 5e Players Handbook
            ('Inquirer', 50 if class_name in ['Bard', 'Paladin', 'Rogue'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Monster Hunter', 50 if class_name in ['Barbarian', 'Ranger'] else 1), # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Mystic', 50 if class_name in ['Monk', 'Cleric'] else 1), # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Noble', 1),  # From 5e Players Handbook
            ('Outlander', 50 if class_name in ['Barbarian', 'Druid', 'Ranger'] else 1),  # From 5e Players Handbook
            ('Pirate', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Prospector', 50 if character_race in ['Mountain Dwarf', 'Hill Dwarf'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Psychic', 50 if class_name in ['Bard', 'Monk', 'Sorcerer'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Reaver', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Royalty', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Sage', 50 if class_name in ['Wizard'] else 1), # From 5e Players Handbook
            ('Sailor', 1),  # From 5e Players Handbook
            ('Scrounger', 25 if class_name in ['Commoner'] else 1),   # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Slave', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Soldier', 50 if class_name in ['Fighter', 'Monk'] else 1),  # From 5e Players Handbook
            ('Spy', 50 if class_name in ['Bard', 'Rogue'] else 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Squire', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Student of Magic', 50 if class_name in ["Wizard"] else 1), # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Unknown', 1),  # from https://www.dandwiki.com/wiki/5e_Backgrounds
            ('Urchin', 25 if class_name in ['Rogue', 'Commoner'] else 1),  # From 5e Players Handbook
            ('Village Idiot', 2)  # From 5e Fan made backgrounds pdf

        ]

        #print background_choices
        char_background = Util.weighted_choice(background_choices)
        self.generated_data['background'] = char_background
        return char_background

    def create_dnd_character(self):

        # Generate all properties
        base_stat_values = self.generate_base_stat_values()
        character_race = self.generate_race()
        race_stats = self.generate_race_stats()
        character_class = self.generate_class_name()
        character_stats = self.generate_character_stats()
        race_modifier_stats = self.generate_race_modifier_stats()
        char_skills = self.generate_char_skills_map()
        char_height = self.generate_char_height()
        char_weight = self.generate_char_weight()
        background = self.generate_background()

        char = {
                "Race": character_race,
                "Base Stats": base_stat_values,
                "Character Stats": character_stats,
                "Class": character_class,
                "Stats": race_stats,
                "Stat Modifiers": race_modifier_stats,
                "Skills": char_skills,
                "Height": char_height[character_race],
                "Weight": char_weight[character_race],
                "Background": background
        }

        return char


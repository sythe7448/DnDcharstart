import pprint


"""Base Character Class
"""
class Character(object):

    name = ''

    height = ''
    stats = ''
    skills = ''
    weight = ''
    profession = ''
    race = ''
    race_stats = ''
    stat_modifiers = ''
    base_stats = ''
    background = ''


    def __init__(self, settings):

        prop_map = {
            'char_name': 'name',
            'char_height': 'height',
            'char_skills': 'skills',
            'char_weight': 'weight',
            'character_class': 'profession',
            'character_race': 'race',
            'character_stats': 'stats',
            'race_stat_modifiers': 'stat modifiers',
            'race_stats': 'race stats',
            'base_stat_values': 'base stats',
            'background': 'background'
        }

        for n in settings:
            try:
                tried = prop_map[n]
            except:
                continue
            prop_name = prop_map[n]
            setattr(self, prop_name, settings[n])

    def props(self):
        return [i for i in self.__dict__.keys() if i[:1] != '_']

    def __repr__(self):
        pp = pprint.PrettyPrinter(indent=4)
        out = ""
        lol = self.props()
        for p in lol:
            out += p + ": " + pp.pformat(getattr(self, p)) + "\n"

        return "Character ({0})".format(out)

# Game world simulation engine

# {verb}  e.g. stand
# {verb} {prep}  e.g. stand up, lie down, go out
# {verb} {object}  e.g. open door, eat chocolate
# {verb} {object} {prep}  e.g. lie on bed, climb up ladder
# {verb} {object1} {prep} {object2}  e.g. put kettle on stove, talk to stranger, go into

import yaml
from yaml import Loader
from word_utils import cap_first_letter, sentence_syntax

# Import custom game functions
from actions import action_funcs, action_synonyms

# Load world data
data_filename = "world_data.yaml"
with open(data_filename, 'r') as f:
    data = yaml.load(f, Loader=Loader)

player = "player1"
sentences = []

agents = data['agents']
if player in agents:
    location = agents[player]['location']
    words = [
        agents[player]['name'],
        agents[player]['verbs']["to be"],
        agents[player]['position'],
        data['locations'][location]['description']
    ]
    sentences.append(sentence_syntax(' '.join(words)))

objects = data['objects']
for object in objects:
    if objects[object]['location'] == location:
        words = [
            "there",
            objects[object]['verbs']["to be"],
            objects[object]['description']
        ]  
        sentences.append(sentence_syntax(' '.join(words)))

print(' '.join(sentences))

user_input = input("> ")
user_words = user_input.split()
location_actions = data['locations'][location]['actions']

for action in location_actions:
    synonyms = [action] + action_synonyms.get(action, [])
    synonym_words = [s.split() for s in synonyms]
    # Sort by number of words to ensure greedy match
    synonym_words = sorted(synonym_words, key=lambda words: len(words), reverse=True)
    for action_words in synonym_words:
        n = len(action_words)
        if user_words[:n] == action_words:
            message = action_funcs[action_words](data,)

pass
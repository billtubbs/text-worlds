# Test the Parser class

from parser import Parser

language = {
    #'Det': []'the', 'a', 'an'],
    'N': ['bed', 'door', 'key', 'handle', 'box', 'window'],
    'V': ['sit', 'open', 'close', 'unlock', 'go'],
    'P': ['on', 'in', 'with', 'to'],
    'J': ['small', 'big', 'wooden', 'heavy', 'open', 'closed', 'round']
}

p = Parser(language)

sentence = "sit on bed"
for tree in p.parse_sentence(sentence):
    print(tree)


player = {
    'name': "you",
    'type': "human",
    'location': "in the living room",
    'position': ("standing", "on", "floor")
}

commands = {
    {'V': 'sit', 'P': 'on'}: 'sit on obj',
    {'V': 'stand', 'P': 'on'}: 'stand on obj',
    {'V': 'lie', 'P': 'on'}: 'lie on obj',
    {'V': 'stand', 'P': 'up'}: 'stand up'
}

actions = {
    'sit on obj': {
        'results': [
            ('change_position', {'new': 'sitting on'})
        ]
    },
    'stand on obj': {
        'results': [
            ('change_position', {'new': 'standing on'})
        ]
    },
    'lie on obj': {
        'results': [
            ('change_position', {'new': 'lying on'})
        ]
    },
    'stand up': {
        'results': [
            ('change_position', {'new': 'standing'})
        ]
    }
}

object_behaviours = {
    'chair': {
        'actions': {
            'human': ['sit on', 'stand on', 'pick up', 'put down']
            }
        },
    'bed': {
        'actions': {
            'human': ['sit on', 'stand on', 'lie on']
            }
    }
}

objects = {
    'the couch': {
        'behaviours': ['chair'],
        'location': "in the living room",
        'position': "on the floor",
    }
}


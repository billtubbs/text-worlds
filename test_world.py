# Test world classes and functions

from itertools import chain
from world import Object, Agent


def loc_obs_func(loc):
    sentences = [
        loc.description,
        'You see ' + ', '.join(obj.name for obj in loc.objects if obj.observable) + '.'
    ]
    return '. '.join(sentences)


def obj_obs_func(obj):
    return ' '.join([obj.name, 'is', obj.position])


def human_obs_world_func(agent):
    print('You are in ' + agent.location.name, end='.\n')
    print(agent.location.observe())


def human_decision_func(agent):
    text = input('> ')
    return text.strip()


name = "the living room"
properties = {
    'description': "It is bright and there is a nice view to the north",
    'objects': []
}
loc1 = Object(name, loc_obs_func, properties)
assert loc1.name == name
assert loc1.description == properties['description']
assert loc1.objects == properties['objects']
assert loc1.obs_func == loc_obs_func

name = "the couch"
properties = {
    'location': loc1,
    'position': 'on the floor',
    'observable': True
}
obj1 = Object(name, obj_obs_func, properties)
assert obj1.name == name
assert obj1.location == properties['location']
assert obj1.position == properties['position']
assert obj1.observable == properties['observable']
assert obj1.observe() == "the couch is on the floor"

loc1.objects.append(obj1)

assert loc1.observe() == "It is bright and there is a nice view to the north. You see the couch."


name = "Player 1"
properties = {
    'location': loc1,
    'position': 'standing',
    'observable': True
}
ag1 = Agent(name, obj_obs_func, human_obs_world_func, 
            human_decision_func, properties)
assert ag1.name == name
assert ag1.location == properties['location']
assert ag1.position == properties['position']
assert ag1.observable == properties['observable']
assert ag1.observe() == "Player 1 is standing"

ag1.observe_world()
action = ag1.decide_action()

breakpoint()
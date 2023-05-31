# Custom action functions
#
# All functions should have the same signature:
#
#  - my_action(data, agent, object)
#

def stand(data, agent, object=None):
    agent_data = data['agents'][agent]
    if agent_data['position'] == "sitting":
        agent_data['position'] == "standing"
        return "you are now standing"
    elif agent_data['position'] == "standing":
        return "you are already standing"
    else:
        return False


def sit(data, agent, object=None):
    agent_data = data['agents'][agent]
    if agent_data['position'] == "standing":
        agent_data['position'] == "sitting"
        message = "you are now sitting"
        if object is not None:
            message = message + " on " + object
    elif agent_data['position'] == "sitting":
        message = "you are already sitting"
        if object is not None:
            message = message + " on " + object
    else:
        return False


def lie(data, agent, object=None):
    agent_data = data['agents'][agent]
    if agent_data['position'] == "standing":
        agent_data['position'] == "lying"
        message = "you are now lying"
        if object is not None:
            message = message + " on " + object
    elif agent_data['position'] == "lying":
        message = "you are already lying"
        if object is not None:
            message = message + " on " + object
    else:
        return False


def go(data, agent, destination):
    agent_data = data['agents'][agent]
    locations = data['locations']
    assert destination in locations
    agent_data['location'] == destination
    return None


# Link all action functions to action words and synonyms
action_funcs = {
    'stand': stand,
    'sit': sit,
    'lie': lie
}

# Provide any synonyms (optional)
action_synonyms = {
    'stand': ['stand up', 'get up', 'stand on'],
    'sit': ['sit down', 'sit on'],
    'lie': ['lie down', 'lie on']
}
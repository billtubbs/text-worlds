class World():

    def __init__(self, name, config=None):

        self.name = name


class Object():

    def __init__(self, name, obs_func, properties=None):

        self.name = name
        self.obs_func = obs_func
        if properties is not None:
            for k, v in properties.items():
                setattr(self, k, v)

    def observe(self):
        return self.obs_func(self)


class Agent(Object):

    def __init__(self, name, obs_func, obs_world_func, 
                 decision_func, properties=None):

        super().__init__(name, obs_func, properties=properties)
        self.obs_world_func = obs_world_func
        self.decision_func = decision_func

    def observe_world(self):
        return self.obs_world_func(self)

    def decide_action(self):
        return self.decision_func(self)

class World2D:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.agents = []
        self.objects = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_agent(self, agent):
        self.agents.remove(agent)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def get_agents(self):
        return self.agents

    def get_objects(self):
        return self.objects

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
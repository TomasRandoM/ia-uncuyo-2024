from environment import *
from reflexiveAgent import *
from randomAgent import *
import copy

if __name__ == "__main__":
    environment = Environment(10, 10, 0.3)
    environment.printEnvironment()
    environment1 = copy.deepcopy(environment)
    agent1 = ReflexiveAgent(environment)
    agent2 = RandomAgent(environment1)

    print(agent1.think())
    print(agent2.think())
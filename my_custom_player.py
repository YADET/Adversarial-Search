from sample_players import DataPlayer
import random, math, copy

# i have get some idea of writing mcts from followings sites:
# https://int8.io/monte-carlo-tree-search-beginners-guide/
# https://github.com/lfiaschi/udacity-aind-isolation



class CustomPlayer(DataPlayer):

    def get_action(self, state):
        if state.ply_count < 2:
            self.queue.put(random.choice(state.actions()))
        else:
            self.queue.put(self.montcarlo(state))

    def montcarlo(self, state):
        rootnode = Node(state)
        epoch = 10
        while epoch >=0:
            epoch-=1
            if rootnode.state.terminal_test():
                return random.choice(state.actions())
            child = selection(rootnode)
            reward = simulation(child.state)
            backpropagation(child, reward)
        indx = rootnode.childs.index(bestchilds(rootnode))
        acts= rootnode.childs_action[indx]
        return acts


def selection(node):
    while not node.state.terminal_test():
        if not len(node.childs_action) == len(node.state.actions()):
            return expand(node)
        node = bestchilds(node)
    return node


def simulation(state):
    initials = copy.deepcopy(state)
    while not state.terminal_test():
        action = random.choice(state.actions())
        state = state.result(action)
    if state._has_liberties(initials.player()):
        reward=-1
    else:
        reward=1
    return reward


def backpropagation(node, reward):
    while node != None:
        node.reward += reward
        node.visit += 1
        node = node.parent
        reward *= -1


class Node():
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.visit = 1
        self.reward = 0
        self.childs = []
        self.childs_action = []


    def addchild(self, state, action):
        child = Node(state, self)
        self.childs.append(child)
        self.childs_action.append(action)


def expand(node):
    for action in node.state.actions():
        if action not in node.childs_action:
            not_tried_state = node.state.result(action)
            node.addchild(not_tried_state, action)
            node_chids=node.childs[-1]
            #print(node_chids)
            return node_chids


def bestchilds(node):

    best_childs_list = []
    highest_score = float("-inf")
    for child in node.childs:
        score = child.reward / child.visit + 1 * (math.sqrt(2.0 * math.log(node.visit) / child.visit))
        if score > highest_score:
            best_childs_list=[child]
            highest_score=score 
        elif score == highest_score:
            best_childs_list.append(child)
    
    random_best_child = random.choice(best_childs_list)
    return random_best_child


CustomPlayer = CustomPlayer

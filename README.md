
# Build Monte Carlo Tree search for an Adversarial Game Playing Agent

This is my assginment solution for Udacity AI fundamental course.

Adversarial search techniques for building an agent to play knights Isolation.  

### Isolation

In the game Isolation, two players each control their own single token and alternate taking turns moving the token from one cell to another on a rectangular grid.  

Finally, agents have a fixed time limit (150 milliseconds by default) to search for the best move and respond.  The search will be automatically cut off after the time limit expires, and the active agent will forfeit the game if it has not chosen a move.


## Instructions

Agent is implemented in the `CustomPlayer` class defined in the `game_agent.py` file. The interface definition for game agents only requires `.get_action()` method, but you can add any other methods to the class that you deem necessary. You can build a basic agent by combining minimax search with alpha-beta pruning and iterative deepening But i implemented MCTS.


#### The get_action() Method
This function is called once per turn for each player. The calling function handles the time limit and 
```
def get_action(self, state):
    import random
    self.queue.put(random.choice(state.actions()))
```

- **DO NOT** use multithreading/multiprocessing (the isolation library already uses them, so using them in your agent may cause conflicts)


#### Saving Information Between Turns
The `CustomPlayer` class can pass internal state by assigning the data to the attribute `self.context`. An instance of your agent class will carry the context between each turn of a single game, but the contents will be reset at the start of any new game.
```
def get_action(...):
    action = self.mcts()
    self.queue.put(action)
    self.context = object_you_want_to_save  # self.context will contain this object on the next turn
```

#### Default oponent is MINMAX but you can select based available other openents as mentioned in run_match.py

TEST_AGENTS = {
    "RANDOM": Agent(RandomPlayer, "Random Agent"),
    "GREEDY": Agent(GreedyPlayer, "Greedy Agent"),
    "MINIMAX": Agent(MinimaxPlayer, "Minimax Agent"),
    "SELF": Agent(CustomPlayer, "Custom TestAgent")
}

example of command to run:

```
$ python run_match.py -o RANDOM
```

other parameters which can be setted are: NUM_PROCS, NUM_ROUNDS = 10, TIME_LIMIT = 100 , number on epochs.


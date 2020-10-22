# THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
# SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. Simon Marty

# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
#
# Modified by Eugene Agichtein for CS325 Sp 2014 (eugene@mathcs.emory.edu)
#

import random
import sys

import util
from game import Agent
from game import Directions
from util import manhattanDistance

players = {
    'PACMAN': 0,
    'FIRST_GHOST': 1
}


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        Note that the successor game state includes updates such as available food,
        e.g., would *not* include the food eaten at the successor state's pacman position
        as that food is no longer remaining.
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        currentFood = currentGameState.getFood()  # food available from current state
        newFood = successorGameState.getFood()  # food available from successor state (excludes food@successor)
        currentCapsules = currentGameState.getCapsules()  # power pellets/capsules available from current state
        newCapsules = successorGameState.getCapsules()  # capsules available from successor (excludes capsules@successor)
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        "*** YOUR CODE HERE ***"
        """
        This evaluation function uses
        - The distance between pacman and the ghost (maximize that)
        - The score (maximize that)
        - Whether the food count will decrease (maximize that)
        - Distance to closest food (minimize that)
        - The weights are a bit arbitrary, I just adjusted them until Pacman seemed to perform
        """

        dist_to_closest_food = min([manhattanDistance(newPos, food) for food in newFood.asList()] + [sys.maxsize]) + 1

        val = 0.1 * manhattanDistance(newPos, newGhostStates[0].getPosition())
        val += 1000 * successorGameState.getScore()
        val += abs(currentFood.count() - newFood.count())
        val += 1000 * 1 / dist_to_closest_food
        return val


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        """
        Modeled partly after the notes, I used some trickery to deduce the current agent
        id from the depth. It's not the prettiest thing but so far I haven't found a
        much better solution that expands the right amount of states.
        """

        def val_function(game_state, depth):

            if game_state.isWin() or game_state.isLose() or depth == self.depth * game_state.getNumAgents():
                return self.evaluationFunction(game_state)

            current_agent = depth % game_state.getNumAgents()

            if current_agent == players['PACMAN']:
                # We are pacman
                return max_function(game_state, current_agent, depth)
            else:
                # We are ghost
                return min_function(game_state, current_agent, depth)

        def max_function(game_state, agent, depth):
            """
            First, generate all values for each legal action for the given agent
            Then get max
            """
            return max([val_function(game_state.generateSuccessor(agent, act), depth + 1) for act in
                        game_state.getLegalActions(agent)])

        def min_function(game_state, agent, depth):
            """
            Similar approach as to the max_function(), except here we reduce with the min() function
            """
            return min([val_function(game_state.generateSuccessor(agent, act), depth + 1) for act in
                        game_state.getLegalActions(agent)])

        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        # I love one liners. If you have any advice on making this even less readable please let me know :
        new_score, action_to_take = max(
            [(val_function(gameState.generateSuccessor(players['PACMAN'], action), players['FIRST_GHOST']), action) for
             action in
             gameState.getLegalActions(players['PACMAN'])] + [(-sys.maxint, Directions.STOP)])

        return action_to_take


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        def val_function(game_state, alpha, beta, depth):
            if game_state.isWin() or game_state.isLose() or depth == self.depth * game_state.getNumAgents():
                return self.evaluationFunction(game_state)
            current_player = depth % game_state.getNumAgents()
            if current_player == players['PACMAN']:
                return max_function(game_state, current_player, alpha, beta, depth)
            else:
                return min_function(game_state, current_player, alpha, beta, depth)
            pass

        def max_function(game_state, agent, alpha, beta, depth):
            res = -sys.maxint
            for action in game_state.getLegalActions(agent):
                res = max(res, val_function(game_state.generateSuccessor(agent, action), alpha, beta, depth + 1))
                if res > beta:
                    return res
                alpha = max(res, alpha)
            return res

        def min_function(game_state, agent, alpha, beta, depth):
            res = sys.maxint
            for action in game_state.getLegalActions(agent):
                res = min(res, val_function(game_state.generateSuccessor(agent, action), alpha, beta, depth + 1))
                if res < alpha:
                    return res
                beta = min(beta, res)
            return res

        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        action_to_take = Directions.STOP
        score = -sys.maxint
        alpha = -sys.maxint
        beta = sys.maxint

        for action in gameState.getLegalActions(players['PACMAN']):
            new_score = val_function(gameState.generateSuccessor(players['PACMAN'], action), alpha, beta,
                                     players['FIRST_GHOST'])
            if new_score > score:
                score = new_score
                action_to_take = action
            if score > beta:
                return action_to_take
            alpha = max(alpha, score)
        return action_to_take


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        import sys

        def expected_value(game_state, agent, depth):
            if depth == 0 or game_state.isWin() or game_state.isLose():
                return self.evaluationFunction(game_state)
            actions = game_state.getLegalActions(agent)
            val = 0
            for action in actions:
                if agent == game_state.getNumAgents() - 1:
                    val += max_function(game_state.generateSuccessor(agent, action), depth - 1)
                else:
                    # Move on to the next ghost
                    val += expected_value(game_state.generateSuccessor(agent, action), agent + 1, depth)

            return val / len(actions)

        def max_function(game_state, depth):
            if depth == 0 or game_state.isWin() or game_state.isLose():
                return self.evaluationFunction(game_state)
            score = -sys.maxint
            for action in game_state.getLegalActions(0):
                score = max(score, expected_value(game_state.generateSuccessor(0, action), 1, depth))
            return score

        new_score, action_to_take = max([(expected_value(gameState.generateSuccessor(players['PACMAN'], action),
                                                         players['FIRST_GHOST'], self.depth), action) for action in
                                         gameState.getLegalActions(players['PACMAN'])] + [
                                            (-sys.maxint, Directions.STOP)])

        return action_to_take


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: Pacman attempts to minimize distance to
      closest food, all foods
      Pacman attempts to maximize the change in food count from one state to the next and score
      If the ghosts are scared, pacman attempts to get closer to them.
      If they are not, pacman attempts to get as far away from them as possible

    """
    "*** YOUR CODE HERE ***"
    import sys

    # If ghosts are scared, add their distance to the eval function, remove dist from ghost from heuristic
    values = {}

    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    food_distances = [manhattanDistance(newPos, food) for food in newFood.asList()]
    ghost_distances = [manhattanDistance(newPos, i.getPosition()) for i in newGhostStates]

    total_food_distance = sum(food_distances)
    dist_to_closest_food = min(food_distances + [sys.maxsize])

    dist_to_closest_ghost = min(ghost_distances)
    total_ghost_distance = sum(ghost_distances)
    scared = sum(newScaredTimes)

    val = currentGameState.getScore() ** 3
    val += 1000 * 1 / (dist_to_closest_food + 1)
    val += 1 / (total_food_distance + 1)

    if not scared:
        val += dist_to_closest_ghost
        val += total_ghost_distance
    else:
        val += 1 / (1 + dist_to_closest_ghost)
        val += 1 / (1 + total_ghost_distance)

    return val


# Abbreviation
better = betterEvaluationFunction


class ContestAgent(MultiAgentSearchAgent):
    """
      Your agent for the mini-contest
    """

    def getAction(self, gameState):
        """
          Returns an action.  You can use any method you want and search to any depth you want.
          Just remember that the mini-contest is timed, so you have to trade off speed and computation.

          Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
          just make a beeline straight towards Pacman (or away from him if they're scared!)
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

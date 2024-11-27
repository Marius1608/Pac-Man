# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from turtledemo.penrose import start

import util
from game import Directions
from typing import List

class SearchProblem:

    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
        state: Search stat
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
        state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
        actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:

    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    #completat
    from util import Stack

    stack = Stack()
    visited = set()
    start_state = problem.getStartState()
    initial_path = []

    stack.push((start_state, initial_path))

    while not stack.isEmpty():

        current_state, current_path = stack.pop()
        if problem.isGoalState(current_state):
            return current_path

        if current_state not in visited:
            visited.add(current_state)
            successors = problem.getSuccessors(current_state)
            for successor, action, _ in successors:
                if successor not in visited:
                    new_path = current_path + [action]
                    stack.push((successor, new_path))
    return []

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:

    """Search the shallowest nodes in the search tree first."""
    #completat

    from util import Queue
    queue = Queue()
    visited = set()
    start_state = problem.getStartState()
    initial_path = []

    queue.push((start_state, initial_path))

    while not queue.isEmpty():

        current_state, current_path = queue.pop()
        if problem.isGoalState(current_state):
            return current_path

        if current_state not in visited:
            visited.add(current_state)
            successors = problem.getSuccessors(current_state)
            for successor, action, _ in successors:
                if successor not in visited:
                    new_path = current_path + [action]
                    queue.push((successor, new_path))
    return []

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:

    """Search the node of least total cost first."""

    #completat
    from util import PriorityQueue
    queue = PriorityQueue()
    visited = set()
    start_state = problem.getStartState()
    initial_path = []
    initial_cost = 0

    queue.push((start_state, initial_path), initial_cost)

    while not queue.isEmpty():

        current_state, current_path = queue.pop()
        if problem.isGoalState(current_state):
            return current_path

        if current_state not in visited:
            visited.add(current_state)
            successors = problem.getSuccessors(current_state)
            for successor, action, step_cost in successors:
                if successor not in visited:
                    new_path = current_path + [action]
                    new_cost = problem.getCostOfActions(new_path)
                    queue.push((successor, new_path), new_cost)
    return []

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:

    """Search the node that has the lowest combined cost and heuristic first."""

    from util import PriorityQueue
    #completat
    start_state = problem.getStartState()
    frontier = PriorityQueue()
    frontier.push((start_state, [], 0), 0)
    explored = {}

    while not frontier.isEmpty():
        state, actions, cost_so_far = frontier.pop()

        if state in explored and cost_so_far >= explored[state]:
            continue

        explored[state] = cost_so_far

        if problem.isGoalState(state):
            return actions

        for successor, action, step_cost in problem.getSuccessors(state):
            new_cost = cost_so_far + step_cost
            if successor not in explored or new_cost < explored[successor]:
                new_actions = actions + [action]
                priority = new_cost + heuristic(successor, problem)
                frontier.push((successor, new_actions, new_cost), priority)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

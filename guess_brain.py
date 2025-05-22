import pandas
from turtle import Turtle

FONT = ("Arial", 8, "normal")

class GuessBrain:
    def __init__(self):
        self.data = pandas.read_csv("50_states.csv") # Returns a pandas dataframe object.
        self.states = self.data["state"].to_list() # Turns the state column into a list.
        self.state_count = 0 # The amount of states the user has guessed.
        self.guessed_states = [] # The name of the states the user has guessed.

    def get_coordinates(self, state):
        """Gets the coordinates of a given state."""
        state_data = self.data[self.data["state"] == state] # Gets the row data of the state the user has guessed.
        x_cor, y_cor = state_data.iloc[0][["x", "y"]] # Gets the x and y coordinate of the state.
        coordinates = (int(x_cor), int(y_cor)) # Converts the coordinates into a tuple.
        return coordinates

    def write_state(self, state):
        """Writes the state name on the map."""
        coordinates = self.get_coordinates(state) # Gets the coordinates from the get_coordinates function.
        turtle = Turtle() # Creates a turtle
        turtle.penup() # Disabled turtle drawing.
        turtle.ht() # Hides the turtle body.
        turtle.goto(coordinates) # Sends the turtle to the state coordinates.
        turtle.write(f"{state}", align="center", font=FONT) # Writes the state name.

    def check_answer(self, answer):
        """Checks the user answer against the list of states."""
        # Checks if the user guess is in the states list and not in the already guessed states list.
        if answer in self.states and answer not in self.guessed_states:
            self.state_count += 1 # Increments the user guess count.
            self.guessed_states.append(answer) # Adds the name of the state to the guessed states list.
            return True # Returns true if a new state is guessed correctly.
        return False # Returns false if the state is guessed incorrectly or if a state has already been guessed.

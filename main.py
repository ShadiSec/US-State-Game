from turtle import Screen, Turtle
from guess_brain import GuessBrain

screen = Screen()
turtle = Turtle()
guess_brain = GuessBrain()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_on = True
while game_on:
    # Creates a text box pop-up.
    user_answer = screen.textinput(title=f"Guess The State {guess_brain.state_count}/50", prompt="Name a state:").title()

    # Stops the loop if user guesses all 50 states.
    if guess_brain.state_count == 50:
        game_on = False
    # Checks if the user guessed correctly.
    elif guess_brain.check_answer(user_answer):
        guess_brain.write_state(user_answer)
    # Checks if the user has already guessed the state.
    elif user_answer in guess_brain.guessed_states:
        print("You've already guessed that.")
    # If the user is wrong.
    else:
        print("That's not quite right.")

screen.exitonclick()


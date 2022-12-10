# Making the US States game
import turtle

import pandas

from answers import Answer

# Initialize screen and images
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Guess the state functions
data = pandas.read_csv("./50_states.csv")

# Number of states
all_states = data.state.to_list()
num_of_states = len(all_states)

correct_guesses = []
end_game = False
while not end_game:
    answer_state = screen.textinput(
        title=f"{len(correct_guesses)}/{num_of_states} States Correct",
        prompt="What's another state's name? ",
    ).title()
    if answer_state == "Exit":
        break
    state_details = data[data.state == answer_state]
    if not state_details.empty:
        answer = Answer(int(state_details.x), int(state_details.y), answer_state)

        correct_guesses.append(answer_state)

    if len(correct_guesses) >= num_of_states:
        end_game = True


# states_to_learn.csv
states_to_learn = {"state": []}
states_to_learn["state"] = [
    state for state in all_states if state not in correct_guesses
]

df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")

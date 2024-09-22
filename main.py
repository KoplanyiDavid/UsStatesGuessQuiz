import turtle, pandas as pd

correct_guesses = 0
game_is_on = True
input_screen_title = ""

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./UsStatesQuiz/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("./UsStatesQuiz/50_states.csv")
states = data.state.to_list()

while(game_is_on):
    if correct_guesses > 0:
        input_screen_title = f"{correct_guesses}/50 States Correct"
    else:
        input_screen_title = "Guess the State"

    answer_state = screen.textinput(title=input_screen_title, prompt="What's a state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states:
        correct_guesses += 1
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

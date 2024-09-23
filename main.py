import turtle, pandas as pd

guessed_states = []
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
    if len(guessed_states) > 0:
        input_screen_title = f"{len(guessed_states)}/50 States Correct"
    else:
        input_screen_title = "Guess the State"

    answer_state = screen.textinput(title=input_screen_title, prompt="What's a state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("./UsStatesQuiz/states_to_learn.csv")
        break
    
    if answer_state in states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

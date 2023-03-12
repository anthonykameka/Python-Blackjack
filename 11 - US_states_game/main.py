import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game") #title of window

image = "blank_states_img.gif" # used as background

screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state_name = data["state"]
state_list = state_name.to_list()
guessed_states = []

score = len(guessed_states) # better than using increasing int, as i can check answer
playing = True

while playing:
    answer_state = screen.textinput(title=f"{score}/50 states guessed correctly", prompt="Guess a state's name. (exit to quit)").title()
    if answer_state == "Exit": ## user can type Exit to leave. states not guessed will update in CSV file
        missing_states = [state for state in state_list not in guessed_states]
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("missed_states.csv")
        print(missing_data)

        break
    if answer_state in state_list and answer_state not in guessed_states:

        row = data[data.state == answer_state]
        print(row)
        guessed_states.append(row.state.item())
        text = turtle.Turtle()
        text.hideturtle()
        text.up()
        # print(row)
        text.goto(int(row.x), int(row.y))
        text.write(row.state.item())
        score += 1

        if score == 50:
            playing = False





"""function to get state coordinates"""
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()








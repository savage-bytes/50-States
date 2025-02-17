import turtle
import pandas

screen = turtle.Screen()
screen.title("50 States of Umerica")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def mouse_click_cor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(mouse_click_cor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_states = turtle.textinput(title=f"{len(guessed_states)}Guess the State", prompt="Name any States? : ").title()

    if answer_states == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        print(missing_states)
        break

    if answer_states in all_states:
        guessed_states.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_states]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_states)

# new_dict = {new_item: new_key for item in list}
# new_dict = {new_item: new_key for (key, value) in dict.items() if test}
# this is the dict form for compression
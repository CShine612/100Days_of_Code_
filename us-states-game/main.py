import turtle
import pandas

FONT = ("Courier", 10, "normal")

states_data = pandas.read_csv("50_states.csv")


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.tracer(0)
image = "blank_states_img.gif"
screen.addshape(image)
map = turtle.Turtle()
map.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")


screen.update()

correct_guesses = []

while len(correct_guesses) < 50:

    answer_state = screen.textinput(f"Guess the state. {len(correct_guesses)}/50", "Whats another State name?").title().strip()

    if answer_state == "Exit":
        missed_states = {"state": [state for state in list(states_data.state) if state not in correct_guesses]}
        missing_states = pandas.DataFrame(missed_states)
        missing_states.to_csv("missing_states.csv")

        break
    if answer_state in list(states_data.state) and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        state = states_data[states_data.state == answer_state]
        writer.setposition((int(state.x), int(state.y)))
        writer.write(str(answer_state), move=False, align="center", font=FONT)
        screen.update()


turtle.mainloop()
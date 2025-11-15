from nicegui import ui
from random import shuffle

EMOJIS = ['🍟', '🍉', '🥯', '😵', '😵‍💫', '😂', '👋', '💸'] * 2
shuffle(EMOJIS)

buttons = []
opened = []
matched = []

def reset_pair(i, j):
    buttons[i].set_text("❓")
    buttons[j].set_text("❓")
    opened.clear()

def handle_click(idx):
    if idx in matched or idx in opened:
        return
    
    opened.append(idx)
    buttons[idx].set_text(EMOJIS[idx])   
    if len(opened) == 2:
        if EMOJIS[opened[0]] == EMOJIS[opened[1]]:
            matched.append(opened[0])
            matched.append(opened[1])
            opened.clear()
        else:
            ui.timer(0.5, lambda: reset_pair(opened[0], opened[1]), once=True)
    if len(matched) == 16:
        ui.notify("You win!")

def restart_game():
    shuffle(EMOJIS)
    matched.clear()
    opened.clear()
    for i in range(16):
        buttons[i].set_text("❓")

with ui.grid(columns = 4):
    for i in range(16):
        button = ui.button("❓", on_click=lambda _, idx = i: handle_click(idx)).style("font-size: 30px").classes("h-30 w-30") 
        buttons.append(button)

restartButton = ui.button("Restart?", on_click=restart_game)
ui.run(title='Memory Game')
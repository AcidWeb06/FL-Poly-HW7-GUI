from nicegui import ui

#TwistHash Algorithm 
def twistHash():
    textString = inputBox.value.strip()
    h = 0x9E3779B1
    for char in textString:
        h = h ^ ord(char)
        h = h * 0x517CC1C7
        h = h & 0xFFFFFFFF
    h = h ^ len(textString)
    hashValue.text = f"Hash Value: {h}"

with ui.column().classes("w-full"):   
    with ui.card().classes("h-65 w-200 self-auto"):
        ui.label("Hashing").style("color: green; font-size: 40px")
        inputBox = ui.input()
        hashValue = ui.label("Hash value: ").classes("font-mono text-lg")
        ui.button("Get Hash", on_click=twistHash, color="blue")

ui.run()
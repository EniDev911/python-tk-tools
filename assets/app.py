from guizero import App, Text, PushButton, Slider, Picture, ButtonGroup

app = App(title="My application")
app.bg = "Yellow"

message = Text(app, text="Hello World", color="darkorange")
message.size = 60
#message.color = "darkorange"

def mostrar():
	logo.visible = True


mostrar = PushButton(app, text="mostrar", command=mostrar)
mostrar.bg = "red"
mostrar.text_size = 40

volumen = Slider(app, start=10, end=500)
volumen.text_size = 25

logo = Picture(app)
logo.value = "onda.gif"
logo.visible = False
logo.resize(300, 320)


choice = ButtonGroup(app, options=['Python', 'Java', 'C++'], selected='Python')
choice.text_size = 20
choice.align = 'top'


app.display()
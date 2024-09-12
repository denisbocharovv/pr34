from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

colors = {
    '#ff0000': 'Красный',
    '#ff8800': 'Оранжевый',
    '#ffff00': 'Желтый',
    '#00ff00': 'Зеленый',
    '#00ffff': 'Голубой',
    '#0000ff': 'Синий',
    '#ff00ff': 'Фиолетовый'
}

class Raduga(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        text_input = TextInput()
        label = Label()

        for color_code, color_name in colors.items():
            button = Button(text=color_name, background_color=[int(color_code[i:i+2], 16)/255 for i in (1, 3, 5)])
            button.bind(on_press=lambda btn, code=color_code, name=color_name: self.on_button_press(code, name, text_input, label))
            layout.add_widget(button)

        layout.add_widget(text_input)
        layout.add_widget(label)
        return layout

    def on_button_press(self, code, name, text_input, label):
        text_input.text = code
        label.text = name

if __name__ == '__main__':
    Raduga().run()
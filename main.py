from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
import random

class DecisionMakerApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10, padding=10)

        # Add a logo image
        logo_image = Image(source='logo.jpg')
        layout.add_widget(logo_image)

        
        # Add a text input
        self.text_input = TextInput(hint_text="Enter options (separated with commas)", size_hint_y=None, height=30)
        layout.add_widget(self.text_input)
        
        # Create a button
        button = Button(text="Choose", size_hint_y=None, height=40)
        button.bind(on_press=self.choose_random_option)
        layout.add_widget(button)
        
        # Add a label for output
        self.output_label = Label(text="", font_size=18)
        layout.add_widget(self.output_label)
        
        return layout

    def choose_random_option(self, instance):
        user_input = self.text_input.text
        options = user_input.split(",")

        # Clean up extra spaces
        cleaned_options = []
        for option in options:
            cleaned_option = option.strip()
            cleaned_options.append(cleaned_option)

        # Print the output
        if cleaned_options:
            chosen_option = random.choice(cleaned_options)
            self.output_label.text = "Go with : "+chosen_option
        else:
            self.output_label.text = "No options provided. Please enter some options."

if __name__ == "__main__":
    DecisionMakerApp().run()



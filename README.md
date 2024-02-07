# Decision_Maker
The Decision Maker App is a simple utility app designed to help users make decisions by randomly selecting an option from a list. Users can input their options (separated by commas), and the app will choose one of those options randomly.

Let's break down the code step by step:
- Importing Necessary Modules:
    - We start by importing the required modules from Kivy and Python.
    - App from kivy.app is the base class for creating Kivy applications.
    - GridLayout from kivy.uix.gridlayout allows us to organize widgets.
    - TextInput from kivy.uix.textinput provides a text input field.
    - Button from kivy.uix.button creates a clickable button.
    - Label from kivy.uix.label creates a output label.
    - Image from kivy.uix.image adds image to the layout.
    - We also import the random module for selecting a random option.
- Creating the App Class:
    - We define our custom app class called DecisionMakerApp, which inherits from App.
    - Inside this class, we'll define the app's behavior and UI.
- Building the UI:
    - In the build method, we create the UI components.
    - We use a GridLayout as the root layout.
    - We create a TextInput widget where users can enter options (separated by commas).
    - We create a button with the label "Choose Random Option."
- Binding the Button Action:
    - We bind the button to the choose_random_option method.
    - When the button is pressed, the choose_random_option method will be called.
- The choose_random_option Method:
    - This method is triggered when the button is pressed.
    - It retrieves the user input from the text input field (self.text_input.text).
    - The input is split into individual options using the comma as the separator (options = user_input.split(",")).
    - We clean up extra spaces around each option using a for loop.
    - If there are cleaned options, we randomly select one and print it.
    - If no options are provided, we print a message indicating that the user should enter some options.
- Running the App:
    - The if __name__ == "__main__": block ensures that the app runs when the script is executed directly (not imported as module).
    - We create an instance of DecisionMakerApp and call its run() method to start the app.

# Output

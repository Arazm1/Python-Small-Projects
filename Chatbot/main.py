class Inputs:
    def __init__(self):
        """Initialize sets of recognized words."""
        self.greetings = {"hello", "hi", "sup"}
        self.farewells = {"bye", "goodbye", "byebye"}

class Responder:
    def __init__(self, inputs):
        self.inputs = inputs

    def respond(self):
        user_input = input("Type something: ").lower()

        if user_input in self.inputs.greetings:
            print("Hello User! 😊")
        elif user_input in self.inputs.farewells:
            print("Goodbye! 👋")
        else:
            print("I don't understand that. 🤔")


inputs = Inputs()
responder = Responder(inputs)

responder.respond()

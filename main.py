class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate food. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} slept. Energy: {self.energy}")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play.")
            return
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played. Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")

    def get_status(self):
        print(f"🐾 {self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

def main():
    print("Welcome to the Pet Simulator!")
    pet_name = input("What is your pet's name? ")
    my_pet = Pet(pet_name)
    print("You can now interact with your pet.")
    print("Commands: eat, sleep, play, train, show_tricks, get_status")
    print("Type 'exit' to quit the simulator.\n")

    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "eat":
            my_pet.eat()
        elif command == "sleep":
            my_pet.sleep()
        elif command == "play":
            my_pet.play()
        elif command == "train":
            trick = input("Enter the trick to train: ").strip()
            my_pet.train(trick)
        elif command == "show_tricks":
            my_pet.show_tricks()
        elif command == "get_status":
            my_pet.get_status()
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()

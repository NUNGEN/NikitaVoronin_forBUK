class Level:
    def __init__(self, name, initial_resources, min_resources=8):
        self.name = name
        self.resources = initial_resources
        self.min_resources = min_resources
        self.alive = True  # Можно оставить, но он не меняется здесь

    def receive_resources(self, amount):
        self.resources += amount
        print(f"{self.name} received {amount} resources. Total: {self.resources}")

    def act(self, next_level):
        if not self.alive:
            return

        print(f"{self.name} -- Resources: {self.resources}")
        print("Choose action:")
        print("1: Keep all")
        print("2: Share half (10% waste)")
        print("3: Send all (10% waste)")
        
        choice = input("Your choice (1, 2, 3): ")

        if choice == "1":
            print(f"{self.name} keeps all resources.")
        elif choice == "2":
            share = self.resources // 2
            self.resources -= share
            lost = int(share * 0.1)
            transfer_amount = share - lost
            print(f"{self.name} shares half. Lost: {lost}. Sent: {transfer_amount}")
            if next_level:
                next_level.receive_resources(transfer_amount)
        elif choice == "3":
            lost = int(self.resources * 0.1)
            transfer_amount = self.resources - lost
            print(f"{self.name} sends all. Lost: {lost}. Sent: {transfer_amount}")
            self.resources = 0
            if next_level:
                next_level.receive_resources(transfer_amount)
        else:
            print("Invalid input. No action taken.")

class Game:
    def __init__(self, num_levels=5, initial_resources=100):
        self.levels = [
            Level(f"Level {i + 1}", initial_resources if i == 0 else 0)
            for i in range(num_levels)
        ]

    def play_one_round(self):
        print("Game started")
        for i in range(len(self.levels)):
            current_level = self.levels[i]
            next_level = self.levels[i + 1] if i + 1 < len(self.levels) else None
            current_level.act(next_level)

            if next_level and next_level.resources < next_level.min_resources:
                print(f"Game over: Next level {next_level.name} has not enough resources.")
                break
            
if __name__ == "__main__":
    game = Game()
    game.play_one_round()
        

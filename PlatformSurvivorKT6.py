class Level:
    def __init__(self, number, resources):
        self.number = number
        self.resources = resources
        self.alive = True

    def receive(self, amount):
        self.resources += amount

    def check(self, min_resources):
        if self.resources < min_resources:
            self.alive = False

    def status(self):
        state = "в игре" if self.alive else "вышел"
        print(f"Уровень {self.number}: {self.resources} ресурсов ({state})")


class Game:
    def __init__(self, levels_count=10, fixed_loss=5, min_resources=10):
        self.levels = []
        self.fixed_loss = fixed_loss
        self.min_resources = min_resources
        self.total_resources = 100 * levels_count  # Общий пул ресурсов
        for i in range(levels_count):
            self.levels.append(Level(i + 1, 100))

    def play_turn(self):
        for i in range(len(self.levels)):
            level = self.levels[i]
            if not level.alive:
                continue

            print(f"\nУровень {level.number}")
            print(f"Текущие ресурсы: {level.resources}")
            print(f"Всего ресурсов в системе: {self.total_resources}")

            try:
                keep = int(input("Сколько оставить себе? "))
                pass_down = int(input("Сколько передать вниз? (будет потеряно 5 единиц) "))
                share = int(input("Сколько поделиться с другими? "))
            except ValueError:
                print("Ошибка ввода. Пропуск хода.")
                continue

            total = keep + pass_down + share
            if total > level.resources:
                print("Ошибка: вы тратите больше, чем у вас есть! Пропуск хода.")
                continue

            # 1. Сохраняем оставленное себе
            level.resources = keep
            self.total_resources -= (pass_down + share)  # Уменьшаем общий пул

            # 2. Передаём вниз с фиксированными потерями
            if pass_down > 0 and i + 1 < len(self.levels):
                lost = min(self.fixed_loss, pass_down)
                sent_amount = pass_down - lost
                self.levels[i + 1].receive(sent_amount)
                print(f"Передано вниз: {sent_amount} (потеряно {lost})")

            # 3. Делимся с другими с учётом остатка
            if share > 0:
                others = [j for j in range(len(self.levels)) if j != i and self.levels[j].alive]
                if others:
                    per_level = share // len(others)
                    remainder = share % len(others)  # Остаток - дополнительные потери
                    
                    for j in others:
                        self.levels[j].receive(per_level)
                    
                    print(f"Поделено с другими: {per_level} на уровень (потеряно {remainder})")
                    self.total_resources -= remainder  # Учитываем остаток как потерю

            # 4. Проверка выживания
            level.check(self.min_resources)

    def show_status(self):
        print("\n--- Состояние всех уровней ---")
        for level in self.levels:
            level.status()
        print(f"Общее количество ресурсов: {self.total_resources}")

    def is_game_over(self):
        alive = [level for level in self.levels if level.alive]
        return len(alive) == 0

    def run(self):
        turn = 1
        while not self.is_game_over():
            print(f"\n========== ХОД {turn} ==========")
            self.play_turn()
            self.show_status()
            turn += 1
            if self.total_resources <= 0:
                print("\n⚠ Ресурсы в системе закончились!")
                break
        print("\n🎮 Игра окончена. Все уровни выбыли.")


if __name__ == "__main__":
    game = Game()
    game.run()
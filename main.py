import json
import os
import sys


class Portfolio:
    def __init__(self, data_path="data.json"):
        """Инициализация портфолио и загрузка данных из JSON."""
        self.data_path = data_path
        self.data = self._load_data()

    def _load_data(self):
        """Внутренний метод для безопасного чтения файла."""
        try:
            with open(self.data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Ошибка: Файл {self.data_path} не найден!")
            sys.exit(1)
        except json.JSONDecodeError:
            print("❌ Ошибка: Неверный формат JSON-файла!")
            sys.exit(1)

    def _print_header(self, title):
        """Бонус: Красивое оформление заголовков секций."""
        print("\n" + "=" * 50)
        print(f"🌟 {title.upper()} 🌟")
        print("=" * 50)

    def show_about(self):
        info = self.data["about"]
        self._print_header(info["title"])
        print(f"👤 Имя:       {info['name']}")
        print(f"🎂 Возраст:   {info['age']} лет")
        print(f"💼 Занятие:   {info['occupation']}")
        print("\n📝 Факты обо мне:")
        for fact in info["facts"]:
            print(f"  • {fact}")

    def show_goal(self):
        info = self.data["goal"]
        self._print_header(info["title"])
        print(info["text"])

    def show_history(self):
        info = self.data["history"]
        self._print_header(info["title"])
        print(info["text"])

    def show_mentor(self):
        info = self.data["mentor"]
        self._print_header(info["title"])
        print(info["text"])

    def show_progress(self):
        info = self.data["progress"]
        self._print_header(info["title"])
        print(info["text"])

    def show_hobbies(self):
        info = self.data["hobbies"]
        self._print_header(info["title"])
        print(info["text"])

    def show_projects(self):
        info = self.data["projects"]
        self._print_header(info["title"])
        for i, item in enumerate(info["items"], 1):
            print(f"\n📂 Проект №{i}: {item['name']}")
            print(f"📝 Описание: {item['desc']}")
            print(f"🔗 Ссылка:   {item['link']}")

    def show_github(self):
        info = self.data["github"]
        self._print_header(info["title"])
        print(f"📂 Репозиторий проекта: {info['url']}")

    def display_menu(self):
        """Вывод главного меню программы."""
        print("\n" + "—" * 50)
        print("Главное меню портфолио Ергазина Рахата:")
        print("—" * 50)
        print(f"1. {self.data['about']['title']}")
        print(f"2. {self.data['goal']['title']}")
        print(f"3. {self.data['history']['title']}")
        print(f"4. {self.data['mentor']['title']}")
        print(f"5. {self.data['progress']['title']}")
        print(f"6. {self.data['hobbies']['title']}")
        print(f"7. {self.data['projects']['title']}")
        print(f"8. {self.data['github']['title']}")
        print("0. Выход из программы")
        print("—" * 50)


def main():
    # Создаем объект класса Portfolio
    portfolio = Portfolio("data.json")

    # Карта соответствия выбора пользователя и методов класса
    menu_actions = {
        "1": portfolio.show_about,
        "2": portfolio.show_goal,
        "3": portfolio.show_history,
        "4": portfolio.show_mentor,
        "5": portfolio.show_progress,
        "6": portfolio.show_hobbies,
        "7": portfolio.show_projects,
        "8": portfolio.show_github
    }

    while True:
        portfolio.display_menu()
        choice = input("Выберите пункт меню (0-8): ").strip()

        if choice == "0":
            print("\n👋 Спасибо за просмотр! До встречи в Middle-разработке!")
            break
        elif choice in menu_actions:
            # Вызываем нужный метод
            menu_actions[choice]()
            input("\nНажмите Enter, чтобы вернуться в меню...")
            # Очистка консоли для аккуратности (работает на Windows и Mac/Linux)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("\n⚠️ Неверный ввод! Пожалуйста, введите цифру от 0 до 8.")


if __name__ == "__main__":
    main()
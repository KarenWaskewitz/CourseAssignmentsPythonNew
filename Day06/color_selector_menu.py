# color_selector_menu.py

def display_menu(colors):
    print("Select a color by entering the corresponding number:\n")
    for index, color in enumerate(colors, start=1):
        print(f"{index}. {color}")

def get_user_choice(colors):
    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(colors):
                return colors[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(colors)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    colors = ["blue", "green", "yellow", "white"]
    display_menu(colors)
    selected_color = get_user_choice(colors)
    print(f"\nYou selected: {selected_color}")

class MenuItem:
    def __init__(self, display_name: str, function_to_call: str) -> None:
        self.display_name = display_name
        self.function_to_call = function_to_call

    def __str__(self) -> str:
        return "aaa"

class TextMenu:
    def __init__(self) -> None:
        self.menu_items: dict = {}

    def __str__(self) -> str:
        return f"{self.menu_items}"

    def add_menu_item(self, menu_item: MenuItem) -> None:
        self.menu_items[menu_item.display_name] = menu_item
        pass

    def remove_menu_item(self) -> None:
        pass

    def get_user_input(self) -> None:
        pass

main_menu = TextMenu()
main_menu.add_menu_item(MenuItem("test", "testing"))

print(main_menu)
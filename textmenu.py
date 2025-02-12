class MenuItem:
    def __init__(self, display_name: str, function_to_call: str, index: int) -> None:
        self.display_name = display_name
        self.function_to_call = function_to_call
        self.index = index

    def __str__(self) -> str:
        return f"{self.index}. {self.display_name.upper()}"

class TextMenu:
    def __init__(self) -> None:
        self.menu_items: dict = {}

    def __str__(self) -> str:
        output = ""
        for menu_item in self.menu_items:
            output += f"{self.menu_items[menu_item]}\n"
        return f"{output}"
    
    def next_index(self) -> int:
        return len(self.menu_items) + 1

    def add_menu_item(self, display_name: str, function_to_call: str) -> None:
        self.menu_items[display_name] = MenuItem(display_name,
                                                function_to_call,
                                                self.next_index())

    def remove_menu_item(self, display_name: str) -> None:
        del self.menu_items[display_name]

    def get_user_input(self) -> None:
        pass

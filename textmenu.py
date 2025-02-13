class MenuItem:
    """
    
    """
    def __init__(self, display_name: str, function_to_call: str,
                 args: str, index: int) -> None:
        """Initializes an instance of a menu item.
        
        Args:
            display_name: Name of the menu item.
            function_to_call: String representing function to be called when
              the menu item is selected by the user.
        """
        self.display_name = display_name
        self.function_to_call = function_to_call
        self.args = args
        self.index = index
        self.aliases = [f"{index}", display_name]

    def add_item_alias(self, alias: str) -> None:
        """Adds additional options to select menu item.

        Args:
            alias: Alternate text input the select menu item.
        """
        self.aliases.append(alias) 

    def __str__(self) -> str:
        """Returns string 
        
        """
        return f"{self.index}. {self.display_name}"
    
    def call_function(self):
        self.function_to_call(f"{self.args}")

class TextMenu:
    """A text-based menu.
    Attributes:
        menu_items: Dictionary containing the menu items making up the menu.
        visibility: 
    """
    def __init__(self, visibility: bool = True,
                 space_before_prompt: bool = True) -> None:
        """Initializes instance of a menu.

        Args:
            visibility: Determines if the menu items should be listed when
              user is prompted for input.
            space_before_prompt: Determines if a blank line is printed before
              the prompt for user input.
        """
        self.menu_items: dict = {}
        self.visibility = visibility
        self.space_before_prompt = space_before_prompt

    def __str__(self) -> str:
        """Returns line separated list of the items in the menu.
        """
        output = ""
        for menu_item in self.menu_items:
            output += f"{self.menu_items[menu_item]}\n"
        return f"{output}"
    
    def next_index(self) -> int:
        return len(self.menu_items) + 1

    def add_menu_item(self, display_name: str,
                      function_to_call, args: str = "") -> None:
        """Adds a new item to the menu.

        Args:
            display_name: Name of the menu item to be added. 
            function_to_call: String representing function to be called when
              the menu item is selected.        
        """
        if display_name in self.menu_items:
            raise KeyError("Menu item display_name must be unique.")
        self.menu_items[display_name] = (
            MenuItem(display_name, function_to_call, args, self.next_index()))

    def remove_menu_item(self, display_name: str,
                         reindex: bool = True) -> None:
        """Removes an item from the menu.

        Args:
            display_name: The key value for the menu item.
            reindex: If True, index values for the remaining menu items will
              be reassigned.

        Raises:
            KeyError: Entered display_name is not found in the menu.
        """
        if display_name not in self.menu_items:
            raise KeyError(f"Menu item {display_name} does not exist.")
        del self.menu_items[display_name]
        if reindex == True:
            self.reindex()

    def reindex(self) -> None:
        """Sequentially reassigns index values for each item in the menu.
        """
        i = 1
        for menu_item in self.menu_items:
            self.menu_items[menu_item].index = i
            i += 1

    def get_user_input(self, prompt: str = "Select Option: ") -> None:
        """Prompts the user for a command and returns the input.

        Args:
            prompt: String displayed to user to prompt input.
        """
        if self.visibility:
            print(self, end="")
        if self.space_before_prompt:
            print()
        user_input = input(prompt)
        for menu_item in self.menu_items:
            if user_input in self.menu_items[menu_item].aliases:
                self.menu_items[menu_item].call_function()
                break


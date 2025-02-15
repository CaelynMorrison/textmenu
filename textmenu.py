from collections.abc import Callable

class MenuItem:
    """
    
    """
    def __init__(self, display_name: str, callback: Callable,
                 index: int, *args: tuple,) -> None:
        """Initializes an instance of a menu item.
        
        Args:
            display_name: Name of the menu item.
            function_to_call: String representing function to be called when
              the menu item is selected by the user.
            args: arguments to pass to the function when called.
            index: Numerical representation of the menu item.
        """
        self.display_name = display_name
        self.callback = callback
        self.args = args
        self.index = index
        self.aliases = [f"{index}", display_name.lower()]

    def add_alias(self, *args: str) -> None:
        """Adds additional options to select menu item.

        Args:
            args: Aliases to be added to the the select menu item.
        """
        for alias in args:
            if alias.lower() not in self.aliases:
                self.aliases.append(alias.lower())

    def remove_alias(self, *args: str) -> None:
        """Removes additional options to select menu item.

        Args:
            args: Aliases to be removed from the the select menu item.
        """
        for alias in args:
            if alias.lower() in self.aliases:
                self.aliases.remove(alias.lower())
            else:
                raise KeyError(f"{alias} is not a valid alias of "
                            f"{self.display_name}.")

    def __str__(self) -> str:
        """Returns string 
        
        """
        return f"{self.index}. {self.display_name}"
    
    def call_function(self):
        self.callback(*self.args)

class TextMenu:
    """A text-based menu.
    Attributes:
        menu_items: Dictionary containing the menu items making up the menu.
        visibility: Determines if menu items are listed before user is prompted
          for input.
        space_before_prompt: Determines if a blank line is printed before
              the prompt for user input.        
    """
    def __init__(self, visibility: bool = True,
                 space_before_list: bool = True,
                 space_before_prompt: bool = True,
                 reprompt: bool = True) -> None:
        """Initializes instance of a menu.

        Args:
            visibility: Determines if the menu items should be listed when
              user is prompted for input.
            space_before_prompt: Determines if a blank line is printed before
              the prompt for user input.
            reprompt: Determines if user should be reprompted if input is
              not found.
        """
        self.menu_items: dict = {}
        self.visibility = visibility
        self.space_before_list = space_before_list
        self.space_before_prompt = space_before_prompt
        self.reprompt = reprompt

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
                      callback: Callable, *args: tuple) -> None:
        """Adds a new item to the menu.

        Args:
            display_name: Name of the menu item to be added. 
            function_to_call: String representing function to be called when
              the menu item is selected.        
        """
        if display_name in self.menu_items:
            raise KeyError("Menu item display_name must be unique.")
        self.menu_items[display_name] = (
            MenuItem(display_name, callback, self.next_index(), *args))

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
            self.menu_items[menu_item].remove_alias(
                f"{self.menu_items[menu_item].index}")
            self.menu_items[menu_item].index = i
            i += 1

    def get_user_input(self, prompt: str = "Select Option: ") -> None:
        """Prompts the user for a command and returns the input.

        Args:
            prompt: String displayed to user to prompt input.
        """
        if self.visibility:
            if self.space_before_prompt:
                print()
            print(self, end="")
        if self.space_before_prompt:
            print()
        user_input = input(prompt).lower()
        found = False
        for menu_item in self.menu_items:
            if user_input in self.menu_items[menu_item].aliases:
                found = True
                self.menu_items[menu_item].call_function()
                break
        if found == False and self.reprompt == True:
            self.get_user_input(prompt) 


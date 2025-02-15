import pytest
from textmenu import TextMenu
from textmenu import MenuItem


def test_menu_creation_defaults():
    test_menu = TextMenu()
    assert test_menu.visibility == True
    assert test_menu.space_before_list == True
    assert test_menu.space_before_prompt == True
    assert test_menu.reprompt == True

def test_menu_creation_defaults_overwritten():
    test_menu = TextMenu(visibility = False, space_before_list = False,
                         space_before_prompt = False, reprompt = False)
    assert test_menu.visibility == False
    assert test_menu.space_before_list == False
    assert test_menu.space_before_prompt == False
    assert test_menu.reprompt == False

def test_menu_creation_defaults_single_overwrite():
    test_menu = TextMenu(space_before_prompt = False)
    assert test_menu.visibility == True
    assert test_menu.space_before_list == True
    assert test_menu.space_before_prompt == False
    assert test_menu.reprompt == True

def test_add_menu_item():
    test_menu = TextMenu()
    def add_numbers(a, b):
        return a + b
    test_menu.add_menu_item("ADD", add_numbers, 5, 7)
    assert test_menu.menu_items["ADD"].display_name == "ADD"
    assert test_menu.menu_items["ADD"].args == (5, 7)

def test_remove_menu_item():
    test_menu = TextMenu()
    def add_numbers(a, b):
        return a + b
    test_menu.add_menu_item("ADD", add_numbers, 5, 7)
    test_menu.remove_menu_item("ADD")
    assert test_menu.menu_items == {}

def test_remove_menu_item_doesnt_exist():
    test_menu = TextMenu()
    with pytest.raises(KeyError, match = "Menu item ADD does not exist."):
        test_menu.remove_menu_item("ADD")

def test_remove_menu_item_reindex():
    test_menu = TextMenu()
    def add_numbers(a, b):
        return a + b
    test_menu.add_menu_item("ITEM1", add_numbers, 1, 2)
    test_menu.add_menu_item("ITEM2", add_numbers, 1, 2)
    test_menu.remove_menu_item("ITEM1")
    assert test_menu.menu_items["ITEM2"].index == 1

def test_remove_menu_item_no_reindex():
    test_menu = TextMenu()
    def add_numbers(a, b):
        return a + b
    test_menu.add_menu_item("ITEM1", add_numbers, 1, 2)
    test_menu.add_menu_item("ITEM2", add_numbers, 1, 2)
    test_menu.remove_menu_item("ITEM1", False)
    assert test_menu.menu_items["ITEM2"].index == 2

def test_remove_menu_item_add_after_reindex():
    test_menu = TextMenu()
    def add_numbers(a, b):
        return a + b
    test_menu.add_menu_item("ITEM1", add_numbers, 1, 2)
    test_menu.add_menu_item("ITEM2", add_numbers, 1, 2)
    test_menu.remove_menu_item("ITEM1")
    test_menu.add_menu_item("ITEM3", add_numbers, 1, 2)
    assert test_menu.menu_items["ITEM3"].index == 2
    
def test_remove_menu_item_add_after_no_reindex():
    test_menu = TextMenu()
    def add_numbers(a, b):
        return a + b
    test_menu.add_menu_item("ITEM1", add_numbers, 1, 2)
    test_menu.add_menu_item("ITEM2", add_numbers, 1, 2)
    test_menu.remove_menu_item("ITEM1", False)
    test_menu.add_menu_item("ITEM3", add_numbers, 1, 2)
    assert test_menu.menu_items["ITEM2"].index == 3



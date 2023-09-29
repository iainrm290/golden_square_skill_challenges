from lib.todo_list import *
from lib.todo import *
import pytest

def test_intantiation_of_todo_list():
    todo_list = TodoList()
    assert isinstance(todo_list, TodoList) == True


def test_intantiation_of_todo():
    todo = Todo("Everything")
    assert isinstance(todo, Todo) == True


def test_todo_list_add():
    todo_list = TodoList()
    todo1 = Todo("Shopping")
    todo_list.add((todo1.task, todo1.complete))
    assert todo_list.task_list == [("Shopping", False)]

def test_todo_list_incomplete():
    todo_list = TodoList()
    todo1 = Todo("Shopping")
    todo_list.add((todo1.task, todo1.complete))
    todo2 = Todo("Cooking")
    todo_list.add((todo2.task, todo2.complete))
    assert todo_list.incomplete() == ["Shopping", "Cooking"]

def test_todo_list_complete():
    todo_list = TodoList()
    todo1 = Todo("Shopping")
    todo1.mark_complete()
    todo_list.add((todo1.task, todo1.complete))
    todo2 = Todo("Cooking")
    todo_list.add((todo2.task, todo2.complete))
    assert todo_list.complete() == ["Shopping"]

def test_todo_list_give_up():
    todo_list = TodoList()
    todo1 = Todo("Shopping")
    todo1.mark_complete()
    todo_list.add((todo1.task, todo1.complete))
    todo2 = Todo("Cooking")
    todo2.mark_complete()
    todo_list.add((todo2.task, todo2.complete))
    assert todo_list.incomplete() == []
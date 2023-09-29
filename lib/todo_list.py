class TodoList:
    def __init__(self):
        self.task_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.task_list.append(todo)
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        tasks_todo = [task[0] for task in self.task_list if not task[1]]
        return tasks_todo

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        tasks_complete = [task[0] for task in self.task_list if task[1]]
        return tasks_complete

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass
import sqlite3
import todo_class
import datetime

class ListOfTodos:
    def __init__(self, conn: sqlite3.Connection ) -> None:
        self.conn = conn 

    def add_todo(self, todo: todo_class.ToDo):
        with self.conn:
            c = self.conn.cursor()
            # c.execute("SELECT status, description, due_date FROM todo_list WHERE status = :status and description =:description and due_date = :due_date", {'status': todo.status, 'description': todo.description, 'due_date': todo.due_date})
            # results = c.fetchall()
            # print(results)
            c.execute("""INSERT INTO todo_list VALUES (:status, :description, :due_date)""", 
                {'status': todo.status, 'description': todo.description, 'due_date': todo.due_date.strftime('%Y/%m/%d %H:%M')})

    def get_all_tasks(self):
        with self.conn:
            c = self.conn.cursor()
            c.execute("SELECT status, description, due_date FROM todo_list")
            results = c.fetchall()
            return [todo_class.ToDo(*x) for x in results]

    def show_all_tasks(self):
        tasks = self.get_all_tasks()
        {print(task) for task in tasks}

    def get_missed_tasks(self):
        with self.conn:
            c = self.conn.cursor()
            c.execute("SELECT status, description, due_date FROM todo_list WHERE due_date < :current_date", {'current_date': datetime.datetime.now().strftime('%Y/%m/%d %H:%M')})
            results = c.fetchall()
            return [todo_class.ToDo(*x) for x in results]

    def show_missed_tasks(self):
        tasks = self.get_missed_tasks()
        {print(task) for task in tasks}

    def get_tasks_for_today(self):
        with self.conn:
            c = self.conn.cursor()
            today = datetime.datetime.now().strftime('%Y/%m/%d') + '%'
            print(f"today: {today}")
            c.execute("SELECT status, description, due_date FROM todo_list WHERE due_date like :current_date", {'current_date': today})
            results = c.fetchall()
            return [todo_class.ToDo(*x) for x in results]

    def show_tasks_for_today(self):
        tasks = self.get_tasks_for_today()
        {print(task) for task in tasks}


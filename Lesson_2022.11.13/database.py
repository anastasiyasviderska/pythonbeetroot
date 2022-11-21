import sqlite3
import todo_class
import todos_containers

if __name__ == "__main__":

    conn = sqlite3.connect('todo_list.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS todo_list(
                status text,
                description text,
                due_date text
                ) """)

    todo_list = todos_containers.ListOfTodos(conn)

    task1 = todo_class.ToDo('created', 'brush my teeth', '2022/10/17 08:00')
    task2 = todo_class.ToDo('created', 'clean the kitchen', '2022/11/18 10:00')
    task3 = todo_class.ToDo('created', 'clean the living room', '2022/11/18 18:00')
    task4 = todo_class.ToDo('created', 'clean the bath room', '2022/11/19 10:00')
    task5 = todo_class.ToDo('created', 'clean the hall', '2022/11/19 12:00')

    # todo_list.add_todo(task1)
    # todo_list.add_todo(task2)
    # todo_list.add_todo(task3)
    # todo_list.add_todo(task4)
    # todo_list.add_todo(task5)

    print('\n\t ALL\n')
    todo_list.show_all_tasks()
    print('\n\tMISSED\n')
    todo_list.show_missed_tasks()
    print('\n\tTODAY\n')
    todo_list.show_tasks_for_today()

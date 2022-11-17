import unittest
import todo_class
import todos_containers
import datetime


class ToDoTestCase(unittest.TestCase):

    def setUp(self):
        self.my_todo_list = todos_containers.ListOfTodos()
        self.task1 = todo_class.ToDo('created', 'brush my teeth', '2022/10/17 08:00')
        self.task2 = todo_class.ToDo('created', 'clean the apartment', '2023/11/17 10:00')
        self.now = datetime.datetime.now()
        self.now_str = self.now.strftime('%Y/%m/%d %H:%M')


    def test_container(self):
        self.my_todo_list.add_todo(self.task1)
        self.assertEqual(len(self.my_todo_list.list_of_todos), 1)
        self.my_todo_list.add_todo(self.task2)
        self.assertEqual(len(self.my_todo_list.list_of_todos), 2)
    
    def test_task1_status(self):
        self.assertEqual(self.task1.status, 'created')
        self.task1.status = 'in progress'
        self.assertEqual(self.task1.status, 'in progress')
        self.task1.status = 'done'
        self.assertNotEqual(self.task1.status, 'done')
        self.task1.status = 'Finished'
        self.assertNotEqual(self.task1.status, 'finished')
        self.task1.status = 'finished'
        self.assertEqual(self.task1.status, 'finished')

    def test_task1_due_date(self):
        self.assertTrue(self.task1.past_due_date())
        self.assertFalse(self.task1.todays_date())
        self.task1.due_date = self.now_str
        self.assertTrue(self.task1.todays_date())
    
    def test_task1_description(self):
        self.assertEqual(self.task1.description, 'brush my teeth')
        self.task1.description = 'clean my teeth'
        self.assertEqual(self.task1.description, 'clean my teeth')
        


unittest.main()
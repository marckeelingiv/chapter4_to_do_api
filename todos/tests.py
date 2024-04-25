from django.test import TestCase

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(
            title='First todo',
            body='A body here',
            completed=False
        )

    def test_title_content(self):
        self.assertEqual(self.todo.title, 'First todo')
        self.assertEqual(str(self.todo), 'First todo')
        self.assertEqual(self.todo.body, 'A body here')
        self.assertEqual(self.todo.completed, False)

    def test_api_listview(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(
            f'/api/{self.todo.id}/'
            ,format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.todo)

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from actions import toggle_todo
from store import store
from reducers import todo_reducers
import containers


class ToDoApp(App):

    def build(self):
        pass


if __name__ == '__main__':
    ToDoApp().run()

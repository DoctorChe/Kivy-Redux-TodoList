from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, StringProperty

class Link(ToggleButton):
    release_callback = ObjectProperty(None)
    vis_filter = StringProperty(None)

    def on_vis_filter(self, instance, value):
        options = {'SHOW_ALL': 'All', 'SHOW_ACTIVE': 'Active',
                   'SHOW_COMPLETED': 'Completed'}
        self.text = options[value]

    def on_touch_down(self, touch):
        if self.state == 'down':
            return False
        else:
            super(Link, self).on_touch_down(touch)

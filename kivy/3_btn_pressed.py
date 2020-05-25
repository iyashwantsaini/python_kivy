from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class rootLayout(BoxLayout):
    
    def __init__(self, **kwargs):
        super(rootLayout,self).__init__(**kwargs)

        self.add_widget(Button(text="btn-1",size=(30,30)))
        
        cb1=customButton()
        cb1.bind(pressed=self.btn_pressed)
        cb1.text="cb-1"
        self.add_widget(cb1)

        # cb2=customButton()
        # cb2.bind(pressed=self.btn_pressed)
        # cb2.text="cb-2"
        # self.add_widget(cb2)

        self.add_widget(Button(text="btn-2"))
    
    def btn_pressed(self,instance,pos):
        print('i_m_from_root :{pos}'.format(pos=pos))

class customButton(Widget):

    pressed=ListProperty([0,0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed=touch.pos
            return True
        return super(customButton,self).on_touch_down(touch)

    def on_pressed(self,instance,pos):
        print('pressed at {pos}'.format(pos=pos))

class textApp(App):
    def build(self):
        return rootLayout()

if __name__=='__main__':
    textApp().run()

    
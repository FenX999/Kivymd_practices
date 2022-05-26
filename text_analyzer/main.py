from textblob import TextBlob
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (480, 800)

class TextInterferace(RelativeLayout):
    def cleanner(self):
        self.ids.input.text = ''
    def submiter(self):
        blob = TextBlob(self.ids.input.text)
        self.ids.wcounter.text=str(len(blob.words))
        self.ids.scounter.text=str(len(blob.sentences))
        sent_on_text = blob.sentiment
        pol, subj = sent_on_text
        self.ids.pol_text.text=str(pol*100)+ '%'
        self.ids.subj_text.text=str(subj*100)+ '%'
        #debug
        # print(sent_on_text)
        # print(f'polarity at: {pol}')
        # print(f'sujectivity at: {subj}')
class ScanApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = "Dark"
        return 0

if __name__=="__main__":
     ScanApp().run()
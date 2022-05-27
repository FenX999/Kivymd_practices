import config #config file with firebase credentials/info
import pyrebase

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog



class LoginInterface(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        firebase = pyrebase.initialize_app(config.firebase_conf)
        self.database = firebase.database()

    def create_entry(self):
        username = self.ids.signup_username.text
        email = self.ids.signup_email.text
        password = self.ids.signup_password.text
        data_exist = False
        if len(username) and len(email) and len(password) > 0:
            data_entry = self.database.get()
            if (data_entry.val() == None):
                data_exist = False
            else:
                for single_data in data_entry.each():
                    dict= single_data.val()
                    if dict['Username'] == username:
                        data_exist = True
                        username_dialog = MDDialog(
                            title='Error Message',
                            text='"Username" already used'
                        )
                        username_dialog.open()
                        break
                    elif dict['Email']== email:
                        data_exist = True
                        email_dialog = MDDialog(
                            title='Error Message',
                            text='"Email" already used'
                        )
                        email_dialog.open()
                        break
        else:
            signup_error = MDDialog(
                title='Sign up error',
                text= 'Please inform all the fields' 
            )
            signup_error.open()
        if data_exist==False:
            data = {"Username": username, "Email": email, "Password": password}
            self.database.child(username).set(data)
    
    def login(self):
        email = self.ids.login_email.text
        password = self.ids.login_password.text

        data_entry = self.database.get()
        if (data_entry.val() == None):
            print(f'You must Sign Up first')
        for single_data in data_entry.each():
            dict= single_data.val()
            if dict['Email']== email and dict['Password'] == password:
                print(f'Success!')
                succcess_dialog = MDDialog(
                    title='Login Information', 
                    text= 'Success!'
                )
                succcess_dialog.open()
                break
            else:
                failed_dialog = MDDialog(
                    title='Login Error',
                    text='Login failed please check your credentials',
                )
                failed_dialog.open()

class LoginApp(MDApp):
    def color_changer(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = 'Teal'
        else:
            self.theme_cls.primary_palette = "Teal"
            self.theme_cls.theme_style = "Dark"

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        return 

if __name__=="__main__":
    LoginApp().run()
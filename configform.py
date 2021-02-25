import json
import tkinter as tk
import tkinter.font as tkfont
import re
import os
from tkinter.messagebox import showinfo


class ConfigForm:
    filename = "config.json"

    @staticmethod
    def load_config():
        if os.path.isfile(ConfigForm.filename):
            with open(ConfigForm.filename, "r") as config_file:
                config_dict = json.load(config_file)
                config_dict['Counter'] = int(config_dict['Counter']) + 1
            with open(ConfigForm.filename, "w") as config_file:
                json.dump(config_dict, config_file)
            return config_dict
        else:
            showinfo("WARNING", message="You have to config first.")
            return

    def __init__(self):
        # Windows meta
        window = tk.Toplevel()
        window.title('Create Config')
        window.geometry('500x330')
        window.configure(background='white')

        # Load config if exist else set default config value
        if os.path.isfile(ConfigForm.filename):
            with open(ConfigForm.filename, "r") as config_file:
                self.config_dict = {key: tk.StringVar(value=val) for key, val in json.load(config_file).items()}
        else:
            self.config_dict = {
                "Email": tk.StringVar(value=''),
                "User Name": tk.StringVar(value=''),
                "Password": tk.StringVar(value=''),
                "Counter": tk.StringVar(value='0'),
            }

        # Windows model
        tk.Label(window, text='Create Config file', font=tkfont.Font(size=20)).pack(side=tk.TOP)
        (input_frame := tk.Frame(window)).pack(side=tk.TOP)
        tk.Button(window, text="Save Config", command=self._save_config_).pack(side=tk.TOP)
        (message_label := tk.Label(window, justify=tk.LEFT)).pack(side=tk.TOP)
        self.message_label = message_label

        # input_frame
        for idx, (key, val) in enumerate(self.config_dict.items()):
            tk.Label(input_frame, text=key).grid(row=idx, column=0)
            tk.Entry(input_frame, textvariable=val, width=50).grid(row=idx, column=1)
        window.mainloop()

    def _save_config_(self):
        # Check format of each entry
        message = []
        if not re.match(r'.+@.+', self.config_dict['Email'].get()):
            message.append('The email format is not correct. "Address", "@", "Domain" are necessary.')
        if len(self.config_dict['User Name'].get()) < 4:
            message.append('User Name too Short (less than 4)')
        if not (re.match(r'.*[A-Z].*', self.config_dict['Password'].get())
                and re.match(r'.*[a-z].*', self.config_dict['Password'].get())
                and re.match(r'.*[0-9].*', self.config_dict['Password'].get())
                and re.match(r'.*[@$!%*?&-+:#^=<>.|].*', self.config_dict['Password'].get())):
            message.append('The password format is not correct. It need at least:\n'
                           '  * one lowercase a-z\n'
                           '  * one uppercase A-Z\n'
                           '  * one special @$!%*?&-+:#^=<>.|\n'
                           '  * one number 0-9')
        if not re.match(r'[0-9]+', self.config_dict['Counter'].get()):
            message.append('Counter should be a number')

        # Save while check passed
        if message:
            self.message_label['text'] = "\n".join(message)
        else:
            with open(ConfigForm.filename, "w") as config_file:
                json.dump({key: val.get() for key, val in self.config_dict.items()}, config_file)
                self.message_label['text'] = "Save config successfully"


if __name__ == '__main__':
    ConfigForm()

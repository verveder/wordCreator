"""This module introduces classes and functions"""

from pathlib import Path
import tkinter as tk

import src.config as cf

# GLOBAL VARIABLES
word_type = cf.word_type
num_of_keys = cf.num_of_keys

radios_word_type = cf.radios_word_type
radios_num_of_keys = cf.radios_num_of_keys

using_prefixes = cf.using_prefixes
using_suffixes = cf.using_suffixes
using_endings = cf.using_endings

language = cf.language

assets_path = cf.assets_path

default_output = cf.default_output


class App(tk.Tk):
    """Describes main app window"""
    def __init__(self):
        super().__init__()
        self.geometry('800x600')

        self.title('CREATOR')
        self.configure(bg=cf.COLOR_BG)
        self.iconbitmap(f'{cf.assets_path}\\icon.ico')


class CustomButton(tk.Button):
    """Reorganises standard buttons"""
    def __init__(self, master, xpos, ypos, width, height, image_idle, image_hover):
        super().__init__(master=master)
        self.master = master

        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height

        image_idle = get_path(image_idle)
        image_hover = get_path(image_hover)

        self.image_idle = tk.PhotoImage(file=image_idle)
        self.image_hover = tk.PhotoImage(file=image_hover)

        self.button = tk.Button(
            master=self.master,
            image=self.image_idle,
            bg=cf.COLOR_BG,
            width=self.width,
            height=self.height,
            relief='flat',
            border=1,
            highlightthickness=0
            )

        self.button.bind('<Enter>', self.on_enter)
        self.button.bind('<Leave>', self.on_leave)

    def on_enter(self, event):
        """Defines attitude when cursor enters"""
        self.set_hovered()

    def on_leave(self, event):
        """Defines attitude when cursor leaves"""
        self.reset_button()

    def reset_button(self):
        """Resets hover effects"""
        self.button.config(image=self.image_idle)

    def set_hovered(self):
        """Defines hover effects"""
        self.button.config(image=self.image_hover)


class SpecificButton(CustomButton):
    """Describes buttons with specific attitude"""
    def __init__(self, toggle, image_toggled, **kwargs):
        super().__init__(**kwargs)

        self.toggle = toggle

        image_toggled = get_path(image_toggled)
        self.image_toggled = tk.PhotoImage(file=image_toggled)

        self.button.bind('<Button-1>', self.on_click)

    def on_click(self, event):
        """Defines attitude on click"""
        self.set_toggled()

    def set_toggled(self):
        """Defines attitude when toggled"""
        self.button.config(image=self.image_toggled)


class RadioButton(SpecificButton):
    """Describes radiobuttons"""
    def __init__(self, radio_type, image_hover_toggled, **kwargs):
        super().__init__(**kwargs)
        self.radio_type = radio_type
        self.group = self.assign_group()

        image_hover_toggled = get_path(image_hover_toggled)
        self.image_hover_toggled = tk.PhotoImage(file=image_hover_toggled)

    def on_click(self, event):
        self.set_toggled()
        self.set_value()
        for button in self.group:
            if button != self:
                button.reset_button()

    def on_enter(self, event):
        if self.if_word_type():
            if word_type == self.toggle:
                self.set_hover_toggled()
            elif word_type != self.toggle:
                self.set_hovered()
        elif self.if_num_of_keys():
            if num_of_keys == self.toggle:
                self.set_hover_toggled()
            elif num_of_keys != self.toggle:
                self.set_hovered()

    def on_leave(self, event):
        if self.if_word_type():
            if word_type == self.toggle:
                self.set_toggled()
            elif word_type != self.toggle:
                self.reset_button()
        elif self.if_num_of_keys():
            if num_of_keys == self.toggle:
                self.set_toggled()
            elif num_of_keys != self.toggle:
                self.reset_button()

    def set_hover_toggled(self):
        """Defines attitude for toggled button when cursor enters"""
        self.button.config(image=self.image_hover_toggled)

    def set_value(self):
        """Defines action on toggling"""
        if self.if_word_type():
            set_word_type(self.toggle)
        elif self.if_num_of_keys():
            set_num_of_keys(self.toggle)

    def if_word_type(self):
        """Checks for radio_type: word_type"""
        if self.radio_type == 'word_type':
            return True
        else:
            return False

    def if_num_of_keys(self):
        """Checks for radio_type: num_of_keys"""
        if self.radio_type == 'num_of_keys':
            return True
        else:
            return False

    def assign_group(self):
        """Organises radiobuttons in groups depending on their radio_type"""
        global radios_word_type, radios_num_of_keys
        if self.if_word_type():
            radios_word_type.append(self)
            return radios_word_type
        elif self.if_num_of_keys():
            radios_num_of_keys.append(self)
            return radios_num_of_keys
        else:
            return None


class CheckButton(SpecificButton):
    """Describes check-buttons"""
    def __init__(self, check_type, image_hover_toggled, **kwargs):
        super().__init__(**kwargs)
        self.check_type = check_type

        image_hover_toggled = get_path(image_hover_toggled)
        self.image_hover_toggled = tk.PhotoImage(file=image_hover_toggled)

    def on_click(self, event):
        if self.if_prefixes():
            if using_prefixes:
                untick_prefixes()
                self.reset_button()
            elif not using_prefixes:
                tick_prefixes()
                self.set_toggled()
        elif self.if_suffixes():
            if using_suffixes:
                untick_suffixes()
                self.reset_button()
            elif not using_suffixes:
                tick_suffixes()
                self.set_toggled()
        elif self.if_endings():
            if using_endings:
                untick_endings()
                self.reset_button()
            elif not using_endings:
                tick_endings()
                self.set_toggled()

    def on_enter(self, event):
        if self.if_prefixes():
            if using_prefixes:
                self.set_hover_toggled()
            elif not using_prefixes:
                self.set_hovered()
        elif self.if_suffixes():
            if using_suffixes:
                self.set_hover_toggled()
            elif not using_suffixes:
                self.set_hovered()
        elif self.if_endings():
            if using_endings:
                self.set_hover_toggled()
            elif not using_endings:
                self.set_hovered()

    def on_leave(self, event):
        if self.if_prefixes():
            if using_prefixes:
                self.set_toggled()
            elif not using_prefixes:
                self.reset_button()
        elif self.if_suffixes():
            if using_suffixes:
                self.set_toggled()
            elif not using_suffixes:
                self.reset_button()
        elif self.if_endings():
            if using_endings:
                self.set_toggled()
            elif not using_endings:
                self.reset_button()

    def set_hover_toggled(self):
        """Defines attitude for toggled button when cursor enters"""
        self.button.config(image=self.image_hover_toggled)

    def if_prefixes(self):
        """Checks for check_type: prefixes"""
        if self.check_type == 'prefixes':
            return True
        else:
            return False

    def if_suffixes(self):
        """Checks for check_type: suffixes"""
        if self.check_type == 'suffixes':
            return True
        else:
            return False

    def if_endings(self):
        """Checks for check_type: endings"""
        if self.check_type == 'endings':
            return True
        else:
            return False


class LanguageToggle(SpecificButton):
    """Describes language toggles"""
    def __init__(self, paired_button, **kwargs):
        super().__init__(**kwargs)
        self.paired_button = paired_button

    def on_click(self, event):
        self.paired_button.reset_button()
        self.set_toggled()
        self.lang_toggle_command(self.master)

    def on_leave(self, event):
        global language
        if language == self.toggle:
            self.set_toggled()
        elif language != self.toggle:
            self.reset_button()

    def lang_toggle_command(self, master):
        """Defines action on toggling LanguageToggle"""
        switch_lang(self.toggle)
        master.set_interface()

    def check_toggle(self):
        """Checks for value of variable 'language'"""
        global language
        if language == self.toggle:
            self.set_toggled()


class CustomEntry(tk.Entry):
    """Introduces entry with custom attributes"""
    def __init__(self, master, xpos, ypos, **kwargs):
        super().__init__(**kwargs)
        self.master = master

        self.xpos = xpos
        self.ypos = ypos

        self.bd = 0,
        self.bg = cf.COLOR_FIELD
        self.fg = cf.COLOR_FONT
        self.font = cf.FONT_INPUT

        self.width = 135
        self.height = 17


class CustomLabel(tk.Label):
    """Introduces label with custom attributes"""
    def __init__(self, master, xpos, ypos, **kwargs):
        super().__init__(**kwargs)
        self.master = master

        self.xpos = xpos
        self.ypos = ypos

        self.text = self.display_output(self.master)
        self.anchor = 'nw'
        self.bg = cf.COLOR_BG

    def display_output(self, master):
        """Allows CustomLabel to show output (default or returned from generators"""
        words_displayed = tk.Text(
            master=master, height=12, width=30, border=0,
            bg=cf.COLOR_FIELD, fg=cf.COLOR_FONT_DARK, font=cf.FONT
            )
        output_text = default_output
        words_displayed.place(bordermode='ignore', x=390, y=205, width=350, height=340)
        words_displayed.insert(tk.END, output_text)
        return output_text


def get_path(path: str) -> Path:
    """Returns Path to .images"""
    return cf.assets_path / Path(path)


def switch_lang(toggle):
    """Changes value of 'language'"""
    global language
    language = toggle


def set_word_type(toggle):
    """Assigns value to 'word_type' used by generators"""
    global word_type
    word_type = toggle


def set_num_of_keys(toggle):
    """Assigns value to 'num_of_keys' used by generators"""
    global num_of_keys
    num_of_keys = toggle


def tick_prefixes():
    """Sets using_prefixes to True"""
    global using_prefixes
    using_prefixes = True


def tick_suffixes():
    """Sets using_suffixes to True"""
    global using_suffixes
    using_suffixes = True


def tick_endings():
    """Sets using_endings to True"""
    global using_endings
    using_endings = True


def untick_prefixes():
    """Sets using_prefixes to False"""
    global using_prefixes
    using_prefixes = False


def untick_suffixes():
    """Sets using_suffixes to False"""
    global using_suffixes
    using_suffixes = False


def untick_endings():
    """Sets using_endings to False"""
    global using_endings
    using_endings = False

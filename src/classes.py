"""This module introduces classes and functions"""

from pathlib import Path
import tkinter as tk

import src.config as cf


class App(tk.Tk):
    """Describes main window"""
    def __init__(self):
        super().__init__()
        self.geometry('800x600')

        self.title('CREATOR')
        self.configure(bg=cf.COLOR_BG)
        self.iconbitmap(f'{cf.assets_path}\\icon.ico')

        self.image_background = tk.PhotoImage(file=f'{cf.assets_path}\\image_background.png')

        self.canvas = tk.Canvas(self, bg=cf.COLOR_BG, height=600, width=800, bd=0, relief='flat')
        self.canvas.place(x=0, y=0)
        self.canvas.create_image(400.0, 300.0, image=self.image_background)


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

        self.button.place(
            x=self.xpos, y=self.ypos,
            width=self.width, height=self.height,
            bordermode='ignore'
            )

        self.button.bind('<Enter>', self.on_enter)
        self.button.bind('<Leave>', self.on_leave)

    def on_enter(self, event):
        """Defines attitude when cursor enters"""
        self.set_hovered()

    def on_leave(self, event):
        """Defines attitude when cursor leaves"""
        self.reset_button()

    def set_hovered(self):
        """Defines hover effects"""
        self.button.config(image=self.image_hover)

    def reset_button(self):
        """Resets hover effects"""
        self.button.config(image=self.image_idle)


class TranslatedButton(CustomButton):
    """Describes buttons that depend on language chosen"""
    def __init__(self, images_idle, images_hover, has_translation, **kwargs):
        super().__init__(image_idle=images_idle[0], image_hover=images_hover[0], **kwargs)
        self.images_idle = images_idle
        self.images_hover = images_hover
        self.has_translation = has_translation

        image_idle_eng = get_path(images_idle[0])
        image_idle_rus = get_path(images_idle[1])
        image_hover_eng = get_path(images_hover[0])
        image_hover_rus = get_path(images_hover[1])

        self.image_idle_eng = tk.PhotoImage(file=image_idle_eng)
        self.image_idle_rus = tk.PhotoImage(file=image_idle_rus)
        self.image_hover_eng = tk.PhotoImage(file=image_hover_eng)
        self.image_hover_rus = tk.PhotoImage(file=image_hover_rus)

        self.add_to_translation_group()

    def add_to_translation_group(self):
        """Tags button for make it change when language switches"""
        if self.has_translation:
            cf.buttons_with_translation.append(self)
            return cf.buttons_with_translation
        else:
            return None

    def on_enter(self, event):
        if is_eng_language():
            self.button.config(image=self.image_hover_eng)
        elif is_rus_language():
            self.button.config(image=self.image_hover_rus)

    def on_leave(self, event):
        if is_eng_language():
            self.button.config(image=self.image_idle_eng)
        elif is_rus_language():
            self.button.config(image=self.image_idle_rus)

    def switch_image(self):
        """Adapts text on button for language chosen"""
        if is_eng_language():
            self.button.config(image=self.image_idle_eng)
        elif is_rus_language():
            self.button.config(image=self.image_idle_rus)


class LanguageToggle(TranslatedButton):
    """Describes language toggles"""
    def __init__(self, toggles, **kwargs):
        super().__init__(**kwargs)
        self.toggles = toggles

        self.button.bind('<Button-1>', self.on_click)

    def on_click(self, event):
        """Changes the interface language on click"""
        switch_lang(self.toggles)
        set_interface(self.master)
        translate_buttons()


class SpecificButton(CustomButton):
    """Describes specific buttons with similar attitude"""
    def __init__(self, toggle, toggle_type, image_toggled, image_hover_toggled, **kwargs):
        super().__init__(**kwargs)

        self.toggle = toggle
        self.toggle_type = toggle_type

        image_toggled = get_path(image_toggled)
        image_hover_toggled = get_path(image_hover_toggled)
        self.image_toggled = tk.PhotoImage(file=image_toggled)
        self.image_hover_toggled = tk.PhotoImage(file=image_hover_toggled)

        self.button.bind('<Button-1>', self.on_click)

    def on_click(self, event):
        """Defines attitude on click"""
        self.set_toggled()

    def on_enter(self, event):
        if self.is_toggled():
            self.set_hover_toggled()
        else:
            self.set_hovered()

    def on_leave(self, event):
        if self.is_toggled():
            self.set_toggled()
        else:
            self.reset_button()

    def set_toggled(self):
        """Defines attitude when toggled"""
        self.button.config(image=self.image_toggled)

    def set_hover_toggled(self):
        """Defines attitude for toggled button when cursor enters"""
        self.button.config(image=self.image_hover_toggled)

    def is_toggled(self):
        """Returns True if button is toggled (defined in subclasses)"""
        pass


class RadioButton(SpecificButton):
    """Describes radiobuttons"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.group = self.set_group()

    def on_click(self, event):
        self.set_toggled()
        self.set_value()
        for button in self.group:
            if button != self:
                button.reset_button()

    def set_value(self):
        """Defines action on toggling"""
        if self.is_word_type():
            set_word_type(self.toggle)
        elif self.is_num_of_keys():
            set_num_of_keys(self.toggle)

    def set_group(self):
        """Organises radiobuttons in groups depending on their radio_type"""
        if self.is_word_type():
            cf.radios_word_type.append(self)
            return cf.radios_word_type
        elif self.is_num_of_keys():
            cf.radios_num_of_keys.append(self)
            return cf.radios_num_of_keys
        else:
            return None

    def is_toggled(self):
        if self.is_word_type():
            if cf.word_type == self.toggle:
                return True
        elif self.is_num_of_keys():
            if cf.num_of_keys == self.toggle:
                return True
        else:
            return False

    def is_word_type(self):
        """Returns True if radio_type is word_type"""
        if self.toggle_type == 'word_type':
            return True
        else:
            return False

    def is_num_of_keys(self):
        """Returns True if radio_type is num_of_keys"""
        if self.toggle_type == 'num_of_keys':
            return True
        else:
            return False


class CheckButton(SpecificButton):
    """Describes check-buttons"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_click(self, event):
        if self.is_toggled():
            self.reset_button()
            if self.is_prefixes():
                untick_prefixes()
            elif self.is_suffixes():
                untick_suffixes()
            elif self.is_endings():
                untick_endings()
        else:
            self.set_toggled()
            if self.is_prefixes():
                tick_prefixes()
            elif self.is_suffixes():
                tick_suffixes()
            elif self.is_endings():
                tick_endings()

    def on_enter(self, event):
        if self.is_toggled():
            self.set_hover_toggled()
        else:
            self.set_hovered()

    def on_leave(self, event):
        if self.is_toggled():
            self.set_toggled()
        else:
            self.reset_button()

    def is_toggled(self):
        if self.is_prefixes():
            if cf.using_prefixes:
                return True
        elif self.is_suffixes():
            if cf.using_suffixes:
                return True
        elif self.is_endings():
            if cf.using_endings:
                return True
        else:
            return False

    def is_prefixes(self):
        """Returns True if check_type is prefixes"""
        if self.toggle_type == 'prefixes':
            return True
        else:
            return False

    def is_suffixes(self):
        """Returns True if check_type is suffixes"""
        if self.toggle_type == 'suffixes':
            return True
        else:
            return False

    def is_endings(self):
        """Returns True if check_type is endings"""
        if self.toggle_type == 'endings':
            return True
        else:
            return False


class CustomLabel(tk.Label):
    """Introduces label with custom attributes"""
    def __init__(self, master, xpos, ypos, output, **kwargs):
        super().__init__(**kwargs)
        self.master = master

        self.output = output

        self.xpos = xpos
        self.ypos = ypos

        self.anchor = 'nw'
        self.bg = cf.COLOR_BG

        self.text = tk.Text(
            master=master, height=12, width=30, border=0,
            bg=cf.COLOR_FIELD, fg=cf.COLOR_FONT_DARK, font=cf.FONT
            )
        self.text.place(
            bordermode='ignore', x=420, y=205, width=313, height=340
            )
        self.text.insert(tk.END, output)


def get_path(path: str) -> Path:
    """Returns Path to .images"""
    return cf.assets_path / Path(path)


def set_word_type(toggle):
    """Assigns value to 'word_type'"""
    cf.word_type = toggle


def set_num_of_keys(toggle):
    """Assigns value to 'num_of_keys'"""
    cf.num_of_keys = toggle


def tick_prefixes():
    """Sets using_prefixes to True"""
    cf.using_prefixes = True


def tick_suffixes():
    """Sets using_suffixes to True"""
    cf.using_suffixes = True


def tick_endings():
    """Sets using_endings to True"""
    cf.using_endings = True


def untick_prefixes():
    """Sets using_prefixes to False"""
    cf.using_prefixes = False


def untick_suffixes():
    """Sets using_suffixes to False"""
    cf.using_suffixes = False


def untick_endings():
    """Sets using_endings to False"""
    cf.using_endings = False


def is_rus_language():
    """Returns True if language is Russian"""
    if cf.language == 'rus':
        return True
    else:
        return False


def is_eng_language():
    """Returns True if language is English"""
    if cf.language == 'eng':
        return True
    else:
        return False


def switch_lang(toggle_list):
    """Switches value of 'language' to opposite"""
    if is_eng_language():
        cf.language = toggle_list[1]
    elif is_rus_language():
        cf.language = toggle_list[0]


def translate_buttons():
    for button in cf.buttons_with_translation:
        button.switch_image()


def set_interface(canvas):
    """Changes interface labels according to language"""
    if is_eng_language():
        switch_interface_to_eng(canvas)
    elif is_rus_language():
        switch_interface_to_rus(canvas)


def switch_interface_to_rus(canvas):
    """Shows Russian labels"""
    canvas.itemconfigure('eng', state='hidden')
    canvas.itemconfig('rus', state='normal')


def switch_interface_to_eng(canvas):
    """Shows English labels"""
    canvas.itemconfigure('rus', state='hidden')
    canvas.itemconfig('eng', state='normal')

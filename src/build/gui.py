"""This module sets GUI objects"""

import tkinter as tk

from src.classes import App, RadioButton, CheckButton, LanguageToggle, CustomEntry, CustomLabel
import src.config as cf

FONT = cf.FONT
FONT_LRG = cf.FONT_LRG
FONT_INPUT = cf.FONT_INPUT

COLOR_FONT = cf.COLOR_FONT
COLOR_FONT_DARK = cf.COLOR_FONT_DARK
COLOR_BG = cf.COLOR_BG
COLOR_FIELD = cf.COLOR_FIELD

language = cf.language


def set_interface():
    """Changes interface labels according to language"""
    global language
    if language == 'eng':
        switch_interface_to_eng()
    elif language == 'rus':
        switch_interface_to_rus()


def switch_interface_to_rus():
    """Switches interface language to Russian"""
    bg_canvas.itemconfigure('eng', state='hidden')
    bg_canvas.itemconfig('rus', state='normal')


def switch_interface_to_eng():
    """Switches interface language to English"""
    bg_canvas.itemconfigure('rus', state='hidden')
    bg_canvas.itemconfig('eng', state='normal')


app = App()

image_background = tk.PhotoImage(file=f'{cf.assets_path}\\image_background.png')
bg_canvas = tk.Canvas(app, bg=COLOR_BG, height=600, width=800, bd=0, relief='flat')
bg_canvas.place(x=0, y=0)
bg_background = bg_canvas.create_image(400.0, 300.0, image=image_background)

texts_eng = [
    bg_canvas.create_text(
        147.0, 158.0,
        anchor='nw', text='✦SETTINGS✦', fill=COLOR_FIELD, font=FONT_LRG, tags='eng'
        ),
    bg_canvas.create_text(
        519.0, 158.0,
        anchor='nw', text='✦OUTPUT✦', fill=COLOR_FIELD, font=FONT_LRG, tags='eng'
        ),
    bg_canvas.create_text(
        85.0, 207.0,
        anchor='nw', text='noun', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    bg_canvas.create_text(
        85.0, 253.0,
        anchor='nw', text='verb', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    bg_canvas.create_text(
        210.0, 207.0,
        anchor='nw', text='anthroponym', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    bg_canvas.create_text(
        246.0, 253.0,
        anchor='nw', text='toponym', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    bg_canvas.create_text(
        58.0, 340.0,
        anchor='nw', text='precise meaning', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    bg_canvas.create_text(
        235.0, 340.0,
        anchor='nw', text='precise key', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    bg_canvas.create_text(
        85.0, 389.0,
        anchor='nw', text='prefixes', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    bg_canvas.create_text(
        85.0, 434.0,
        anchor='nw', text='suffixes', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    bg_canvas.create_text(
        85.0, 479.0,
        anchor='nw', text='endings', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    bg_canvas.create_text(
        261.0, 389.0,
        anchor='nw', text='one key', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    bg_canvas.create_text(
        255.0, 434.0,
        anchor='nw', text='two keys', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    bg_canvas.create_text(
        242.0, 479.0,
        anchor='nw', text='three keys', fill=COLOR_FONT, font=FONT, tags='eng'
        )
    ]

texts_rus = [
    bg_canvas.create_text(
        137.0, 158.0,
        anchor='nw', text='✦УСТАНОВКИ✦', fill=COLOR_FIELD, font=FONT_LRG, tags='rus'
        ),
    bg_canvas.create_text(
        508.0, 158.0,
        anchor='nw', text='✦РЕЗУЛЬТАТ✦', fill=COLOR_FIELD, font=FONT_LRG, tags='rus'
        ),
    bg_canvas.create_text(
        85.0, 207.0,
        anchor='nw', text='имя сущ.', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    bg_canvas.create_text(
        85.0, 253.0,
        anchor='nw', text='глагол', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    bg_canvas.create_text(
        218.0, 207.0,
        anchor='nw', text='антропоним', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    bg_canvas.create_text(
        246.0, 253.0,
        anchor='nw', text='топоним', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    bg_canvas.create_text(
        55.0, 340.0,
        anchor='nw', text='точное значение', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    bg_canvas.create_text(
        225.0, 340.0,
        anchor='nw', text='точный ключ', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    bg_canvas.create_text(
        85.0, 389.0,
        anchor='nw', text='префиксы', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    bg_canvas.create_text(
        85.0, 434.0,
        anchor='nw', text='суффиксы', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    bg_canvas.create_text(
        85.0, 479.0,
        anchor='nw', text='окончания', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    bg_canvas.create_text(
        234.0, 389.0,
        anchor='nw', text='один ключ', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    bg_canvas.create_text(
        237.0, 434.0,
        anchor='nw', text='два ключа', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    bg_canvas.create_text(
        237.0, 479.0,
        anchor='nw', text='три ключа', fill=COLOR_FONT, font=FONT, tags='rus'
        )
    ]
#         self.item_id = self.master.create_window(
#             self.xpos, self.ypos, window=self.button
#             )
lang_toggle_rus = LanguageToggle(
    master=bg_canvas, toggle='rus', paired_button=None,
    image_idle='image_idle_language_rus.png',
    image_hover='image_hover_language_rus.png',
    image_toggled='image_toggled_language_rus.png',
    xpos=757.0, ypos=50.0, width=30.0, height=24.0
    )
lang_toggle_rus.place()

lang_toggle_eng = LanguageToggle(
    master=bg_canvas, toggle='eng', paired_button=None,
    image_idle='image_idle_language_eng.png',
    image_hover='image_hover_language_eng.png',
    image_toggled='image_toggled_language_eng.png',
    xpos=757.0, ypos=88.0, width=30.0, height=24.0
    )
lang_toggle_eng.place()

lang_toggle_rus.paired_button = lang_toggle_eng
lang_toggle_eng.paired_button = lang_toggle_rus

lang_toggle_rus.check_toggle()
lang_toggle_eng.check_toggle()

radio_noun = RadioButton(
    master=bg_canvas,
    xpos=51.0, ypos=210.0, width=24.0, height=24.0,
    radio_type='word_type', toggle='noun',
    image_idle='image_idle_radio.png',
    image_hover='image_hover_radio.png',
    image_toggled='image_toggled_radio.png',
    image_hover_toggled='image_hover_toggled_radio.png'
    )

radio_verb = RadioButton(
    master=bg_canvas,
    xpos=51.0, ypos=255.0, width=24.0, height=24.0,
    radio_type='word_type', toggle='verb',
    image_idle='image_idle_radio.png',
    image_hover='image_hover_radio.png',
    image_toggled='image_toggled_radio.png',
    image_hover_toggled='image_hover_toggled_radio.png'
    )

radio_anthroponym = RadioButton(
    master=bg_canvas,
    xpos=324.0, ypos=210.0, width=24.0, height=24.0,
    radio_type='word_type', toggle='anthroponym',
    image_idle='image_idle_radio.png',
    image_hover='image_hover_radio.png',
    image_toggled='image_toggled_radio.png',
    image_hover_toggled='image_hover_toggled_radio.png'
    )

radio_toponym = RadioButton(
    master=bg_canvas,
    xpos=324.0, ypos=255.0, width=24.0, height=24.0,
    radio_type='word_type', toggle='toponym',
    image_idle='image_idle_radio.png',
    image_hover='image_hover_radio.png',
    image_toggled='image_toggled_radio.png',
    image_hover_toggled='image_hover_toggled_radio.png'
    )

radio_one_key = RadioButton(
    master=bg_canvas,
    xpos=324.0, ypos=289.0, width=24.0, height=24.0,
    radio_type='num_of_keys', toggle=1,
    image_idle='image_idle_radio.png',
    image_hover='image_hover_radio.png',
    image_toggled='image_toggled_radio.png',
    image_hover_toggled='image_hover_toggled_radio.png'
    )

radio_two_keys = RadioButton(
    master=bg_canvas,
    xpos=324.0, ypos=434.0, width=24.0, height=24.0,
    radio_type='num_of_keys', toggle=2,
    image_idle='image_idle_radio.png',
    image_hover='image_hover_radio.png',
    image_toggled='image_toggled_radio.png',
    image_hover_toggled='image_hover_toggled_radio.png'
    )

radio_three_keys = RadioButton(
    master=bg_canvas,
    xpos=324.0, ypos=479.0, width=24.0, height=24.0,
    radio_type='num_of_keys', toggle=3,
    image_idle='image_idle_radio.png',
    image_hover='image_hover_radio.png',
    image_toggled='image_toggled_radio.png',
    image_hover_toggled='image_hover_toggled_radio.png'
    )

checkbox_prefixes = CheckButton(
    master=bg_canvas, check_type='prefixes', toggle=None,
    xpos=51, ypos=389, width=24.0, height=24.0,
    image_idle='image_idle_checkbox.png',
    image_hover='image_hover_checkbox.png',
    image_toggled='image_toggled_checkbox.png',
    image_hover_toggled='image_hover_toggled_checkbox.png'
    )

checkbox_suffixes = CheckButton(
    master=bg_canvas, check_type='suffixes', toggle=None,
    xpos=51, ypos=434, width=24.0, height=24.0,
    image_idle='image_idle_checkbox.png',
    image_hover='image_hover_checkbox.png',
    image_toggled='image_toggled_checkbox.png',
    image_hover_toggled='image_hover_toggled_checkbox.png'
    )

checkbox_endings = CheckButton(
    master=bg_canvas, check_type='endings', toggle=None,
    xpos=51, ypos=479, width=24.0, height=24.0,
    image_idle='image_idle_checkbox.png',
    image_hover='image_hover_checkbox.png',
    image_toggled='image_toggled_checkbox.png',
    image_hover_toggled='image_hover_toggled_checkbox.png'
    )

field_meaning = CustomEntry(app, xpos=51.0, ypos=318.0)
field_key = CustomEntry(app, xpos=209, ypos=318.0)

field_meaning.place()
field_key.place()

output = CustomLabel(app, xpos=380, ypos=200)
output.place()

set_interface()

app.mainloop()

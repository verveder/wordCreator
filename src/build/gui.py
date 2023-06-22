"""This module sets GUI objects"""

import tkinter as tk

import src.classes as cls
import src.config as cf

FONT = cf.FONT
FONT_LRG = cf.FONT_LRG
FONT_INPUT = cf.FONT_INPUT

COLOR_FONT = cf.COLOR_FONT
COLOR_FONT_DARK = cf.COLOR_FONT_DARK
COLOR_BG = cf.COLOR_BG
COLOR_FIELD = cf.COLOR_FIELD


app = cls.App()

texts_eng = [
    app.canvas.create_text(
        148.0, 158.0,
        anchor='nw', text='✦SETTINGS✦', fill=COLOR_FIELD, font=FONT_LRG, tags='eng'
        ),
    app.canvas.create_text(
        530.0, 158.0,
        anchor='nw', text='✦OUTPUT✦', fill=COLOR_FIELD, font=FONT_LRG, tags='eng'
        ),
    app.canvas.create_text(
        101.0, 210.0,
        anchor='nw', text='noun', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    app.canvas.create_text(
        101.0, 260.0,
        anchor='nw', text='verb', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    app.canvas.create_text(
        193.0, 210.0,
        anchor='nw', text='anthroponym', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    app.canvas.create_text(
        229.0, 260.0,
        anchor='nw', text='toponym', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    app.canvas.create_text(
        101.0, 360.0,
        anchor='nw', text='prefixes', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    app.canvas.create_text(
        101.0, 410.0,
        anchor='nw', text='suffixes', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    app.canvas.create_text(
        101.0, 460.0,
        anchor='nw', text='endings', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    app.canvas.create_text(
        243.0, 360.0,
        anchor='nw', text='one key', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    app.canvas.create_text(
        235.0, 410.0,
        anchor='nw', text='two keys', fill=COLOR_FONT, font=FONT, tags='eng'
        ),
    app.canvas.create_text(
        223.0, 460.0,
        anchor='nw', text='three keys', fill=COLOR_FONT, font=FONT, tags='eng'
        )
    ]

texts_rus = [
    app.canvas.create_text(
        138.0, 158.0,
        anchor='nw', text='✦УСТАНОВКИ✦', fill=COLOR_FIELD, font=FONT_LRG, tags='rus'
        ),
    app.canvas.create_text(
        519.0, 158.0,
        anchor='nw', text='✦РЕЗУЛЬТАТ✦', fill=COLOR_FIELD, font=FONT_LRG, tags='rus'
        ),
    app.canvas.create_text(
        101.0, 210.0,
        anchor='nw', text='имя сущ.', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    app.canvas.create_text(
        101.0, 260.0,
        anchor='nw', text='глагол', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    app.canvas.create_text(
        197.0, 210.0,
        anchor='nw', text='антропоним', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    app.canvas.create_text(
        227.0, 260.0,
        anchor='nw', text='топоним', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    app.canvas.create_text(
        101.0, 360.0,
        anchor='nw', text='префиксы', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    app.canvas.create_text(
        101.0, 410.0,
        anchor='nw', text='суффиксы', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    app.canvas.create_text(
        101.0, 460.0,
        anchor='nw', text='окончания', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    app.canvas.create_text(
        216.0, 360.0,
        anchor='nw', text='один ключ', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    app.canvas.create_text(
        219.0, 410.0,
        anchor='nw', text='два ключа', fill=COLOR_FONT, font=FONT, tags='rus'
        ),
    app.canvas.create_text(
        218.0, 460.0,
        anchor='nw', text='три ключа', fill=COLOR_FONT, font=FONT, tags='rus'
        )
    ]

lang_toggle = cls.LanguageToggle(
    master=app.canvas, toggles=['eng', 'rus'], has_translation=True,
    images_idle=['image_language_eng_idle.png', 'image_language_rus_idle.png'],
    images_hover=['image_language_eng_hover.png', 'image_language_rus_hover.png'],
    xpos=760.0, ypos=563.0, width=30.0, height=24.0
    )

radio_noun = cls.RadioButton(
    master=app.canvas,
    xpos=63.0, ypos=213.0, width=24.0, height=24.0,
    toggle_type='word_type', toggle='noun',
    image_idle='image_radio_idle.png',
    image_hover='image_radio_hover.png',
    image_toggled='image_radio_toggled.png',
    image_hover_toggled='image_radio_hover_toggled.png'
    )

radio_verb = cls.RadioButton(
    master=app.canvas,
    xpos=63.0, ypos=263.0, width=24.0, height=24.0,
    toggle_type='word_type', toggle='verb',
    image_idle='image_radio_idle.png',
    image_hover='image_radio_hover.png',
    image_toggled='image_radio_toggled.png',
    image_hover_toggled='image_radio_hover_toggled.png'
    )

radio_anthroponym = cls.RadioButton(
    master=app.canvas,
    xpos=313.0, ypos=213.0, width=24.0, height=24.0,
    toggle_type='word_type', toggle='anthroponym',
    image_idle='image_radio_idle.png',
    image_hover='image_radio_hover.png',
    image_toggled='image_radio_toggled.png',
    image_hover_toggled='image_radio_hover_toggled.png'
    )

radio_toponym = cls.RadioButton(
    master=app.canvas,
    xpos=313.0, ypos=263.0, width=24.0, height=24.0,
    toggle_type='word_type', toggle='toponym',
    image_idle='image_radio_idle.png',
    image_hover='image_radio_hover.png',
    image_toggled='image_radio_toggled.png',
    image_hover_toggled='image_radio_hover_toggled.png'
    )

radio_one_key = cls.RadioButton(
    master=app.canvas,
    xpos=313.0, ypos=363.0, width=24.0, height=24.0,
    toggle_type='num_of_keys', toggle=1,
    image_idle='image_radio_idle.png',
    image_hover='image_radio_hover.png',
    image_toggled='image_radio_toggled.png',
    image_hover_toggled='image_radio_hover_toggled.png'
    )

radio_two_keys = cls.RadioButton(
    master=app.canvas,
    xpos=313.0, ypos=413.0, width=24.0, height=24.0,
    toggle_type='num_of_keys', toggle=2,
    image_idle='image_radio_idle.png',
    image_hover='image_radio_hover.png',
    image_toggled='image_radio_toggled.png',
    image_hover_toggled='image_radio_hover_toggled.png'
    )

radio_three_keys = cls.RadioButton(
    master=app.canvas,
    xpos=313.0, ypos=463.0, width=24.0, height=24.0,
    toggle_type='num_of_keys', toggle=3,
    image_idle='image_radio_idle.png',
    image_hover='image_radio_hover.png',
    image_toggled='image_radio_toggled.png',
    image_hover_toggled='image_radio_hover_toggled.png'
    )

checkbox_prefixes = cls.CheckButton(
    master=app.canvas, toggle_type='prefixes', toggle=None,
    xpos=63, ypos=363, width=24.0, height=24.0,
    image_idle='image_checkbox_idle.png',
    image_hover='image_checkbox_hover.png',
    image_toggled='image_checkbox_toggled.png',
    image_hover_toggled='image_checkbox_hover_toggled.png'
    )

checkbox_suffixes = cls.CheckButton(
    master=app.canvas, toggle_type='suffixes', toggle=None,
    xpos=63, ypos=413, width=24.0, height=24.0,
    image_idle='image_checkbox_idle.png',
    image_hover='image_checkbox_hover.png',
    image_toggled='image_checkbox_toggled.png',
    image_hover_toggled='image_checkbox_hover_toggled.png'
    )

checkbox_endings = cls.CheckButton(
    master=app.canvas, toggle_type='endings', toggle=None,
    xpos=63, ypos=463, width=24.0, height=24.0,
    image_idle='image_checkbox_idle.png',
    image_hover='image_checkbox_hover.png',
    image_toggled='image_checkbox_toggled.png',
    image_hover_toggled='image_checkbox_hover_toggled.png'
    )

field_meaning = tk.Entry(app, bd=0, bg=cf.COLOR_FIELD, fg=cf.COLOR_FONT, font=cf.FONT_INPUT)
field_meaning.place(x=66.0, y=315.0, width=117, height=17, bordermode='ignore')

field_key = tk.Entry(app, bd=0, bg=cf.COLOR_FIELD, fg=cf.COLOR_FONT, font=cf.FONT_INPUT)
field_key.place(x=216.0, y=315.0, width=117, height=17, bordermode='ignore')

output = cls.CustomLabel(app, xpos=380, ypos=200, output=cf.default_output)
output.place()

button_create = cls.TranslatedButton(
    master=app.canvas, has_translation=True,
    images_idle=['image_button_create_eng_idle.png', 'image_button_create_rus_idle.png'],
    images_hover=['image_button_create_eng_hover.png', 'image_button_create_rus_hover.png'],
    xpos=138.0, ypos=525.0, width=125, height=50
    )

button_save = cls.CustomButton(
    master=app.canvas, xpos=760.0, ypos=310.0, width=30, height=30,
    image_idle='image_button_save_idle.png',
    image_hover='image_button_save_hover.png'
    )

button_edit = cls.CustomButton(
    master=app.canvas, xpos=760.0, ypos=260.0, width=30, height=30,
    image_idle='image_button_edit_idle.png',
    image_hover='image_button_edit_hover.png'
    )

button_re_create = cls.CustomButton(
    master=app.canvas, xpos=760.0, ypos=210.0, width=30, height=30,
    image_idle='image_button_re_create_idle.png',
    image_hover='image_button_re_create_hover.png'
    )

button_info = cls.CustomButton(
    master=app.canvas, xpos=760.0, ypos=10.0, width=30, height=30,
    image_idle='image_button_info_idle.png',
    image_hover='image_button_info_hover.png'
    )

button_select_conlang = cls.CustomButton(
    master=app.canvas, xpos=10.0, ypos=10.0, width=30, height=30,
    image_idle='image_button_select_conlang_idle.png',
    image_hover='image_button_select_conlang_hover.png'
    )

cls.set_interface(app.canvas)

app.mainloop()

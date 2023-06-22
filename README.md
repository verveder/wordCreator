# congenCreator / wordCreator 
### (old, but already working) / (new, but in process)

## congenCreator

### WHAT IS IT:

It's a simple Python-based word generator I develop for my conlang (invented language).  
At this stage it can only generate random (and weird) names, but it might turn into a really useful instrument in future.

GUI generated with wonderful [Tkinter Designer](https://github.com/ParthJadhav/Tkinter-Designer.git).

### WHAT IT DOES:

It creates N unique names with N keys joined together 
and shows created names along with the meaning of each key used. Simple!  
Both Numbers are to input with GUI.

A "key" mentioned above is a meaningful word (or even a root, if you want).

You can find some sample words and their RU-translation included 
(words can seem a bit weird, though).

### HOW TO USE congenCreator FOR YOUR OWN LANGS:
- Put a .txt with words you want to use
(only two space separated words per line, conlang first and translation second, i.e.: abracadabra magic)
into src/workfiles directory and name it accordingly to the dictionary you will use in code.
- Create new dictionary with Dictionary class in congen.py, and in gui.py replace 'cg.elven' with your created dictionary.

!!! Make sure that your dictionary.lang_name is equal to .txt name !!!  
!!! You need also to rewrite manually path to your project in the __init__ of Dictionary class !!!  

#### NOTE: 
As there are only 11 words now in .txt included, please DO NOT try to generate 
12+ names with 1 key and 111+ names with 2 keys - obviously, congenCreator crashes.


## wordCreator

### WHAT IS IT:
It's still a simple word "generator" for conlangs, but improved a bit in comparison with older version. 
Main changes: GUI is totally rewrited and project "code" is totally reorganised.

Once mvp is developed, old "Creator" will be removed. 

### WORK IN PROGRESS

#### TO-DO's:
- [X] Place widgets on screen _correctly_
- [X] Define and create additional buttons
- [ ] Start working with what wordCreator does, not what it looks like

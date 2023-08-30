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
- Put into src/workfiles directory a .txt with words you want to use
(only two words, space separated, per line, conlang first and translation second, i.e.: abracadabra magic)
 and name it accordingly to the dictionary you will use in code.
- Create new dictionary with Dictionary class in congen.py, and in gui.py replace 'cg.elven' with your created dictionary.

!!! Make sure that your dictionary.lang_name is equal to .txt name !!!  

#### NOTE: 
As there are only 11 words now in .txt included, please DO NOT try to generate 
12+ names with 1 key and 111+ names with 2 keys - obviously, congenCreator crashes.


## wordCreator
### !!!WORK IN PROGRESS!!!

Once mvp is developed, old "Creator" will be removed. 



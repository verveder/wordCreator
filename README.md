# wordCreator 

### WHAT IS IT:

At this stage it's just a primitive Python-based word generator with GUI, and it can only concatenate word from a word list and show list of meanings that word has.

The default word list is simplified *quenya* dictionary with about 1400 entries 
(and *quenya* is elven language created by Tolkien, in case you somehow managed not to know that).

### HOW TO RUN
1. Clone the repository
2. Enter {HOME}/wordCreator/congenCreator_old/src
3. Run gui.py

### HOW TO USE IT FOR YOUR OWN LANGS:
- Put into src/workfiles directory a .txt with words you want to use and name it accordingly to the dictionary you will use in code.
(NOTE: word and its meaning must be space separated, but meaning can be a whole phrase)
- Create new dictionary with Dictionary class in congen.py, and in gui.py replace 'cg.quenya' with your created dictionary.

!!! Make sure that your dictionary.lang_name is equal to .txt name !!!  

#### WORK IN PROGRESS
#### TRYING TO MAKE SOMETHING GOOD ENOUGH TO BE SHOWN ON GITHUB

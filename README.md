# wordCreator 

### WHAT IS IT:

At this stage it's just a primitive Python-based word generator with GUI, and all it can do - concatenate word from a word list and show list of meanings that new word has.

The default word list is simplified *quenya* dictionary with about 1400 entries on nouns and adjectives
(and *quenya* is elven language created by Tolkien, in case you somehow managed not to know that).

*Note that this dictionary was automatically "cleared" from various symbols so it has some weird entries like "violentind" instead of "violent wind". 
Use it with conscience.*

### HOW TO RUN
1. Clone the repository
2. Enter project's directory
3. Run gui.py

### HOW TO USE IT FOR YOUR OWN LANGS:
- Put into src/workfiles directory a .txt with words you want to use and name it accordingly to the dictionary you will use in code.
(NOTE: word and its meaning must be space separated, but meaning can be a whole phrase)
- Create new dictionary with Dictionary class in congen.py, and in gui.py replace 'cg.quenya' with your created dictionary.

!!! Make sure that your dictionary.lang_name is equal to .txt name !!!  

#### *WORK IN PROGRESS*
#### *ONE DAY THERE WILL BE SOMETHING GOOD ENOUGH TO BE SHOWN ON GITHUB*

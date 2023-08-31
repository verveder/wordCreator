import random
from pathlib import Path

########################################################################

# Dictionaries


class Dictionary:
    """Describes Dictionary in use"""

    def __init__(self, lang_name):
        """Initializes Dictionary"""
        self.lang_name = lang_name
        self.wordbase_path = Path(
            f'{Path.cwd()}\\workfiles\\{self.lang_name}\\{self.lang_name}.txt'
        )
        self.names_dict = {}
        self.keys_conlang = []
        self.keys_rus = []

    def set_wordbase(self):
        """
        Creates {key:value} dict from .txt,
        where key: word in conlang, value: its meaning.
        !!! Word and it's meaning must be separated with space
        """
        with open(self.wordbase_path, encoding='utf-8') as wordbase:
            for line in wordbase:
                key, *value = line.split()
                self.names_dict[key] = ' '.join(value)

            self.keys_conlang = [*self.names_dict.keys()]
            self.keys_rus = [*self.names_dict.values()]


default_lang = Dictionary('quenya')

########################################################################
# Generators


class WordConcatenator:
    """Describes Word Generator"""

    def __init__(self):
        self.generator_type = None
        self.words_output = '- "Keys" field defines how many words to concatenate\n(1 to 3 recommended)\n- "Words" field defines how many words you want to get\n- Current version allows to play only with quenya,\nbut you can set your own word list (see project\'s"Readme")'

    def generate_random(self, dictionary, word):
        """Generates name with random keys"""
        dictionary.set_wordbase()

        keys_num = int(word.keys_num)
        words_num = int(word.words_num)

        new_words = []
        words_list = []

        while words_num > 0:
            random_keys = random.sample(dictionary.keys_conlang, keys_num)
            used_keys = [i for i in random_keys]
            used_keys_eng = []

            for key in used_keys:
                used_keys_eng.append(dictionary.names_dict[key])
            new_word = ''.join(random_keys)

            if new_word not in words_list:
                words_list.append(new_word)
                new_words.append(
                    f"{new_word} (keys: {', '.join(used_keys_eng)})"
                )
                words_num -= 1
            else:
                continue

        self.words_output = '\n'.join(new_words)
        return self.words_output


concatenator = WordConcatenator()

########################################################################
# Words


class Word:
    """Describes settings for name generation"""

    def __init__(self, keys_num, words_num):
        self.keys_num = keys_num
        self.words_num = words_num

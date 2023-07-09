import random
from pathlib import Path
from copy import deepcopy


###############################################################################

# Dictionaries


class Dictionary:
    """Класс, описывающий используемый словарь"""

    def __init__(self, lang_name):
        """Инициализирует параметры словаря"""
        self.lang_name = lang_name
        self.wordbase_path = Path(
            f'{Path.cwd()}\\workfiles\\{self.lang_name}\\{self.lang_name}.txt'
        )

        self.names_dict = {}
        self.keys_conlang = []
        self.keys_rus = []

    def set_wordbase(self):
        """Обрабатывает исходный txt-словарь"""
        with open(self.wordbase_path, encoding='utf-8') as wordbase:
            # Просматриваем текст по строкам
            for line in wordbase:
                # Первое слово - ключ, второе - значение (по пробелу)
                key, *value = line.split()
                # Назначаем каждому ключу его значение (и переводим список в строку)
                self.names_dict[key] = ''.join(value)

            self.keys_conlang = [*self.names_dict.keys()]
            self.keys_rus = [*self.names_dict.values()]


elven = Dictionary('finwe')

###############################################################################
# Generators


class Generator:
    """Класс генераторов"""

    def __init__(self):
        self.generator_type = None
        self.words_output = 'No name here :( \nLet\'s generate something new!'

    def generate_random(self, dictionary, word):
        """Генерирует имя из случайных ключей"""
        dictionary.set_wordbase()

        keys_num = int(word.keys_num)
        names_num = int(word.words_num)

        new_names = []
        names_list = []

        n_count = deepcopy(names_num)

        while n_count > 0:
            # Создаём список из случайных корней в количестве keys_num штук
            random_keys = random.sample(dictionary.keys_conlang, keys_num)
            # Записываем использованные корни в спец. список ключей
            used_keys = [i for i in random_keys]
            # Создаём пустой список для значений использованных корней
            used_keys_rus = []

            # По очереди ищем значения по ключам и добавляем их в список
            for key in used_keys:
                used_keys_rus.append(dictionary.names_dict[key])
            new_name = ''.join(random_keys)
            # Гарантируем отсутствие повторов
            if new_name not in names_list:
                names_list.append(new_name)
                new_names.append(
                    f"{new_name} (ключи: {', '.join(used_keys_rus)})"
                )
                n_count -= 1
            else:
                continue

        self.words_output = '\n'.join(new_names)
        return self.words_output


name_gen = Generator()

###############################################################################
# Words


class Word:
    """Класс, отвечающий за типы слов, доступных к генерации"""

    def __init__(self, keys_num, words_num, word_type='name'):
        self.keys_num = keys_num
        self.words_num = words_num
        self.word_type = word_type

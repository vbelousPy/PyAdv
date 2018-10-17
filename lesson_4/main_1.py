import keyword
import string


class Language:
    _words = list(string.ascii_letters)

    def lexicon(self):
        return self._words


class ProgLanguage(Language):
    _keywords = [1,2,3]

    def lexicon(self):
        return self._keywords


class Python(ProgLanguage):
    _keywords = keyword.kwlist


language = Python()
print(language.lexicon())

prog_lang = ProgLanguage(language)
print(prog_lang.lexicon())
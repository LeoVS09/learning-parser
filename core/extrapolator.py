from core.translator import Translator
import re


class Extrapolator(Translator):
    @classmethod
    def is_letters(self, string):
        for letter in string:
            if not self.is_letter(letter):
                return False
        return True

    letter = "[a-zA-Zа-яА-Я]"

    @classmethod
    def is_letter(self, string):
        return re.match(self.letter, string)

    @classmethod
    def extrapolate_literally(self, string):
        if len(string) == 1 or not self.is_letters(string):
            return "literally \"" + string + "\""
        return "raw \"(" + self.letter + "{" + str(len(string)) + "})\""

    @classmethod
    def extrapolate(self, tree):
        if isinstance(tree, list):
            return self.extrapolate_list(tree)
        if not isinstance(tree, dict):
            return self.extrapolate_literally(tree)
        return self.translate_to_srl(tree)

    @classmethod
    def extrapolate_list(self, list):
        if len(list) == 2 and -1 in list:
            result = ""
            for el in list:
                if el != -1:
                    result += self.extrapolate(el)
            result += " optional"
            return result
        else:
            return self.list_to_srl(list)

    @classmethod
    def branch_to_srl(self, branch):
        result = "( "
        keys = ["begin", "overall", "end"]
        for key in keys:
            el = branch[key]
            if el != -1:
                result += self.extrapolate(el) + ", "
        return result[:-2] + ")"
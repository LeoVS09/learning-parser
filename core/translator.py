from srl import SRL


class Translator:
    @classmethod
    def to_srl(self, tree):
        return self.srl_capture(self.translate_to_srl(tree))

    @classmethod
    def to_reg(self, string):
        return self.translate_to_reg(string)

    @classmethod
    def translate_to_srl(self, tree):
        result = ""
        if isinstance(tree, list):
            result = self.list_to_srl(tree)
        elif isinstance(tree, dict):
            result = self.branch_to_srl(tree)
        else:
            result = "literally \"" + tree + "\""
        return result

    @classmethod
    def list_to_srl(self, list):
        if len(list) == 2 and -1 in list:
            result = ""
        else:
            result = "any of ( "
        for el in list:
            if el != -1:
                result += self.translate_to_srl(el) + ", "
        if len(list) == 2 and -1 in list:
            result = result[:-2] + " optional"
        else:
            result = result[:-2] + " )" + (" optional" if -1 in list else "")
        return result

    @classmethod
    def branch_to_srl(self, branch):
        result = "( "
        keys = ["begin", "overall", "end"]
        for key in keys:
            el = branch[key]
            if el != -1:
                result += self.translate_to_srl(el) + ", "
        return result[:-2] + ")"

    @classmethod
    def srl_capture(self, string):
        string = "capture ( " + string + " )"
        return string

    @classmethod
    def translate_to_reg(self, string):
        return str(SRL(string))
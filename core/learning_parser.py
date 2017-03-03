from core.builder import Builder
from core.translator import Translator
from core.extrapolator import Extrapolator
import re


class LearningParser:

    data = []
    tree = []
    srl = ""
    reg = ""

    def learn(self, strings, literally=True):
        self.data = strings
        self.tree = Builder.tree(self.data)
        print(self.tree)
        if literally:
            self.srl = Translator.to_srl(self.tree)
        else:
            self.srl = Extrapolator.to_srl(self.tree)
        print(self.srl)
        self.reg = Translator.to_reg(self.srl)
        print(self.reg)

    def search(self,string):
        return re.search(self.reg,string)




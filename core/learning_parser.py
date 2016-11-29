from core.builder import builder
from core.translator import translator
from core.extrapolator import extrapolator
import re



class learning_parser:

    data = []
    tree = []
    srl = ""
    reg = ""

    def learn(self, strings, literally=True):
        self.data = strings
        self.tree = builder.tree(self.data)
        print(self.tree)
        if literally:
            self.srl = translator.to_srl(self.tree)
        else:
            self.srl = extrapolator.to_srl(self.tree)
        print(self.srl)
        self.reg = translator.to_reg(self.srl)
        print(self.reg)

    def search(self,string):
        return re.search(self.reg,string)


def test():

    parser = learning_parser()
    parser.learn(["еж", "чет/нед", "неч/нед"])
    print(parser.search("ММСС, пр, Парамонов, чет/нед, ДМ, 4-16н, а.512/1"))
    print(parser.search("Физическая культура, пр, еж, 2-18н, 18н-зачет, спортзал"))
    print(parser.search("ММСС, лаб, Парамонов, неч/нед, 3-17н, а.508/1"))

test()

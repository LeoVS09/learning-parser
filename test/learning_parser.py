from core.learning_parser import LearningParser


def test():

    parser = LearningParser()
    parser.learn(["еж", "чет/нед", "неч/нед"], False)
    print(parser.search("ММСС, пр, Парамонов, чет/нед, ДМ, 4-16н, а.512/1"))
    print(parser.search("Физическая культура, пр, еж, 2-18н, 18н-зачет, спортзал"))
    print(parser.search("ММСС, лаб, Парамонов, неч/нед, 3-17н, а.508/1"))

test()
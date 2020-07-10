
# Class Under Test (CUT)
class PatchClass(object):

    def __init__(self):
        self.attribute_1 = None
        self.__attribute_2 = None

    def m_1(self):
        self.m_2()
        self.m_3()

    def m_2(self):
        print('a')

    def m_3(self):
        print('b')

    def m_4(self):
        self.attribute_1 = 10
        self.__attribute_2 = 20

    def get_attribute_1(self):
        return self.attribute_1

    def get_attribute_2(self):
        return self.__attribute_2

    def __get_attribute_2(self):
        return self.__attribute_2


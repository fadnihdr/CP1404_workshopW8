class ProgrammingLanguage:
    def __init__(self,name,type,reflection,year):
        self.name = name
        self.type = type
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.type == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return ("{}, {} Typing, Reflection = {}, First appeared in {}".format(self.name,self.type,self.reflection,
                                                                              self.year))
from programminglanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


languages = [ruby,python,vb]


for each_lang in languages:
        if each_lang.is_dynamic():
                print(each_lang.name)
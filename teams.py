#imports the library
from dragonfly import (Mimic, Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mouse)

# def foo(slot):
#     t = int(slot)
#     x = .15
#     z = .05
#     y = (t*z)
#     zed = y + x - z
#     return "(0.1, {}), left".format(zed)

# def bar(test):
#     print(test)


class CodeMappings(MappingRule):
    mapping = {  
        'Activity': Key('c-1'),
        'chat': Key('c-2'),
        'Teams': Key('c-3'),
        'Calendar': Key('c-4'),
        'slot 1': Mouse("(0.1, 0.15), left"),  
        'slot 2': Mouse("(0.1, 0.2), left"),  
        'slot 3': Mouse("(0.1, 0.25), left"),  
        'Slot 4': Mouse("(0.1, 0.30), left"),  
        'Slot 5': Mouse("(0.1, 0.35), left"),  
        'Slot 6': Mouse("(0.1, 0.40), left"),  
        'Slot 7': Mouse("(0.1, 0.45), left"),  
        'Slot 8': Mouse("(0.1, 0.50), left"),  
        # 'test <number>': bar("text"),  
    }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("text")
    ]

context = AppContext(executable='Teams')
grammar=Grammar('Teams',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
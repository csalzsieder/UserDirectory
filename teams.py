2#imports the library
from dragonfly import (Function, Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mouse)


def calculateSlotNumber(number):
    startingPoint = .15
    increment = .048
    calculation = (number*increment)
    slotNumber = (startingPoint + calculation) - increment
    Mouse("(0.1, {}), left".format(slotNumber)).execute()


class CodeMappings(MappingRule):
    mapping = {  
        'Slot <number>': Function(calculateSlotNumber),
        'Activity': Key('c-1'),
        'chat': Key('c-2'),
        'Teams': Key('c-3'),
        'Calendar': Key('c-4'),
        'snurch': Key('c-e'),
        'goat': Key('c-g'),
        'Filter': Key('cs-f'),
        '<text>': Text("%(text)s "),
        
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
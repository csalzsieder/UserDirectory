#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mouse, Function)

def calculateSlotNumber(number):
    startingPoint = .35
    increment = .053
    calculation = (number*increment)
    slotNumber = (startingPoint + calculation) - increment
    Mouse("(0.3, {}), left".format(slotNumber)).execute()

class CodeMappings(MappingRule):
    mapping = {
        'Slot <number>': Function(calculateSlotNumber),
		
        }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("text")
    ]

context = AppContext(executable='outlook')
grammar=Grammar('outlook',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
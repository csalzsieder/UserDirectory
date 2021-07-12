#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mouse, Function)

def calculateSlotNumber(number):
    startingPoint = .25
    increment = .07
    calculation = (number*increment)
    slotNumber = (startingPoint + calculation) - increment
    Mouse("(0.3, {}), left".format(slotNumber)).execute()

class CodeMappings(MappingRule):
    mapping = {
        'tab <number>': Function(calculateSlotNumber),
        'new message': Key('c-n'),
        'send items': Key('c-y, down:2, enter'),
		
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
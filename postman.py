#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause)

class CodeMappings(MappingRule):
    mapping = {  
            'run it': Key('c-enter'),
            'x open': Key('c-backslash'),
            'close tab': Key('ca-w'),
            'nexti': Key('cs-]'),
            'previ': Key('cs-['),
            'tab <tab>': Key('c-%(tab)d'),
        }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("text")
    ]

context = AppContext(executable='Postman')
grammar=Grammar('Post man',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
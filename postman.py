#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause)

class CodeMappings(MappingRule):
    mapping = {  
            'send it': Key('c-enter'),
            'sidebar': Key('c-backslash'),
            'line nip': Key('c-slash'),
            'close tab': Key('ca-w'),
            'del line': Key('c-d'),
            'nexti': Key('c-tab'),
            'previ': Key('cs-tab'),
            'Two pain': Key('ca-v'),
            'rename': Key('c-e'),
            'tab <tab>': Key('c-%(tab)d'),
            'save': Key('c-s'),
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
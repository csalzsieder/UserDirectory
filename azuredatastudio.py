#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause)

class CodeMappings(MappingRule):
    mapping = {  
        'previ': Key('c-pgup'),
		'nexty': Key('c-pgdown'),  
        'Run it': Key("f5"),
        'close tab': Key('c-w'),
        'new query': Key('c-n'),
        'line comment': Key("c-k,c-c"),
        'select from': Text("SELECT * FROM")
        }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("text")
    ]

context = AppContext(executable='azuredatastudio')
grammar=Grammar('Azure Data Tools',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
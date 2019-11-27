#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause)

class CodeMappings(MappingRule):
    mapping = {  
		'test code': Text('cd D:GitProjects')
        }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("text")
    ]

context = AppContext(executable=R"C:\Program Files\Git\usr\bin\mintty.exe")
grammar=Grammar('Bash',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
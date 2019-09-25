#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause)

class CodeMappings(MappingRule):
    mapping = {  
        'back space': Key('backspace'),
		'previ': Key('c-pgup'),
		'nexty': Key('c-pgdown'),
		'X open': Key('cs-e'),
		'Text open': Key('cs-g'),
        'line <number>': Key('c-g') + Text('%(number)d') + Key('enter'),
        'get check out develop': Key("c-`,") + Pause("20") + Text("git co develop") + Key("enter"),
        'get check out feature': Key("c-`,") + Pause("20") + Text("git co feature/DF-"),
        'get called release': Key("c-`,") + Text("git cob release/"),
        'get called feature': Key("c-`,") + Text("git cob feature/DF-"),
        'num var': Key("%,(,n,u,m,b,e,r,),d"),
    }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("text")
    ]

context = AppContext(executable='code')
grammar=Grammar('Visual Studio Code',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
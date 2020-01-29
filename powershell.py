#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause)

class CodeMappings(MappingRule):
    mapping = {  
            'dock stat': Text('docker ps -a') + Key('enter'),
            'dock rem': Text('docker rm'),
            'dock redis': Text('docker run --name devredis -p 6379:6379 -d redis') + Key('enter'),
            'redis commander': Text('redis-commander') + Key('enter'),
        }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("text")
    ]

context = AppContext(executable='powershell')
grammar=Grammar('Powershell',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
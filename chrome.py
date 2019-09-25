#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation)  

class GlobalChromeMappings(MappingRule):
    mapping = {
        'close tab': Key('c-w'),
        'open tab': Key('c-t'),
        'duplicate tab': Key('y/25,t'),                  # vimium
        'reopen tab': Key('cs-t'),
        'book snap': Key('cs-b'),
        'book add': Key('c-d'),
        'nexty': Key('c-pgdown'),
        'previ': Key('c-pgup'),
        'tab <tab>': Key('c-%(tab)d'),
        'down <number>': Key('down:%(number)d'),
        'up <number>': Key('up:%(number)d'),
        'down': Key('down'),
        'up': Key('up'),
        'downy': Key('d'),
        'upy': Key('u'),
        'go back': Key('a-left'),
        'go forward': Key('a-right'),
        'reload': Key('f5'),
		'snurch': Key('a-d'),
        'open team city': Key("c-t") + Text("http://teamcity.inspirato.com") + Key("enter"),
        'open bitbucket': Key("c-t") + Text("https://bitbucket.org/dashboard/overview") + Key("enter"),
        'open team city <pascal_text>': Key("c-t") + Text("http://teamcity.inspirato.com/project.html?projectId=%(pascal_text)s") + Key("enter"),
        'Open Jira': Key("c-t") + Text("https://inspirato.atlassian.net/secure/RapidBoard.jspa?rapidView=253") + Key("enter"),
        'Open ticket <number>': Key("c-t") + Text("https://inspirato.atlassian.net/browse/DF-%(number)d") + Key("enter"),
        
    }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 99999),
        Dictation("text"),
        Dictation("pascal_text", default="").title().replace(" ", ""),
    ]

context = AppContext(executable='chrome')
grammar=Grammar('Google Chrome',context=context)
grammar.add_rule(GlobalChromeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
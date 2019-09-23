#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation)

class GlobalChromeMappings(MappingRule):
    mapping = {
        'close tab': Key('c-w'),
		'open new tab': Key('c-t'),
        'duplicate tab': Key('y/25,t'),                  # vimium
        'reopen tab': Key('cs-t'),
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
		'nip': Key('escape'),
        'find <text>': Key("c-f") + Text("%(text)s"),
        'open team city': Key("c-t") + Text("http://teamcity.inspirato.com") + Key("enter"),
        'open team city <pascal_text>': Key("c-t") + Text("http://teamcity.inspirato.com/project.html?projectId=%(pascal_text)s") + Key("enter"),
        'Open JIRA Craig': Key("c-t") + Text("https://inspirato.atlassian.net/secure/RapidBoard.jspa?rapidView=253&assignee=557058%3A17c5d830-0332-4496-a9bd-a99169a75113") + Key("enter"),
    }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
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
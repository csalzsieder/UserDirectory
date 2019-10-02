#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause)

class VisualStudioMappings(MappingRule):
    mapping = {  
        # temp
        'Add navigation': Text('~/Views/Navigation/Header/Navigation'),
        'Add header': Text('~/Views/Navigation/Header'),
        'Add Extension': Text('.cshtml'),

        # Bookmarks
        'book <number>': Key("c-%(number)s"),
        'book <number> snap': Key("cs-%(number)s"),
        'book view': Key("c-`,"),
        
        'Break snap': Key("f9"),
        'Break view': Key("ca-b"),
        'Run it': Key("f5"),
        'snurch': Key("cs-f"),
        'Attach <number>': Key("c-r,c-%(number)s"),
        # 'close all tabs': Key("-"),
        'delete line': Key("s-delete"),
        'Sink dock': Key("c-[,s"),
        'goat': Key("c-t"),
        'Blossom': Key("cs-b"),
        'X open': Key("ca-l"),
        # Debugging
        'step in': Key('f5'),
        'step over': Key('f10'),
        'step out': Key("s-f11"),

        # editing
        'surround with': Key('c-e, c-u'),

        'line <number>': Key("c-g") + Text("%(number)s") + Key("enter,end"),
        'get called <number> <dashtext>': Key("alt,t,n,o") + Text("git cob feature/DF-%(number)s-%(dashtext)s"),
        'get check out develop': Key("alt,t,n,o") + Text("git co develop") + Key("enter"),
        'get check out <nospace>': Key("alt,t,n,o") + Text("git co %(nospace)s/DF-"),
        'get discard': Key("alt,t,n,o") + Text("git checkout -- .") + Key("enter"),
        'get merge continue': Key("alt,t,n,o") + Text("git merge --continue") + Key("enter"),
        'get merge develop': Key("alt,t,n,o") + Text("git merge origin/develop") + Key("enter"),
        'get merge feature': Key("alt,t,n,o") + Text("git merge feature/DF-"),
        'get pull': Key("alt,t,n,o") + Text("git pull") + Key("enter"),
        'get push': Key("alt,t,n,o") + Text("git push") + Key("enter"),
        'get stash [<text>]': Key("alt,t,n,o") + Text("git stash %(text)s") + Key("enter"), #drop/pop
        'get commit <text>': Key("alt,t,n,o") + Text('git commit -am "%(text)s"'),
        'save em': Key("cs-s"),
        'Open solution': Key("cs-o"),
        "Open dry fly": Key("cs-o,a-d") + Text('D:\GitProjects\dryfly\FreeStone\DryFly.sln') + Key('enter'),
        "Open MC API": Key("cs-o,a-d") + Text('D:\GitProjects\marketing-content-api\src\MarketingContent.Api.sln') + Key('enter'),
    }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("text"),
        Dictation("dashtext", default="").lower().replace(" ", "-"),
        Dictation("nospace", default="").lower().replace(" ", ""),
    ]

context = AppContext(executable='devenv')
grammar=Grammar('Visual Studio',context=context)
grammar.add_rule(VisualStudioMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
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
        
        # Navigation
        'snurch': Key("cs-f"),
        'goat death': Key('c-f12'),
        'peak death': Key('a-f12'),
        'view recent': Key('c-comma'),
        'view edits': Key('cs-comma'),
        'line <number>': Key("c-g") + Text("%(number)s") + Key("enter,end"),
        'close all tabs': Key("a-minus")+ Pause('50') + Key('a'),
        'close pinned': Key("a-minus")+ Pause('50') + Key('down:6, enter'),
        'pin tab': Key("a-minus")+ Pause('50') + Key('p'),
        'save them': Key("cs-s"),
        'delete line': Key("s-delete"),
        'Sink dock': Key("c-[,s"),
        'goat': Key("c-t"),
        'X open': Key("ca-l"),

        # Debugging
        'step in': Key('f5'),
        'step over': Key('f10'),
        'step out': Key("s-f11"),
        'Break snap': Key("f9"),
        'Break view': Key("ca-b"),
        'Run it': Key("f5"),
        'Attach <number>': Key("c-r,c-%(number)s"),
        'watch <number>': Key('ca-w,%(number)s'),
        'tests run': Key('c-r,c-t'),
        'test debug': Key('c-u,c-d'),
        'Blossom': Key("cs-b"),
        'blessed load': Key("cs-b") + Pause('800') + Key('w-4') + Pause('50') + Key('c-1,f5') + Pause('50') + Key('w-6'),
        'Load web': Key('w-4') + Pause('50') + Key('c-1,f5') + Pause('50') + Key('w-6'),

        # editing
        'Blossom': Key("cs-b"),
        'blessed load': Key("cs-b") + Pause('800') + Key('w-4') + Pause('50') + Key('c-1,f5') + Pause('50') + Key('w-6'),
        'Load web': Key('w-4') + Pause('50') + Key('c-1,f5') + Pause('50') + Key('w-6'),
        'surround with': Key('c-e, c-u'),
        'line comment': Key('c-k,c-c'),
        'line uncomment': Key('c-k,c-u'),
        'add class': Key('ca-insert,enter'),
        
        # git 
        'get called <number> <dashtext>': Key("alt,t,n,o") + Text("git cob feature/DF-%(number)s-%(dashtext)s"),
        'get check out develop': Key("alt,t,n,o") + Text("git co develop") + Key("enter"),
        'get check out <nospace>': Key("alt,t,n,o") + Text("git co %(nospace)s/DF-"),
        'get discard': Key("alt,t,n,o") + Text("git checkout -- .") + Key("enter"),
        'get merge <text>': Key("alt,t,n,o") + Text("git merge --%(text)s") + Key("enter"), #Abort, merge
        'get merge develop': Key("alt,t,n,o") + Text("git merge origin/develop") + Key("enter"),
        'get merge feature': Key("alt,t,n,o") + Text("git merge feature/DF-"),
        'get pull': Key("alt,t,n,o") + Text("git pull") + Key("enter"),
        'get push': Key("alt,t,n,o") + Text("git push") + Key("enter"),
        'get stash [<text>]': Key("alt,t,n,o") + Text("git stash %(text)s") + Key("enter"), #drop/pop
        'get commit': Key("alt,t,n,o") + Text('git commit -am ""') + Key("left"),

        # Snippets
        'Open snippets': Key('c-k,c-b'),
        'prop snip': Text('prop') + Key('tab'),
        'See tour snip': Text('ctor') + Key('tab'),

        # Opening solutions
        'Open solution': Key("cs-o"),
        "Open dry fly": Key("cs-o,a-d") + Text('D:\GitProjects\dryfly\FreeStone\DryFly.sln') + Key('enter'),
        "Open MC API": Key("cs-o,a-d") + Text('D:\GitProjects\marketing-content-api\src\MarketingContent.Api.sln') + Key('enter'),
    }
    extras=[
        Integer('tab', 1, 10),
        Integer('number', 0, 9999),
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
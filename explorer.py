from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause)

class IERule(MappingRule):
    pronunciation = "explorer"

    mapping = {
        "address bar": Key("a-d"),
        "new folder": Key("cs-n"),
        "new file": Key("a-f, w, t"),
        "(show | file | folder) properties": Key("a-enter"),
        "go up": Key("a-up"),
        "go back": Key("a-left"),
        "go forward": Key("a-right"),
        "snurch [<text>]": Key("a-d, tab:1") + Text("%(text)s"),
        "(navigation | nav | left) pane": Key("a-d, tab:2"),
        "(center pane | (file | folder) (pane | list))": Key("a-d, tab:3"),
            # for the sort command below,
            # once you've selected the relevant heading for sorting using the arrow keys, press enter
        "sort [headings]": Key("a-d, tab:4"),
        "Open dry fly": Key("a-d") + Text('D:\GitProjects\dryfly\FreeStone\DryFly.sln') + Key('enter'),
        "Open MC API": Key("a-d") + Text('D:\GitProjects\marketing-content-api\src\MarketingContent.Api.sln') + Key('enter'),
        "Open Macro system": Key("a-d") + Text('C:\NatLink\NatLink\MacroSystem') + Key('enter') + Pause('50') + Key('tab:9, down:2, shift:down, end, shift:up,c-c,a-d') + Text('C:\NatLink\UserDirectory') + Key('enter') + Pause('50') + Key('enter, tab:9'),
        "Open User directory": Key("a-d") + Text('C:\NatLink\UserDirectory') + Key('enter'),
        "code <dashtext> ": Key("a-d") + Text('D:\GitProjects\%(dashtext)s') + Key('enter'),

    }
    extras = [
        Dictation("text"),
        Integer("n", 1, 1000),
        Dictation("dashtext", default="").lower().replace(" ", "-"),
    ]
    defaults = {"n": 1}


context = AppContext(executable="explorer")
grammar=Grammar('Explorer',context=context)
grammar.add_rule(IERule())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
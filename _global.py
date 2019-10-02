#imports the library

from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause)

class GlobalMappings(MappingRule):
    mapping = {  
		'find [<text>]': Key("c-f") + Pause("10") + Text("%(text)s"),
        'back space': Key('backspace'),
        'nip': Key('escape'),
        'snap': Key('a-tab'),
        'snap hold': Key('alt:down, tab'),
        'pick': Key('enter,alt:up'),
        'slap': Key('c-tab'),
        'down': Key('down'),
        'down <number>': Key('down:%(number)d'),
        'up': Key('up'),
        'up <number>': Key('up:%(number)d'),
        'ut': Key("pgup"),
        'dut': Key("pgdown"),
        'left [<number>]': Key('left:%(number)d'),
        'left <number> word': Key("ctrl:down, left:%(number)d, ctrl:up"),
        'right [<number>]': Key('right:%(number)d'),
        'right <number> word': Key("ctrl:down, right:%(number)d, ctrl:up"),
        "camel [under] <camel_text>": Text("%(under)s%(camel_text)s"),
        "snake [<under>] <snaketext>": Text("%(under)s%(snaketext)s"),
        "dash [<dash>] <dashtext>": Text("%(dash)s%(dashtext)s"),
        "paschal [<pascaltext>]": Text("%(pascaltext)s"),
        "title [<titletext>]": Text("%(titletext)s"),
        'select down <number>': Key("home, shift:down, down:%(number)d, up, end, shift:up"),
        'select up <number>': Key("end, shift:down, up:%(number)d, down, home, shift:up"),
        'select right <number>': Key("ctrl:down, shift:down, right:%(number)d, ctrl:up, shift:up"),
        'select left <number>': Key("ctrl:down, shift:down, left:%(number)d, ctrl:up, shift:up"),
        'line end [<number>]': Key("end") + Key("left:%(number)d"),
        'line home [<number>]': Key("home") + Key("right:%(number)d"),
        'undo [<number>]': Key("c-z:%(number)d"),
        'redo [<number>]': Key("c-y:%(number)d"),
        'to files': Key("w-1"),
        'to Outlook': Key("w-2"),
        'to Teams': Key("w-3"),
        'to Web': Key("w-4"),
        'to pie': Key("w-5") + Pause('50') + Key("enter"),
        'to code': Key("win:down, 5, 5, win:up") + Pause('50') + Key("enter"),
        'to stud': Key("w-6"),
        'to pre': Key("w-7"),
        'to notepad': Key("w-8"),
        'to dragon': Key("w-9"),
        'flag it': Key("enter") + Text("//ToDo: DF-10303 remove unused fields, delete later") + Key("down,c-k,c-c"),
        'craig pass': Text("conec#20"),
        }

    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("camel_text", default="").camel(),
        # Define a Dictation element that produces snake case text,
        # e.g. hello_world.
        Dictation("snaketext", default="").lower().replace(" ", "_"),
        Dictation("dashtext", default="").lower().replace(" ", "-"),
        # Define a Dictation element that produces text matching Python's
        # class casing, e.g. DictationContainer.
        Dictation("pascaltext", default="").title().replace(" ", ""),
        Dictation("titletext", default="").title().replace(" ", " "),
        # Allow adding underscores before cased text.
        Choice("under", {"under": "_"}, default=""),
        Choice("dash", {"dash": "-"}, default=""),
        Dictation("text")
    ]

grammar=Grammar('Global')
grammar.add_rule(GlobalMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
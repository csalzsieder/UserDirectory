#imports the library
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause)

class CodeMappings(MappingRule):
    mapping = {
		'find <text>': Key("c-f") + Text("%(text)s"),
        'back space': Key('backspace'),
		'previ': Key('c-pgup'),
		'nexty': Key('c-pgdown'),
		'X open': Key('cs-e'),
		'Text open': Key('cs-g'),
        'down <number>': Key('down:%(number)d'),
        'up <number>': Key('up:%(number)d'),
        'left <number>': Key('left:%(number)d'),
        'right <number>': Key('right:%(number)d'),
        'line <number>': Key('c-g') + Text('%(number)d') + Key('enter'),
        "camel <camel_text>": Text("%(camel_text)s"),
        "snake [<under>] <snaketext>": Text("%(under)s%(snaketext)s"),
        "dash [<dash>] <dashtext>": Text("%(dash)s%(dashtext)s"),
        "paschal [<pascaltext>]": Text("%(pascaltext)s"),
        "title [<titletext>]": Text("%(titletext)s"),
        'copy down <number>': Key("home, shift:down, down:%(number)d, up, end, shift:up"),
        'copy up <number>': Key("end, shift:down, up:%(number)d, down, home, shift:up"),
        'get check out develop': Key("c-`,") + Pause("20") + Text("git co develop") + Key("enter"),
        'get check out feature': Key("c-`,") + Pause("20") + Text("git co feature/DF-"),
        'get called release': Key("c-`,") + Text("git cob release/"),
        'get called feature': Key("c-`,") + Text("git cob feature/DF-"),
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

context = AppContext(executable='code')
grammar=Grammar('Visual Studio Code',context=context)
grammar.add_rule(CodeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
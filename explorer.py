from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mimic)

class IERule(MappingRule):
    pronunciation = "explorer"

    mapping = {
        "address bar": Key("a-d"),
        "copy path": Key("a-d,c-c"),
        "new folder": Key("cs-n"),
        "new file": Key("a-f, w, t"),
        "(show | file | folder) properties": Key("a-enter"),
        "go up": Key("a-up"),
        "go back": Key("a-left"),
        "go forward": Key("a-right"),
        "snurch [<text>]": Key("a-d, tab:1") + Text("%(text)s"),
        "(navigation | nav | left) pane": Key("a-d, tab:2"),
        "(center pane | (file | folder) (pane | list))": Key("a-d, tab:3"),
        "sort [headings]": Key("a-d, tab:4"),


        # code - bricks
        'zap': Key('c-slash'), 
        'run me': Key('c-enter'), 
        'run it': Key('s-enter'), 
        'run up': Key('sa-up'), 
        'run down': Key('sa-down'), 
        'run all': Key('sa-enter'), 
        'nexty': Key('c-pgdown'),
        'previ': Key('c-pgup'),
        'insert up': Key('ca-p'),
        'insert down': Key('ca-n'),
        'insert display': Key('ca-p') + Pause('100') + Text('display('),
        'split cell': Key('ca-n'),
        'copy cell': Key('ca-c'),
        'cut cell': Key('ca-x'),
        'del cell': Key('ca-d'),
        'del line': Key('s-delete'),
        'cell down': Key('ca-down'),
        'indent me': Key('c-]'),
        'dedent me': Key('c-['),
        'find me': Key('ca-f'),
        'paste wheel': Text('dbfs:/FileStore/jars/passlist-1.0.0-py3-none-any.whl'),
        'print count': Text('print(df.count())'),


        'frame it': Text('df.'),


        "goat dry fly": Key("a-d") + Text(R'D:\GitProjects\dryfly\FreeStone') + Key('enter'),
        "goat code": Key("a-d") + Text(R'D:\GitProjects') + Key('enter'),
        "goat me bin": Key("a-d") + Text(R'C:\Users\csalzsieder\.nuget\packages\passlist.businesslogic\1.1.4.16\lib\netcoreapp2.1') + Key('enter'),
        "goat biz bin": Key("a-d") + Text(R'D:\GitProjects\passlist-business\PassList.BusinessLogic\bin\Debug\netcoreapp2.1') + Key('enter'),
        "goat biz": Key("a-d") + Text(R'D:\GitProjects\passlist-business\PassList.BusinessLogic') + Key('enter'),
        "goat build": Key("a-d") + Text(R'D:\GitProjects\passlist-build\PassList.Functions\RebuildOfferings') + Key('enter'),
        "goat end bin": Key("a-d") + Text(R'D:\GitProjects\passlist-endpoints\PassList.Functions\OfferingFilters\bin\Debug\netcoreapp2.1\bin') + Key('enter'),
        "goat end": Key("a-d") + Text(R'D:\GitProjects\passlist-endpoints\PassList.Functions') + Key('enter'),
        "goat react": Key("a-d") + Text(R"D:\GitProjects\react-components") + Key('enter'),
        "goat grammer": Key("a-d") + Text(R"C:\NatLink\NatLink\MacroSystem") + Key('enter'),
        "goat grammer repo": Key("a-d") + Text(R"C:\NatLink\UserDirectory") + Key('enter'),

        "Open MC API": Key("a-d") + Text(R'D:\GitProjects\marketing-content-api\src\MarketingContent.Api.sln') + Key('enter'),
        "Open pass": Key("a-d") + Text(R'D:\GitProjects\offering-list\OfferingList.sln') + Key('enter'),
        "Open QA": Key("c-t") + Text(R'https://adb-1477701841953214.14.azuredatabricks.net/?o=1477701841953214') + Key('enter'),
        
        

        # "copy grammers": Key("a-d") + Text(R'C:\NatLink\NatLink\MacroSystem') + Key('enter') + Pause('50') + Key('tab:9, down:2, shift:down, end, shift:up,c-c,a-d') + Text('C:\NatLink\UserDirectory') + Key('enter') + Pause('50') + Key('enter, tab:9,c-v') + Pause('50') + Key('enter'),
        "Test mimic" : Mimic

    }
    extras = [
        Dictation("text").lower(),
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
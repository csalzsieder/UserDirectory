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
        'load': Key('f5'),
        'snap title': Key('t'), 
        'snap result': Key('o'),  
        'to fetch': Text(R' = DeltaTable.forName(spark, "").toDF()') + Key("left:9"), 
        'to read': Text(R' = spark.table("")') + Key("left:2"), 


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
        'copy cell': Key('c-c'),
        'cut cell': Key('c-x'),
        'del cell': Key('ca-d'),
        'del line': Key('s-delete'),
        'cell down': Key('ca-down'),
        'indent me': Key('c-]'),
        'dedent me': Key('c-['),
        'find me': Key('ca-f'),
        'paste wheel': Text('dbfs:/FileStore/jars/passlist-1.0.0-py3-none-any.whl'),
        'print count': Text('print(df.count())'),
        'F call': Text('F.col("")') + Key('left:2'),

        'insert cell': Key('c-m,b'), 
        'frame it': Text('df.'),
        "goat dry fly": Key("a-d") + Text(R'D:\GitProjects\dryfly\FreeStone') + Key('enter'),

       

        "Open data": Key("c-t") + Text(R'https://adb-8131518869320383.3.azuredatabricks.net/explore/data/hive_metastore/default?o=8131518869320383') + Key('enter'),
        "Open workflow": Key("c-t") + Text(R'https://adb-8131518869320383.3.azuredatabricks.net/?o=8131518869320383#job/list') + Key('enter'),
        "Open recent": Key("c-t") + Text(R'https://adb-8131518869320383.3.azuredatabricks.net/recents?o=8131518869320383') + Key('enter'),
        "Open data": Key("c-t") + Text(R'https://adb-8131518869320383.3.azuredatabricks.net/explore/data?o=8131518869320383') + Key('enter'),
        "open Yan": Key("c-t") + Text(R'https://adb-1477701841953214.14.azuredatabricks.net/browse/folders/2359562396776343?o=1477701841953214') + Key('enter'),
        # "Open data": Key("c-t") + Text(R'') + Key('enter'),
        # "Open data": Key("c-t") + Text(R'') + Key('enter'),
        # "Open data": Key("c-t") + Text(R'') + Key('enter'),
        # "Open data": Key("c-t") + Text(R'') + Key('enter'),

        
        

        # "copy grammers": Key("a-d") + Text(R'C:\NatLink\NatLink\MacroSystem') + Key('enter') + Pause('50') + Key('tab:9, down:2, shift:down, end, shift:up,c-c,a-d') + Text('C:\NatLink\UserDirectory') + Key('enter') + Pause('50') + Key('enter, tab:9,c-v') + Pause('50') + Key('enter'),
        "Test mimic" : Mimic

    }
    extras = [
        Dictation("text").lower(),
        Integer("n", 1, 1000),
        Dictation("dashtext", default="").lower().replace(" ", "-"),

    ]
    defaults = {"n": 1}


context = AppContext(executable="firefox")
grammar=Grammar('Firefox',context=context)
grammar.add_rule(IERule())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
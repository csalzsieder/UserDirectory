from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Pause)  
  

class GlobalChromeMappings(MappingRule):
    mapping = {
        'close tab': Key('c-w'),
        # 'open tab': Key('c-t') + Pause('30') + Key('f,enter') + Pause('150') + Key('cs-.'),
        'open tab': Key('c-t') + Pause('30') + Text('foo') + Key('enter') + Pause('150') + Key('cs-.'),
        'restore tab': Key('cs-t'),
        'duplicate tab': Key('y/25,t'),                  # vimium
        'book snap': Key('cs-b'),
        'book add': Key('c-d'),
        'nexty': Key('c-tab'),
        'previ': Key('cs-tab'),
        'tab <tab>': Key('c-%(tab)d'),
        'down <number>': Key('down:%(number)d'),
        'up <number>': Key('up:%(number)d'),
        'down': Key('down'),
        'up': Key('up'),
        'downy': Key('d'),
        'upy': Key('u'),
        'go back': Key('a-left'),
        'go forward': Key('a-right'),
        'load': Key('f5'),
		# 'open tab': Key('a-d') + Pause('10') + Text('https://www.google.com') + Key('enter') + Pause('30') + Key('cs-.'),
		'snurch': Key('cs-.'),
		'pie snurch': Key('a-d') + Pause('20') + Text('python pyspark '),
		'goat bar': Key('a-d'),
		'run it': Key('s-enter'),

        # Common websites
        'Open tech docs': Key("c-t") + Text(R"https://docs.google.com/document/d/1XVYzcH_kkqa6Wr13Z654RdRuJ1j0mVRVMgU8_XSiTx0/edit") + Key("enter"),
        'Open commander': Key("c-t") + Text("http://127.0.0.1:8081") + Key("enter"),
        'Open pluralsight': Key("c-t") + Text("https://app.pluralsight.com/library/") + Key("enter"),
        'Open fly docs': Key("c-t") + Text("https://pythonhosted.org/dragonfly/actions.html#key-names") + Key("enter"),
        'open octo': Key("c-t") + Text("https://octo.inspirato.com:8000/app") + Key("enter"),
        'Open Jira': Key("c-t") + Text("https://inspirato.atlassian.net/jira/software/c/projects/DP/boards/341") + Key("enter"),
        'Open wiki': Key("c-t") + Text("https://inspirato.atlassian.net/wiki/spaces/DP/overview") + Key("enter"),
        'Open Gmail': Key("c-t") + Text("https://mail.google.com/mail/u/0/#inbox") + Key("enter"),
        'Open load test': Key("c-t") + Text("https://app.k6.io/projects/3490751") + Key("enter"),
        'open notes': Key("c-t") + Text("https://docs.google.com/document/d/1UpkG04_QhrmELH0qUvN0CCuXheeoAZqq4Ij0ZJvl6ag/edit") + Key("enter"),
        'open lake': Key("c-t") + Text(R"https://portal.azure.com/#blade/Microsoft_Azure_Storage/ContainerMenuBlade/overview/storageAccountId/%2Fsubscriptions%2Fc22e7019-2735-41cf-8a4d-3a887aa2cbac%2FresourceGroups%2Frg-datapipelines-sb%2Fproviders%2FMicrosoft.Storage%2FstorageAccounts%2Fdlsdatapipelinessb/path/passlist/etag/%220x8D86AF6914772FD%22/defaultEncryptionScope/%24account-encryption-key/denyEncryptionScopeOverride//defaultId//publicAccessVal/None") + Key("enter"),
        'open sumo': Key("c-t") + Text(R"https://inspirato.us2.sumologic.com/ui/#/search/cea32bc6_2883_5d31_582c_1b141cf2c6da") + Key("enter"),
        'open astro cert': Key("c-t") + Text(R"https://academy.astronomer.io/astronomer-certification-apache-airflow-dag-authoring-preparation") + Key("enter"),
        'open astro': Key("c-t") + Text(R"https://cloud.astronomer.io/clctnq05z758897e3dbt8ku9um/deployments") + Key("enter"),
        'Open build': Key("c-t") + Pause('20') + Text(R"https://dev.azure.com/inspirato-dev/Data%20Platform/_build") + Key("enter"),
        'Open medium': Key("c-t") + Pause('20') + Text(R"https://medium.com/") + Key("enter"),
        'Open docs': Key("c-t") + Pause('20') + Text(R"https://docs.google.com/document/u/0/") + Key("enter"),
        'Open Kafka': Key("c-t") + Pause('20') + Text(R"https://confluent.cloud/login/sso/c1ca1d2f-2be1-404a-bf9c-dd27848f2602") + Key("enter"),
        'Open airflow': Key("c-t") + Pause('20') + Text(R"https://cloud.astronomer.io/clctnq05z758897e3dbt8ku9um/deployments") + Key("enter"),
        'Open Jeannie': Key("c-t") + Pause('20') + Text(R"https://inspirato.app.opsgenie.com/alert/list") + Key("enter"),
        'Open mail': Key("c-t") + Pause('20') + Text(R"https://outlook.office.com/mail/") + Key("enter"),
        'Open bee': Key("c-t") + Pause('20') + Text(R"https://app.linearb.io/pulse?iteration_id=2184542677&teams=9769") + Key("enter"),
        'Open todo': Key("c-t") + Pause('20') + Text(R"https://docs.google.com/document/d/1q8Ix0XktV6SY-6HcMkUvGX5PjE1zy7k-5_7PMU34Q4k/edit") + Key("enter"),
        'Open Uni': Key("c-t") + Pause('20') + Text(R"https://www.udemy.com/home/my-courses/learning/") + Key("enter"),
        'Open chat': Key("c-t") + Pause('20') + Text(R"https://chatgpt.com/") + Key("enter"),
        'Open drive': Key("c-t") + Pause('20') + Text(R"https://drive.google.com/drive/https://chatgpt.com/u/0/my-drive") + Key("enter"),
        'Open web drive': Key("c-t") + Pause('20') + Text(R"https://navigee-my.sharepoint.com/personal/csalzsieder_inspirato_com/_layouts/15/onedrive.aspx?view=1") + Key("enter"),
        'Open plan': Key("c-t") + Pause('20') + Text(R"https://inspirato.atlassian.net/jira/plans/3/scenarios/3/timeline?vid=12") + Key("enter"), 
        'Open epics': Key("c-t") + Pause('20') + Text(R"https://inspirato.atlassian.net/jira/software/c/projects/DP/boards/341/timeline") + Key("enter"), 
        'Open bard': Key("c-t") + Pause('20') + Text(R"https://bard.google.com/chat") + Key("enter"), 
        "Open workflow": Key("c-t") + Text(R'https://adb-8131518869320383.3.azuredatabricks.net/?o=8131518869320383#job/list') + Key('enter'),
        "Open recent": Key("c-t") + Text(R'https://adb-8131518869320383.3.azuredatabricks.net/recents?o=8131518869320383') + Key('enter'),
        "Open data": Key("c-t") + Text(R'https://adb-8131518869320383.3.azuredatabricks.net/explore/data?o=8131518869320383') + Key('enter'),
        'Open standup': Key("c-t") + Pause('20') + Text(R"https://docs.google.com/document/d/17_MgBmkjFZvwkh0kwv7mQNkM5K8L_4XyCiuWtesLcqI/edit") + Key("enter"), 
        'Open course': Key("c-t") + Pause('20') + Text(R"https://www.udemy.com/course/llm-mastery-chatgpt-gemini-claude-llama3-openai-apis/learn/lecture/44120358?start=0#overview") + Key("enter"), 
        # 'Open bee': Key("c-t") + Pause('20') + Text(R"") + Key("enter"), 
        # 'Open bee': Key("c-t") + Pause('20') + Text(R"") + Key("enter"), 
        # 'Open bee': Key("c-t") + Pause('20') + Text(R"") + Key("enter"), 

        #azure
        'Open Azure': Key("c-t") + Text(R'https://portal.azure.com/#blade/HubsExtension/RecentResources.ReactView') + Key("enter"),
        'Open pie spark': Key("c-t") + Text(R'https://spark.apache.org/docs/latest/api/python/index.') + Key("enter"),
        
        # Bit bucket
        'open git': Key("c-t") + Text("https://github.com/Inspirato/data-platform") + Key("enter"),
        # 'open bit data': Key("c-t") + Text("https://bitbucket.org/inspirato/data-platform/src/main/") + Key("enter"),
        
        'Open grammer chat': Key("c-t") + Text("https://gitter.im/dictation-toolbox/dragonfly?source=orgpage") + Key("enter"),
        'Open ticket <number>': Key("c-t") + Text("https://inspirato.atlassian.net/browse/DF-%(number)d") + Key("enter"),
        'Open trunk': Key("c-t") + Text("https://dryfly-trunk.dev.inspirato.com") + Key("enter"),
        # 'Open JS snippets': Key("c-t") + Text("https://marketplace.visualstudio.com/items?itemName=xabikos.JavaScriptSnippets") + Key("enter"),

        # Jira
        'open ticket': Key("c-t") + Text("https://inspirato.atlassian.net/browse/DP-115") + Key("enter") + Pause('300') + Key('.') + Pause('100') + Text('clone') + Key('enter') + Pause('50') + Key('s-home'),
        'open task': Key("c-t") + Text("https://inspirato.atlassian.net/secure/CloneIssueDetails!default.jspa?id=191596") + Key("enter"),
        # coding
        # 'open snippets': Key("c-t") + Text("https://docs.microsoft.com/en-us/visualstudio/ide/visual-csharp-code-snippets?view=vs-2019") + Key("enter"),

        # Web console
        'open debugger': Key('f12'),
        'goat': Key('cs-.'),
        # 'run it': Key('f8'), 
        'step over': Key('s-f11'),                      
        'step in': Key('f11'),
        'step out': Key('f10'),
        'elements tab': Key('c-1'),
        'Consol tab': Key('c-2'),
        'sources tab': Key('c-3'),
        'network tab': Key('c-4'),
        'performance tab': Key('c-5'),
        'line <number>': Key('c-g') + Text('%(number)d') + Key('enter'),
        'break snap': Key('c-f8'),
        'inspect': Key('cs-c'),

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

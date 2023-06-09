from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Pause)  
  

class GlobalChromeMappings(MappingRule):
    mapping = {
        'close tab': Key('c-w'),
        # 'open tab': Key('c-t') + Pause('30') + Key('f,enter') + Pause('150') + Key('cs-.'),
        'open tab': Key('c-t') + Pause('30') + Key('tab:4') + Key('cs-.'),
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
        'Open zoom': Key("c-t") + Text(R"https://zoom.us/j/6516749931") + Key("enter"),
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
        'Open build': Key("c-t") + Pause('20') + Text("https://dev.azure.com/inspirato-dev/Data%20Platform/_build") + Key("enter"),
        'Open medium': Key("c-t") + Pause('20') + Text(R"https://medium.com/") + Key("enter"),
        'Open docs': Key("c-t") + Pause('20') + Text(R"https://docs.google.com/document/u/0/") + Key("enter"),
        'Open bigeye': Key("c-t") + Pause('20') + Text(R"https://app.bigeye.com/preview/catalog/schema/22999/tables") + Key("enter"),
        'Open Kafka': Key("c-t") + Pause('20') + Text(R"https://confluent.cloud/login/sso/c1ca1d2f-2be1-404a-bf9c-dd27848f2602") + Key("enter"),
        'Open airflow': Key("c-t") + Pause('20') + Text(R"https://cloud.astronomer.io/clctnq05z758897e3dbt8ku9um/deployments") + Key("enter"),
        'Open Jeannie': Key("c-t") + Pause('20') + Text(R"https://inspirato.app.opsgenie.com/alert/list") + Key("enter"),
        'Open mail': Key("c-t") + Pause('20') + Text(R"https://outlook.office.com/mail/") + Key("enter"),
        'Open bee': Key("c-t") + Pause('20') + Text(R"https://app.linearb.io/pulse?iteration_id=2184542677&teams=9769") + Key("enter"),
        'Open todo': Key("c-t") + Pause('20') + Text(R"https://docs.google.com/document/d/1q8Ix0XktV6SY-6HcMkUvGX5PjE1zy7k-5_7PMU34Q4k/edit") + Key("enter"),
        'Open elation': Key("c-t") + Pause('20') + Text(R"https://inspirato.alationcloud.com/") + Key("enter"),
        'Open Uni': Key("c-t") + Pause('20') + Text(R"https://www.udemy.com/") + Key("enter"),
        'Open chat': Key("c-t") + Pause('20') + Text(R"https://chat.openai.com/chat") + Key("enter"),
        'Open drive': Key("c-t") + Pause('20') + Text(R"https://drive.google.com/drive/u/0/my-drive") + Key("enter"),
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

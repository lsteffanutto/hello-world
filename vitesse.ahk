^²:: ; ecrit le code ci-dessous en faisant "ctrl+²", (";" de cette ligne permet de commenter). Quand ce script est édité, ne pas oublier de le run (+ éventuellement faire un script qui le run quand l'ordi démarre)
Send, mdp
return

^&:: ; ouvre le terminal en faisant "ctrl+&"
Run, C:\windows\system32\cmd.exe
return

^é:: ; Visual Studio Code
Run, C:\Program Files\CodeBlocks\codeblocks.exe
return

^":: ; Capture ecran
Run, %windir%\system32\SnippingTool.exe
return

^':: ; mail
Send, mail

^<:: ; user : elastic, mdp_elastic : ça
Send, mdp
return

^(:: ; nom repo es
Send, .\elasticsearch-8.6.1
return

^-::
Send, curl --insecure --cacert .\elasticsearch-8.6.1\config\certs\http_ca.crt -u elastic:ndCm=tHD4nh5rVxMGHjR "https://localhost:9200/"
return

^è::
Send, .\logstash-8.6.1\bin\logstash.bat -f .\config\logstash_csv.conf
return

^q::
Send, exit()
return

^e::
Run, C:\Users\lsteffanutto-admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Anaconda Prompt (anaconda3)
return

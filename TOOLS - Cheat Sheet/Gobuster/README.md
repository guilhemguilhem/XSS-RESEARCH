For path, subdomains... enumeration 

```bash
gobuster vhost -w ~/SecLists/Discovery/Web-Content/combined_directories.txt -u http://dev.stocker.htb/stock -t 50 --append-domain
```
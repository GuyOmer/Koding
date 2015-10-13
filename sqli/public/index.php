<?php

require("../includes/config.php");
if ($_SERVER["REQUEST_METHOD"] == "POST")
{
    
    $sql = "SELECT * FROM `users` WHERE `username`=\"". $_POST['username']."\"";
    echo $sql;
    $result = queryi($sql);
    dump($result);
}
else
{
    render("../templates/sqli.php");
    exit;
}
?>
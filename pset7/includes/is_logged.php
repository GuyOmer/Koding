<?php

    function islogged() 
    {
        if(session_status() === PHP_SESSION_ACTIVE)
            return;
        
        redirect("login.php");
    }

?>

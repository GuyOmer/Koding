<?php

    // configuration
    require("../includes/config.php");

    // if form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        //verify inputs
        if(empty($_POST["username"]))
        {
            apologize("You must provide a username.");
            exit;
        }
        if(empty($_POST["password"]))
        {
            apologize("You must provide a password.");
            exit;
        }
        if($_POST["password"] != $_POST["confirmation"])
        {
            apologize("Passwords don't match.");
            exit;
        }
            
        $result = query("INSERT INTO users (username,hash,cash) VALUES(?,?,10000.0000)",
                  $_POST["username"], crypt($_POST["password"]));
                  
        if($result === false)
        {
            apologize("Error, probably username already exsits. Try again.");
            exit;
        }
        
        $rows = query("SELECT LAST_INSERT_ID() AS id");
        $id = $rows[0]["id"];
        $_SESSION["id"] = $id;
        redirect("index.php");
        
    }
    else
    {
        // else render form
        render("register_form.php", ["title" => "Register"]);
    }

?>

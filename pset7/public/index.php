<?php

    // configuration
    require("../includes/config.php"); 

    if(!isset($_SESSION["id"]))
    {
        logout();
        redirect("login.php");
    }
    
    
    //symbol, shares
    $stocks = query("SELECT * FROM stocks WHERE id=?",$_SESSION['id']);
    
    //name, price
    foreach($stocks as &$stock)
    {
        $result = lookup($stock["symbol"]);
        $stock["name"] = $result["name"];
        $stock["price"] = $result["price"];
    }
    
    //cash
    $cash = query("SELECT cash FROM users WHERE id=?",$_SESSION['id']);
    
    // render portfolio
    render("portfolio.php", ["title" => "Portfolio","data" => $stocks, "cash" =>$cash[0]["cash"]]);

?>

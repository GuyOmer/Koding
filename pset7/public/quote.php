<?php
    // configuration
    require("../includes/config.php");
    
    //nothing inputted
    if(!isset($_GET["symbol"]))
    {
        //show quote_search.php
        render("quote_search.php", ["title" => "Quote"]);
        exit;
    }
    
    if($result = lookup($_GET["symbol"]))
    {
        render("quote_result.php",["title" => "Quote", "symbol" => strtoupper($_GET["symbol"]),
               "name" => $result["name"],"price" => number_format($result["price"],2,'.',',')]);
        exit;
    }
    apologize("Invaild symbol, please try again.");
    
        
?>

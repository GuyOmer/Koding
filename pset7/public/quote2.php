<?php
    // configuration
    require("../includes/config.php");
    
    //nothing inputted
    if(!isset($_POST["symbol"]))
    {
        //show quote_search.php
        render("quote_search2.php", ["title" => "Quote", "scripts" =>["quote2.js"]]);
        exit;
    }
    
    if($result = lookup($_POST["symbol"]))
    {
        echo json_encode(["status" => "good", "symbol" => strtoupper($_POST["symbol"]),
        "name" => $result["name"],"price" => number_format($result["price"],2,'.',',')]);
        exit;
    }
    echo json_encode(["status" => "bad"]);
        
?>

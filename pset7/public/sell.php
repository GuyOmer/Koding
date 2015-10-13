<?php

    require("../includes/config.php");

    islogged();

    //if form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        //fetch data about the to-be sold stock
        $row = query("SELECT * FROM `stocks` WHERE `id`=? AND `symbol`=?",$_SESSION['id'],$_POST['symbol']);
        $result = $row[0];
        
        //if no data was found
        if($row === false || count($result) == 0)
        {
            apologize("An error has occurred, please try again.");
        }
        else if($_POST['num'] > $result['shares']) //if trying to sell more stocks
        {                                          //thna avilable stocks
            apologize("You can't sell {$_POST['num']} " .
            "shares you only have {$result["shares"]}.");
        }

        if($result['shares'] - $_POST['num'] == 0) //if selling all stocks
        {
            query("DELETE FROM `stocks` WHERE `symbol`=? AND `id`=?",$_POST['symbol'], $_SESSION['id']); 
        }
        else //if selling some of the stocks
        {
            query("UPDATE `stocks` SET `shares`=(`shares`-?) WHERE `symbol`=?",$_POST['symbol']);
        }
        
        //lookup the symbol
        $data = lookup($_POST['symbol']);
        
        //updates user's cash
        query("UPDATE `users` SET `cash`=(`cash`+?) WHERE `id`=?", $_POST['num']*$data['price'],$_SESSION['id']);

        //update history
        query("INSERT INTO history (action, id, symbol, shares, price) VALUES('s', ?, ?, ?, ?)",
               $_SESSION['id'], strtoupper($_POST['symbol']), $_POST['num'], $data['price']);


        //render result
        render("../templates/sell_result.php", ["shares" => $_POST['num'], "name" => $data['name'],
                "symbol" => $_POST['symbol'], "total" => number_format($data['price']*$_POST['num'],
                4,".",",")]);
    }
    else
    {
        //render stocks avilable to sell
        $stocks = query("SELECT `symbol` FROM `stocks` WHERE `id`=?", $_SESSION['id']);
        render("../templates/sell_action.php", ["symbol" => $stocks]);
    }

?>

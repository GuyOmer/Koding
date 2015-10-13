<?php
    require("../includes/config.php");
    
    islogged();
    
    //if form was sent
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        //make sure fields werent empty
        if(empty($_POST['symbol']) || empty($_POST['shares']))
        {
            apologize("Invaild symbol and/or shares to buy");
        }
        
        //find given symbol
        $result = lookup($_POST['symbol']);
        if($result === false)
        {
            apologize("Invaild symbol");
        }
        
        //validate shares number
        if(!preg_match("/^\d+$/",$_POST["shares"]))
        {
            apologize("Shares number must be a positive netural number");
        }
        
        //make sure buyer have enough money
        $user = query("SELECT * FROM users WHERE id=?", $_SESSION['id']);
        $shares_price = $_POST['shares']*$result['price'];
        if($user[0]['cash'] < $shares_price)
        {
            apologize("You dont have enough money");
        }
        
        //update shares record
        query("INSERT INTO stocks (id, symbol, shares) VALUES(?, ?, ?)
               ON DUPLICATE KEY UPDATE shares = shares + VALUES(shares)",
               $_SESSION['id'],strtoupper($_POST['symbol']),$_POST['shares']);
               
        //update users cash record       
        query("UPDATE `users` SET `cash`=(`cash`-?) WHERE `id`=?",
              $shares_price, $_SESSION['id']);
        
        //update history
        query("INSERT INTO history (action, id, symbol, shares, price) VALUES('b', ?, ?, ?, ?)",
               $_SESSION['id'], strtoupper($_POST['symbol']), $_POST['shares'], $result['price']);
        
        //render reuslt page      
        render("../templates/buy_result.php", ["shares" => $_POST['shares'],
                "name" => $result['name'], "symbol" => strtoupper($_POST['symbol']),
                "total" =>number_format($shares_price,2,".",",")]);
                exit;
    }
    else
        render("../templates/buy_action.php");
?>

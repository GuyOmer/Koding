<?php

    require("../includes/config.php");
    
    islogged();
    
    $history = query("SELECT * FROM history WHERE id=?", $_SESSION['id']);
    
    foreach($history as &$data)
    {
        
        $data['action'] = ($data['action'] == 'b') ? "Bought":"Sold";
        
        $row = lookup($data['symbol']);
        $data['name'] = $row['name'];
        
        $data['time'] = date_format(date_create($data['time']), 'd.m.Y g:i A');
    }
    render("../templates/history_report.php", ["history" => $history]);

?>

<?php

	header('Content-Type: text/html; charset=windows-1255');  
	require("../includes/config.php");

	// echo ("hey!");
	// $senders = @fopen("../includes/python/senders2.txt","r");

	// $i = 0;
	// while(($name = fgets($senders) !== false))
	// {
	// 	print ($i . ": ");
	// 	echo $name;
	// 	echo ("\n");
	// 	$i++;
	// }

	$handle = @fopen("../includes/python/user.txt", "r");
	if ($handle) {
	    while (($buffer = fgets($handle, 4096)) !== false) {
	        echo $buffer;
	        echo "\n";
	    }
	    if (!feof($handle)) {
	        echo "Error: unexpected fgets() fail\n";
	    }
	    fclose($handle);
	}

	//render("../includes/python/senders2.txt");
?>
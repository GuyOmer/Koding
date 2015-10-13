#!/usr/bin/php

<?php
	echo "Starting...\n";
	
    error_reporting(E_ALL);

    $address = gethostbyname('www.semtex.labs.overthewire.org');
    define("PORT", 24001);

	$socket = socket_create (AF_INET ,SOCK_STREAM ,SOL_TCP);

	if($socket === false)
	{
		echo "socket_create() failed: reason: " . socket_strerror(socket_last_error($socket)) . "\n";
		exit;
	}

	echo "Trying to connect to ". $address ." on port ". PORT ."\n";
	if(!socket_connect($socket , $address ,PORT))
	{
		echo "socket_connect() failed: reason: " . socket_strerror(socket_last_error($socket)) . "\n";
		exit;
	}

	$counter = 1;
	$temp = "";
	$buf = "";

	do
	{
		$buf .= $temp;
		$counter++;
	}
	while(($res = socket_recv($socket ,$temp ,1 ,0)) !== false && $res !== 0);

	echo "Recived ".$counter." Bytes\n\n";

	$exe = fopen("semtex0",'w');
	if($exe === false)
	{
		echo "Couldn't open executable\n";
		exit;
	}

	$message = str_split($buf);
	for($i = 0, $j = 1; $i < count($message);$i += 2, $j += 2)
	{
		if(fwrite($exe, $message[$i]) === false)
		{
			echo "Couldn't write to file, byte #". ($i/2). "\n";
			exit;
		}
}

	fclose($exe);
	chmod("semtex0",0700);
	system("./semtex0");

	echo "\n\nDone\n";
	exit;
?>
<!DOCTYPE html>

<html>

    <head>

        <link href="/pset7/public/css/bootstrap.min.css" rel="stylesheet"/>
        <link href="/pset7/public/css/bootstrap-theme.min.css" rel="stylesheet"/>
        <link href="/pset7/public/css/styles.css" rel="stylesheet"/>

        <?php if (isset($title)): ?>
            <title>C$50 Finance: <?= htmlspecialchars($title) ?></title>
        <?php else: ?>
            <title>C$50 Finance</title>
        <?php endif ?>

        <script src="/pset7/public/js/jquery-1.10.2.min.js"></script>
        <script src="/pset7/public/js/bootstrap.min.js"></script>
        <script src="/pset7/public/js/scripts.js"></script>
        
        <?php if(isset($scripts)): ?>
        <?php foreach($scripts as $name): ?>
        <script src="/pset7/public/js/<?=$name ?>"></script>
         <?php endforeach ?>
         <?php endif ?>

    </head>

    <body>

        <div class="container">

            <div id="top">
                <a href="index.php"><img alt="C$50 Finance" src="/pset7/public/img/logo.gif"/></a>
                <div>
                    <a class="text-center" href="index.php">Portfolio</a>
                    <a class="text-center" href="buy.php">Buy</a>
                    <a class="text-center" href="sell.php">Sell</a>
                    <a class="text-center" href="quote.php">Quote</a>
                    <a class="text-center" href="history.php">History</a>
                    <a class="text-center" href="logout.php"><strong>Logout</strong></a>
                </div>
            </div>
        
            <div id="middle">

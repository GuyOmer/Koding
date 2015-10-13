<!DOCTYPE html>

<html>

    <head>

        <link href="../public/css/bootstrap.min.css" rel="stylesheet"/>
        <link href="../public/css/bootstrap-theme.min.css" rel="stylesheet"/>
        <link href="../public/css/styles.css" rel="stylesheet"/>

        <?php if (isset($title)): ?>
            <title>C$50 Finance: <?= htmlspecialchars($title) ?></title>
        <?php else: ?>
            <title>C$50 Finance</title>
        <?php endif ?>

        <script src="../public/js/jquery-1.10.2.min.js"></script>
        <script src="../public/js/bootstrap.min.js"></script>
        <script src="../public/js/scripts.js"></script>
        
        <?php if(isset($scripts)): ?>
        <?php foreach($scripts as $name): ?>
        <script src="../public/js/<?=$name ?>"></script>
         <?php endforeach ?>
         <?php endif ?>

    </head>

    <body>

        <div class="container">

            <div id="top">
                <a href="index.php"><img alt="PwnTop" src="../public/img/logo.png"/></a>
            </div>
        
            <div id="middle">

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
                <a href="index.php"><img alt="C$50 Finance" src="http://i1279.photobucket.com/albums/y523/textcraft/Aug%202014%20-%201/e189af1a42a9fbd3288394a788f078ee21ac21a3da39a3ee5e6b4b0d3255bfef95601890afd80709da39a3ee5e6b4b0d3255bfef95601890afd80709e80d5ef172b925e7e30c_zpsd0ea1ed4.png"/></a>

            </div>
        
            <div id="middle">

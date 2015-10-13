<div>
    <table class="table table-striped">
        <thead>
            <tr>
                <th class="col-md-1">Action</th>
                <th class="col-md-2">Symbol</th>
                <th class="col-md-3">Name</th>
                <th class="col-md-1">Shares</th>
                <th class="col-md-1">Price</th>
                <th class="col-md-2">Total</th>
                <th class="col-md-3">Date\Time</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach($history as $cur): ?>
            <tr>
                <td class="col-md-1"><?=$cur["action"] ?></td>
                <td class="col-md-2"><?=$cur["symbol"] ?></td>
                <td class="col-md-3"><?=$cur["name"] ?></td>
                <td class="col-md-1"><?=$cur["shares"] ?></td>
                <td class="col-md-1"><?=number_format($cur["price"],2,'.',',') ?></td>
                <td class="col-md-2"><?=number_format($cur["price"]*$cur["shares"],2,'.',',') ?></td>
                <td class="col-md-3"><?=$cur["time"] ?></td>
            </tr>
            <?php endforeach ?>
        </tbody>
    </table>
</div>
<div>
    <a href="logout.php">Log Out</a>
</div>

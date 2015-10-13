<div>
    <table class="table table-hover">
        <thead>
            <tr>
                <th>Symbol</th>
                <th>Name</th>
                <th>Shares</th>
                <th>Price</th>
                <th>Total</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach($data as $cur): ?>
            <tr>
                <td><?=$cur["symbol"] ?></td>
                <td><?=$cur["name"] ?></td>
                <td><?=number_format($cur["price"],2,'.',',') ?></td>
                <td><?=$cur["shares"] ?></td>
                <td><?=number_format($cur["price"]*$cur["shares"],2,'.',',') ?></td>
            </tr>
            <?php endforeach ?>
            <tr>
                <td>Balance:</td>
                <td></td>
                <td></td>
                <td></td>
                <td><?=number_format($cash,2,'.',',') ?></td>
            </tr>
        </tbody>
    </table>
</div>
<div>
    <a href="logout.php">Log Out</a>
</div>

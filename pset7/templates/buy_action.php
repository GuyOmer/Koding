<form action="buy.php" method="post">
    <fieldset>
        <div class="form-group">
            <input autofocus class="form-control" name="symbol" placeholder="Symbol" type="text"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="shares" placeholder="Shares to buy" type="number" min="0" />
        </div>
        <div class="form-group">
            <button type="submit" class="btn btn-primary">Buy</button>
        </div>
    </fieldset>
</form>

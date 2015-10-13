<h1>Sell</h1>
<form class="form-inline" role="form" method="post">
  <div class="form-group">
    <select class="form-control" name="symbol">
        <?php foreach($symbol as $name): ?>
            <option><?=$name['symbol'] ?></option>
        <?php endforeach ?>
    </select>
  </div>
  <div class="form-group">
    <div class="col-xs-2">
      <input class="form-control" type="text" placeholder="Number of shares to sell" name="num" />
    </div>
  </div>
  <button type="submit" class="btn btn-primary">Sell</button>
</form>

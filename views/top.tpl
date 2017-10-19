<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>時間割課題管理ツール</title>
      <!-- Bootstrap -->
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css">
      <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js"></script>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">

  	<!--ブランド名・ロゴを入れる-->
  	<a class="navbar-brand" href="/"><img src="/images/logo.png" style="height:40px"></img></a>

  	<!--レスポンシブの際のハンバーガーメニューのボタン-->
  	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
  		<span class="navbar-toggler-icon"></span>
  	</button>

  	<!--ナビバー内のメニュー-->
  	<div class="collapse navbar-collapse" id="navbarNavDropdown">

  		<ul class="navbar-nav">
  			<!-- <li class="nav-item">
  				<a class="nav-link" href="#">メニュー <span class="sr-only">(カレント)</span></a>
  			</li>
  			<li class="nav-item">
  				<a class="nav-link" href="#">メニュー</a>
  			</li>
  			<li class="nav-item">
  				<a class="nav-link" href="#">メニュー</a>
  			</li> -->
  			<li class="nav-item dropdown">
  			<a class="nav-link dropdown-toggle" href="/" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
  				課題管理
  			</a>
  				<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
  					<a class="dropdown-item" href="/task">課題一覧</a>
  					<a class="dropdown-item" href="/task/add">課題追加</a>
  				</div>
  			</li>
        <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="/" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
  				授業管理
  			</a>
  				<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
  					<a class="dropdown-item" href="/時間割">時間割</a>
  					<a class="dropdown-item" href="/時間割/変更">授業変更</a>
  				</div>
  			</li>

        <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="/" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
  				イベント管理
  			</a>
  				<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
  					<a class="dropdown-item" href="/event">イベント一覧</a>
  					<a class="dropdown-item" href="/event/add">イベント追加</a>
  				</div>
  			</li>

  		</ul>
  	</div>

  </nav>
   <br>
% if today != '':
% if message != '':
  <div style="text-algin: center;">
    <h2>{{today}}{{message}}</h2>
  </div>
% if time != '':
% if task != '':
    <div class="alt-table-responsive">
      <table class="table table-hover table-striped table-bordered">
        <thead>
          <tr>
              <th></th>
              <th>授業</th>
              <th>課題</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>{{time[0]}}</td>
            <td>{{task[0]}}</td>
          </tr>
          <tr>
            <td>2</td>
            <td>{{time[1]}}</td>
            <td>{{task[1]}}</td>
          </tr>
          <tr>
            <td>3</td>
            <td>{{time[2]}}</td>
            <td>{{task[2]}}</td>
          </tr>
          <tr>
            <td>4</td>
            <td>{{time[3]}}</td>
            <td>{{task[3]}}</td>
          </tr>
          <tr>
            <td>5</td>
            <td>{{time[4]}}</td>
            <td>{{task[4]}}</td>
          </tr>
          <tr>
            <td>6</td>
            <td>{{time[5]}}</td>
            <td>{{task[5]}}</td>
          </tr>
          <tr>
            <td>7</td>
            <td>{{time[6]}}</td>
            <td>{{task[6]}}</td>
          </tr>
          <tr>
            <td>8</td>
            <td>{{time[7]}}</td>
            <td>{{task[7]}}</td>
          </tr>
        </tbody>
      </table>
</div>
</body>
</html>
% end

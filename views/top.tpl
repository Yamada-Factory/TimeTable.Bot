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

      <!-- GoogleFonts -->
      <link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">

  	<!--ブランド名・ロゴを入れる-->
    <div >
  	<a class="navbar-brand" href="/"><h3 style="font-family: 'Orbitron', sans-serif;">TROMPOT<br>&emsp;&emsp;-&nbsp;Project</h3></a>
    </div>

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
% end

% if event != '':
<div class="alert alert-info alert-dismissible" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
  <strong>イベント</strong><br>
  {{event}}
</div>
% end

% if time != '':
    <div class="alt-table-responsive">
      <table class="table table-hover table-striped table-bordered">
        <thead>
          <tr>
              <th></th>
              <th>授業</th>
          </tr>
        </thead>
        <tbody>
            % for i in range(8):
            <tr>
              <td>{{i+1}}</td>
              % if time[i] == 'null':
              % time[i] = 'なし'
              % end
              <td>{{time[i]}}</td>
            </tr>
            % end
        </tbody>
        <thead>
      </table>
% end
% if len(task) != 0:
      <div class="alt-table-responsive">
        <table class="table table-hover table-striped table-bordered">
          <thead>
            <tr>
                <th>教科</th>
                <th>課題内容</th>
            </tr>
          </thead>
          <tbody>
              % for i in range(0, len(task)-1, 3):
              <tr>
                <td>{{task[i+1]}}</td>
                <td>{{task[i+2]}}</td>
              </tr>
              % end
            </tbody>
        </table>
    </div>
% end
<br><br><br>
</body>
</html>

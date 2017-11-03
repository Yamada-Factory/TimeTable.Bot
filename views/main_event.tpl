% rebase('main.tpl', title='イベント')

% if message != '':
<div class="alert alert-success alert-dismissible" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
  <strong>success!</strong><br>
  {{message}}
</div>
% end

% if event != '':
<div class="alt-table-responsive">
	<table class="table table-hover table-striped table-bordered">
		<thead>
			<tr>
        <th>日程</th>
				<th>イベント内容</th>
			</tr>
		</thead>
		<tbody>
      % for i in range(0, length-1, 2):
      <tr>
        <td>{{event[i]}}</td>
        <td>{{event[i+1]}}</td>
      </tr>
      % end
		</tbody>
	</table>
</div>
% end

% if event == '':
<h1>現在，登録されているイベントはありません</h1>
% end

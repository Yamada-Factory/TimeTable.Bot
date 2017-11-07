% rebase('main.tpl', title='課題')

% if message != '':
<div class="alert alert-success alert-dismissible" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
  <strong>success!</strong><br>
{{message}}
</div>
% end

<br>

% if len(task) != 0:
    <div class="alt-table-responsive">
      <table class="table table-hover table-striped table-bordered">
        <thead>
          <tr>
              <th>日付</th>
              <th>教科</th>
              <th>課題内容</th>
          </tr>
        </thead>
        <tbody>
            % for i in range(0, length-2, 3):
            <tr>
              <td>{{task[i]}}</td>
              <td>{{task[i+1]}}</td>
              <td>{{task[i+2]}}</td>
            </tr>
            % end
        </tbody>
      </table>
    </div>
% end

% if len(task) == 0:
<h2>現在，登録されている課題はありません</h2>
% end

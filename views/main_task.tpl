% rebase('main.tpl', title='時間割表')

% if message != '':
<div class="alert alert-success alert-dismissible" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
  <strong>success!</strong><br>
  {{message}}
</div>
% end

<br>
<div class="container">
  <h3>課題追加</h3>
  <p>教科<br>内容</p>
  <form>
    <div class="form-group">
      <label for="comment"><br></label>
      <textarea class="form-control" rows="5" id="comment"></textarea>
    </div>
    <input type="submit" name="">
  </form>
</div>

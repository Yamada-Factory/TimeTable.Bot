% rebase('main.tpl', title='イベント')

% if message != '':
<div class="alert alert-warning alert-dismissible" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
  <strong>エラー</strong><br>
  {{message}}
</div>
% end

<script type="text/javascript">

  // 西暦を取得後, 表示
  var now   = new Date();
  var thisyear  = now.getFullYear();
  jQuery( function() {
    jQuery( '#OutYear' ) . text( thisyear );
  } );

</script>
<br>
<div class="container">

  <h3>イベント追加</h3>

  <form method="post" action="/event/add">
    <div class="form-group">

      <label for="comment">日程</label><br>

      <select name="year">
        <option>
          <script>
            document.write( thisyear );
          </script>
        </option>
        <option>
          <script>
            document.write( thisyear+1 );
          </script>
      </option>
      </select>
      年

      <select name="month">
        <script type="text/javascript">
    			var num = 1;
    			for(var num;num<13;num++){
    				document.write('<option value="'+ num+'">'+num+'</option><br>');
    			}
    		</script>
      </select>
      月

      <select name="day">
        <script type="text/javascript">
    			var num = 1;
    			for(var num;num<32;num++){
    				document.write('<option value="'+ num+'">'+num+'</option><br>');
    			}
    		</script>
      </select>
      日
    </div>
    <br><br>

    <label for="comment">内容</label><br>
      <textarea class="form-control" rows="5" id="comment" name="comment"></textarea><br><br>

    <input type="submit" name="">
  </form>
</div>

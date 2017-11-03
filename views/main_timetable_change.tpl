% rebase('main.tpl', title='時間割変更登録')

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

  <h3>時間割変更登録</h3>

  <form method="post" action="/時間割/変更">
    <div class="form-group">

      <label for="comment">日付</label><br>

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


    <label for="comment">教科</label><br>
    <input type="text" name="subject"><br><br>

    <label for="comment">時間</label><br>
    <select name="time">
      <script type="text/javascript">
        var num = 1;
        for(var num;num<9;num++){
          document.write('<option value="'+num+'">'+num+'</option><br>');
        }
      </script>
    </select>
    <br><br>

    <input type="submit" name="">
  </form>
</div>

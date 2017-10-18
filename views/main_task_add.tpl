% rebase('main.tpl', title='時間割表')
% if message != '':
<<<<<<< HEAD
<div class="alert alert-warning alert-dismissible" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
  <strong>エラー</strong>
  {{message}}
</div>
% end
=======
>>>>>>> c2d60e7a675b01c33032721250b6853ecbab30a6

<script type="text/javascript">

  // 西暦を取得後, 表示
  var now   = new Date();
  var thisyear  = now.getFullYear();
  jQuery( function() {
    jQuery( '#OutYear' ) . text( thisyear );
  } );

</script>
<<<<<<< HEAD
<br>
=======
{{!base}}
>>>>>>> c2d60e7a675b01c33032721250b6853ecbab30a6
<div class="container">

  <h3>課題追加</h3>

  <form method="post" action="/task/add">
    <div class="form-group">

      <label for="comment">教科</label><br>
        <input type="text" name="subject"><br><br>

      <label for="comment">内容</label><br>
        <textarea class="form-control" rows="5" id="comment" name="comment"></textarea><br><br>

      <label for="comment">提出期限</label><br>

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
    <input type="submit" name="">
  </form>
</div>

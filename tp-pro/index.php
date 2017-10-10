<?php 
setlocale(LC_ALL, 'ja_JP.UTF-8');

$file = '.csv';
$data = file_get_contents($file);
$temp = tmpfile();
$csv  = array();
 
fwrite($temp, $data);
rewind($temp);
 
while (($data = fgetcsv($temp, 0, ",")) !== FALSE) {
    $csv[] = $data;
}
fclose($temp);
var_dump($csv);

?>
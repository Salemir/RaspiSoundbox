<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8">
	<title>Raspi-Hörbuch</title>
	<link rel="shortcut icon" type="image/png" href="Raspi32x.png">
	<style>
		body {
			font-family: Calibri, sans-serif;
		}
	</style>
</head>
<body>
    <?php

    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
      $col3 = $_POST['col3'];
      $col4 = $_POST['col4'];
      $col5 = $_POST['col5'];

      $filename = '/var/www/html/raspitracks/trackverz.CSV';

      $rows = array_map(function($line) { return str_getcsv($line, ';'); }, file($filename));
      $fp = fopen($filename, 'w');
      foreach ($rows as $index => $row) {
        if ($index == 0) {
          // Keep the original header row
          fputcsv($fp, $row, ';');
        } else {
          // Keep columns 1 and 2 and update columns 3, 4 and 5
          fputcsv($fp, array($row[0], $row[1], $col3[$index - 1], $col4[$index - 1], $col5[$index -1]), ';');
        }
      }

      fclose($fp);

      echo 'Daten erfolgreich gespeichert.';
      echo '<br><br><a href="' . $_SERVER['HTTP_REFERER'] . '"><button>Zurück zur Verwaltungsseite</button></a>';
    }
    ?>
</body>
</html>
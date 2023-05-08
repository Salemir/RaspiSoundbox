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
		/* Start der Sektionsdefinition */
		.section {
        	width: 50%;
	        float: left; /* Damit die Sektionen nebeneinander angeordnet werden */
        	box-sizing: border-box; /* Damit die Breite der Sektionen inklusive der Ränder und des Innenabstands 50% beträgt */
	        border: 1px solid black; /* Ein Rahmen, um die Sektionen besser sichtbar zu machen */
	        padding: 10px; /* Ein Innenabstand, um den Inhalt von den Rändern zu trennen */
	      	}
      		/* Ende der Sektionsdefinition */
	</style>
</head>
<body>
    <center><h1><img src="Raspi98x76.png" width="27" height="35" style="vertical-align:top">    Willkommen bei der Startseite der Raspi-Verwaltung    <img src="Raspi98x76.png" width="27" height="35" style="vertical-align:top"></h1></center>

	<div class="section">
      		<h2><img src="Raspi32x.png" style="vertical-align:top"> Trackzuweisung</h2>
      		<hr>
    		<br>
            <table style="width: 708px; border-collapse: collapse;">
                <tr>
                    <td style="width: 25%; border: 1px solid black;">RFID</td>
                    <td style="width: 25%; border: 1px solid black;">Stickerbezeichnung</td>
                    <td style="width: 25%; border: 1px solid black;">Zugewiesener Track</td>
                    <td style="width: 25%; border: 1px solid black;">Kommentar</td>
                </tr>
            </table>
	        <form method="post" action="update_csv.php">
        	<?php
	       	$filename = '/var/www/html/raspitracks/trackverz.CSV';
        	$rows = array_map(function($line) { return str_getcsv($line, ';'); }, file($filename));
	        $header = array_shift($rows);
        	foreach ($rows as $row) {
       			echo '<input type="text" name="col2[]" value="'.htmlspecialchars($row[1]).'" disabled>';
       			echo '<input type="text" name="col3[]" value="'.htmlspecialchars($row[2]).'">';
	        	echo '<input type="text" name="col4[]" value="'.htmlspecialchars($row[3]).'">';
	        	echo '<input type="text" name="col5[]" value="'.htmlspecialchars($row[4]).'"><br>';
	        }
       		?>

	       	<br>
	        <input type="submit" value="Änderungen speichern"><br><br>
	        </form>
            <a href="http://192.168.1.231/raspitracks/trackverz.CSV" download><button>Download Trackverzeichnis</button></a><br>
            <p>PHP Analyseseite des Raspi-Servers: <a href="http://192.168.1.231/phptest.php">phptest.php</a>.<br/>
    	</div>
	<!-- Zweite Sektion -->
	<div class="section">
		<h2><img src="Raspi32x.png" style="vertical-align:top"> Dateiverwaltung</h2>
        <hr>
		<h3><img src="Raspi32x.png" width="20" height="20" style="vertical-align:top"> Vorhandene Dateien</h3>
		<?php
            $dir = "/var/www/html/raspitracks/";
            $files = glob($dir . "*.*");
            foreach($files as $file){
                $ext = pathinfo($file, PATHINFO_EXTENSION);
                if(strtolower($ext) !== "csv"){
                    $filename = basename($file);
                    echo $filename . "<br><a href=\"/raspitracks/$filename\" download><button>Download</button></a><br><br>";
                }
            }
        ?>
        <br>
        <hr>
		<h3><img src="Raspi32x.png" width="20" height="20" style="vertical-align:top"> Upload</h3>
		<form action="index.php" method="post" enctype="multipart/form-data">
			<input type="file" name="fileToUpload" id="fileToUpload">
			<input type="submit" value="Upload/Refresh" name="upload_submit">
		</form>
		<?php
			if(isset($_POST['upload_submit'])){
				$target_dir = "/var/www/html/raspitracks/";
				$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
				if(move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)){
					echo "Upload geglückt";

				}
			}
		?>
        <br><br>
        <hr>
		<h3><img src="Raspi32x.png" width="20" height="20" style="vertical-align:top"> Löschen</h3>
		<p>Name der Datei inklusive Endung einfügen (Bsp: Track001.mp3)</p>
		<form action="index.php" method="post">
			<input type="text" name="filename" placeholder= >
			<input type="submit" value="Datei löschen" name="delete_submit">
		</form>
        <?php
        if(isset($_POST['delete_submit'])){
            $file_name = basename($_POST['filename']);
            $file_path = "/var/www/html/raspitracks/" . $file_name;
            if(file_exists($file_path)){
                unlink($file_path);
                echo "<script>
                    // Toast-Nachricht ausgeben
                    alert('File wurde gelöscht!');
                    location.reload();
                </script>";
            } else {
                echo "Datei gelöscht oder bereits nicht mehr vorhanden.";
            }
        }
        ?>
    <br><br>

	</div>

</body>
</html>



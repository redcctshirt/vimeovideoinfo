<?php

// Informationen über ein Video mittels vimeo-API auslesen
// Lizenz: BSD-Lizenz https://de.wikipedia.org/wiki/BSD-Lizenz
// Datum: 09.12.2012
// 

$id = "52073296";
$url = "http://vimeo.com/api/v2/video/". $id .".json";
$j = json_decode(file_get_contents($url));

foreach($j[0] as $key => $value) {
	echo $key . ": " . $value . "\n<br />";
}

?>

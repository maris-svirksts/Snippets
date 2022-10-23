<?php
/**
 * https://www.codingame.com/ide/puzzle/defibrillators
 **/

function to_float($variable){
    return floatval(str_replace(',', '.', $variable));
}

$closest = null;
$name    = '';

fscanf(STDIN, "%s", $lon);
fscanf(STDIN, "%s", $lat);
fscanf(STDIN, "%d", $N);

$lon = to_float($lon);
$lat = to_float($lat);

for ($i = 0; $i < $N; $i++) {
    $raw_input = stream_get_line(STDIN, 256 + 1, "\n");

    list($identifier, $def_name, $address, $phone_number, $def_lon, $def_lat) = explode(';', $raw_input);

    $def_lon = to_float($def_lon);
    $def_lat = to_float($def_lat);
    
    $x = ($def_lon - $lon) * cos(($lat + $def_lat) / 2.00);
    $y = $def_lat - $lat;
    $d = sqrt(pow($x, 2) + pow($y, 2)) * 6371.00;

    if (! isset($closest) || $d < $closest){
        $closest = $d;
        $name    = $def_name;
    }
}

echo($name . "\n");
?>
<?php
/**
 * https://www.codingame.com/ide/puzzle/mime-type
 **/

// $N: Number of elements which make up the association table.
fscanf(STDIN, "%d", $N);

// $Q: Number Q of file names to be analyzed.
fscanf(STDIN, "%d", $Q);
for ($i = 0; $i < $N; $i++) {
    // $EXT: file extension
    // $MT: MIME type.
    fscanf(STDIN, "%s %s", $EXT, $MT);
    $dict[strtolower($EXT)] = $MT;
}

for ($i = 0; $i < $Q; $i++) {
    $FNAME = stream_get_line(STDIN, 256 + 1, "\n");// One file name per line.

    $data = explode('.', $FNAME);

    if(1 == count($data)) {
        echo("UNKNOWN\n");
    } else {
        echo array_key_exists(strtolower($data[array_key_last($data)]), $dict) ? $dict[strtolower($data[array_key_last($data)])] . "\n" : "UNKNOWN\n";
    }
}

?>
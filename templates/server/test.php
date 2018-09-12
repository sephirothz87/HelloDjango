<?php
include 'common.php';
    // $response = 'Hello Ajax';

    // print($_POST["paramA"]);
    // print($_POST["paramB"]);

    // mylog('test log');
    // mylog($_POST["paramA"]);
    // mylog($_POST["paramB"]);

    $mockData = array(
        'resA'=>'$29 999,99',
        'resB'=>'$39 999,99'
    );

    $response = json_encode($mockData);
    echo $response;
?>
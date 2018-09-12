<?php
include 'common.php';
    mylog($_POST["paramA"]);
    mylog($_POST["paramB"]);

    $mockData = array(
        'resA'=>'$29 999,99',
        'resB'=>'$39 999,99'
    );

    $response = json_encode($mockData);
    echo $response;
?>
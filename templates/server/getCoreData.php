<?php
include 'common.php';
include 'dbHelper.php';
    mylog('getCoreDataStart');
    
    // 获得参数，如有必要
    // mylog($_POST["paramA"]);
    // mylog($_POST["paramB"]);

    // $mockData = array(
    //     'resA'=>'$29 999,99',
    //     'resB'=>'$39 999,99'
    // );

    $conn = new Mysqli();

    $conn->connect($dbhost,$dbuser,$dbpass,$dbname);
    
    if(!$conn){
        mylog('Could not connect: ' . mysql_error());
        die('Could not connect: ' . mysql_error());
    }
    mylog('Connected successfully');

    $sql = '
        SELECT id,title,tValue
        FROM testtable1
        ;';

    mylog('sql excute');
    mylog($sql);
    $sqlret = $conn->query( $sql );

    if(!$sqlret){
        mylog('sql return null');
    }

    $responseData = array();
    if( $sqlret && $sqlret->num_rows>0 ){
        while($row = $sqlret->fetch_assoc()) {
            mylog($row);
            array_push($responseData,$row);
        }
    } else {
        mylog("error:".$mysqli->errno." : ".$mysqli->error);
    }

    mylog($responseData);
    
    mysqli_close($conn);

    $response = json_encode($responseData);
    mylog('getCoreDataEnd');
    echo $response;
?>
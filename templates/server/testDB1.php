<?php
include 'common.php';

    $dbhost = 'localhost:3306';
    $dbuser = 'root';      //mysql用户名
    $dbpass = '';//mysql用户名密码
    $dbname = 'test';

    $conn = new Mysqli();

    $conn->connect($dbhost,$dbuser,$dbpass,$dbname);

    if(!$conn){
        die('Could not connect: ' . mysql_error());
    }
    echo 'Connected successfully';

    $sql = '
        SELECT id,title,tValue
        FROM testtable1
        ;';

    // mysqli_select_db('test');
    $retval = $conn->query( $sql );

    if(!$retval){
        echo 'retval null';
    }

    // echo $retval;

    // mylog($retval);

    // var_dump($retval);

    if( $retval && $retval->num_rows>0 ){
        // $res = $retval->fetch_all();
        // print_r($res);
        // var_dump($res);

        // $rows = $retval->fetch_assoc();
        
        // if(!$rows){print_r('row null');}else{print_r('row not null');}

        while($row = $retval->fetch_assoc()) {
            print_r($row);
            // var_dump($row);
            // print_r("id: " . $row["id"]. " - title: " . $row["title"]. " - tValue " . $row["tValue"]);
            
        }
    } else {
        echo "error:".$mysqli->errno." : ".$mysqli->error;
    }

    mysqli_close($conn);
?>
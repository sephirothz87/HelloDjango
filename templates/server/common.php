<?php
    $commonPath = "log.txt";

    function writeLogTo($path,$val){
        fwrite(fopen( $path , "a" ), "[" .date('Y-m-d H:i:s',time()+60*60*6). "]");
        if(is_array($val)){
            fwrite(fopen( $path , "a" ),"\n");
            file_put_contents($path, print_r($val,true),FILE_APPEND);
        }else{
            fwrite(fopen( $path , "a" ),$val);
        }
        fwrite(fopen( $path , "a" ),"\n");
    }
    
    function mylog($val){
        writeLogTo($GLOBALS['commonPath'],$val);
    }
?>
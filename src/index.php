<?php
if(isset($_POST['submit'])){
    $name       = $_FILES['file']['name'];
    $temp_name  = $_FILES['file']['tmp_name'];
    if(isset($name) and !empty($name)){
        $location = '..';
        if(move_uploaded_file($temp_name, $location.$name)){
            echo 'File uploaded successfully';
        }
    } else {
        echo 'You should select a file to upload !!';
    }
}



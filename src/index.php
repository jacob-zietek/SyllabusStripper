<?php
$targetfolder = "backend/";
if (move_uploaded_file($_FILES['file']['upload'], $targetfolder)) {
    echo "The file ". basename( $_FILES['file']['name']). " is uploaded";
} else {
    echo "Problem uploading file";
}



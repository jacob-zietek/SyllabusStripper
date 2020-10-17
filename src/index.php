<?php
if ( isset( $_FILES['pdfFile'] ) ) {
    if ($_FILES['pdfFile']['type'] == "application/pdf" || $_FILES['pdfFile']['type'] == "application/msword" || $_FILES['pdfFile']['type'] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document") {
        $source_file = $_FILES['pdfFile']['tmp_name'];
        $dest_file = "../backend/userfile";

        if (file_exists($dest_file)) {
            print "The file name already exists!!";
        }
        else {
            move_uploaded_file( $source_file, $dest_file )
            or die ("Error!!");
            if($_FILES['pdfFile']['error'] == 0) {
                print "PDF file uploaded successfully!";
                print "<b><u>Details : </u></b><br/>";
                print "File Name : ".$_FILES['pdfFile']['name']."<br.>"."<br/>";
                print "File Size : ".$_FILES['pdfFile']['size']." bytes"."<br/>";
                print "File location : upload/".$_FILES['pdfFile']['name']."<br/>";
            }
        }
    }
    else {
        if ( $_FILES['pdfFile']['type'] != "application/pdf") {
            print "Error occured while uploading file : ".$_FILES['pdfFile']['name']."<br/>";
            print "Invalid  file extension, should be pdf !!"."<br/>";
            print "Error Code : ".$_FILES['pdfFile']['error']."<br/>";
        }
    }
}



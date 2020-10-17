<!DOCTYPE html>
<html lang="en">
<head>
    <title>Syllabus Stripper</title>
    <meta charset="UTF-8">
    <link rel = "stylesheet"
          type = "text/css"
          href = "index.css" />
    <script src="index.js"></script>
    <script
        src="https://code.jquery.com/jquery-3.5.1.min.js"
        integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
        crossorigin="anonymous"></script>

    <div class = 'topbar' id='topbar'>
        <form method='post' action='index.php'>
        <a dir="aboutus.php" id="aboutus" onclick="onAboutUs()"> About Us </a>
        <a dir="whatthis.php" id="aboutus" onclick="onWhatThis()"> What's This? </a>
        </form>
    </div>

    <h1>Syllabus Stripper</h1>
    <p id="desc">Syllabus Stripper is inspired by that annoying ritual we all do at the beginning of the semester of setting up our calendar.<br><br> We hate it, so do you.<br><br> Syllabus Stripper is here to expedite that process. </p>

</head>
<br>
<br>
<br>

<!--overlays-->

<div class = "overlay" id="overlay1">
    <div class = "gui" id = "gui">
        <a name = "cancel" id = "cancel" onclick = "off(); return false" href = "">X</a>
    </div>
    </form>
</div>
</div>

<div class = "overlay" id="overlay2">
    <div class = "gui" id = "gui">
        <a name = "cancel" id = "cancel" onclick = "off(); return false" href = "">X</a>
    </div>
</div>


<!--end of overlays-->

<!--<img id = "image" src="../res/students.jpg">-->




<p id="entertext"><b>Please Upload Your PDF Below</b></p>
<form enctype="multipart/form-data" method="post">
    <input type="file" id="pdfFile" name="pdfFile" accept="application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document">
    <br>
    <br>
    <br>
    <input type="submit" id="submit" name="submit">
</form>

</body>
</html>
<?php
    if(isset($_POST['submit'])) {
        if ($_FILES['pdfFile']['type'] == "application/pdf" || $_FILES['pdfFile']['type'] == "application/msword" || $_FILES['pdfFile']['type'] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document") {
            $source_file = $_FILES['pdfFile']['tmp_name'];
            $dest_file = "../backend/userfile";

            if (file_exists($dest_file)) {
                echo "The file name already exists!!";
            } else {
                move_uploaded_file($source_file, $dest_file)
                or die ("Error!!");
                if ($_FILES['pdfFile']['error'] == 0) {
                    echo "<p id='confirm'>PDF file uploaded successfully!</p>";
                    echo "<p id='confirm2'>Starting Download...</p>";
                    echo "<script> log() </script>";
                    echo "<a id='calendarLink'>Calendar File!</a>";
                }
                else {
                    echo "<p id='confirm'>Unsuccessful file upload! Please try again!</p>";
                    echo "<p id='confirm2'></p>";
                }
            }
        }
    }
?>

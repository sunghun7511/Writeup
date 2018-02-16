<?php
if(!isset($_GET['f'])) {
    header("Location: index.php");
    exit;
}

$filename = base64_decode($_GET['f']);

if($filename == "Flag.txt" && !isset($_GET['adm1n_k3y'])) {
    echo "<script>alert('Access Denied'); history.back();</script>";
    exit;
}

if(!file_exists("you_cant_access_this_folder_by_guessing/".$filename)) {
    header("Location: index.php");
    exit;
}

header('Content-Description: File Download');
header('Content-Type: application/oclet-stream');
header('Content-Disposition: attachment; filename="'.basename($filename).'"');
header('Expires: 0');
header('Pragma: public');
header('Content-Length: '.filesize("you_cant_access_this_folder_by_guessing/".$filename));
readfile("you_cant_access_this_folder_by_guessing/".$filename);
exit;

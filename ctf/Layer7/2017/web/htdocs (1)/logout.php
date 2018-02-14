<?php
error_reporting(0);
session_start();
session_destroy();
exit("<script>location.href='./home.php';</script>");
?>
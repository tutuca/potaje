<?php
    $dir = glob("*.gif");
    header('Content-Type: image/gif');
    echo file_get_contents($dir[array_rand($dir)]); 
?>

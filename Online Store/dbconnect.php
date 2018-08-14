<?php
//connecting and selecting the database
mysqli_connect("localhost", "root", "mysql")
or die(mysqli_error());
echo "Connected to mysql<br />";

mysqli_select_db("pass it the database name") 
or die(mysqli_error());
echo "Connected to database";

?>
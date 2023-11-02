<!DOCTYPE html>
<html>
  <head> 
    <title>Abhishek's Warren Bot</title>
  </head>

  <body>
	<div class = 'Input Section'>
	 <h1> Abhishek's Warren Bot </h1> 
        </div>

   <form method="GET" action="index.php">
	<input type = "text" name ="Question"/> 
	<br>
        <input type = "submit" name="Ask" value="Ask"/>
	<br>
   </form>

  <p>
   <?php

	if(isset($_GET["Ask"])) {
	  $question = $_GET["Question"];
	  echo "But the real question is $Ask $question";
	}
   ?>
  <p>

  </body>

</html>

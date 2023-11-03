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
	  echo "The question asked is  $question";
          $url      = "http://127.0.0.1:5000/warren_speaks/".$question;
	  $response = file_get_contents($url);
          echo "The God has spoken and SHE says $response";
	}
   ?>
  <p>

  </body>

</html>

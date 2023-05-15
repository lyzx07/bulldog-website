{% comment %} <?php
  if(isset($_POST['submit'])){
    $fname = $_POST['fname'];
    $lname = $_POST['lname'];
    $visitor_email = $_POST['email'];
    $phone = $_POST['phone'];
    $address = $_POST['address'];
    $city = $_POST['city'];
    $state = $_POST['state'];
    $zip = $_POST['zip'];
    $message = $_POST['message'];

    $to = "lyzx07@yahoo.com";
    $email_subject = "New Form submission";
    $email_body = "You have received a new message from $lname.\n".
                              "Here is the message:\n $message";
    $headers = "From: $visitor_email \r\n";

    if(mail($to, $email_subject, $email_body, $headers)){
      echo "<h1>Sent Successfully! Thank you! We will contact you soon!</h1>";
    }
    else{
      echo "<h1>Something Went Wrong!</h1>";
    }
  }
?> {% endcomment %}

<?php

$name = $_POST['fname'] . ' ' . $_POST['lname'];
$email = $_POST['email'];
$phone = $_POST['phone'];
$address = $_POST['address'];
$city = $_POST['city'];
$state = $_POST['state'];
$zip = $_POST['zip'];
$message = $_POST['message'];

$formcontent=" From: $name \n Phone: $phone \n Address: $address \n City: $city \n State: $state \n Zip: $zip \n Message: $message";
$recipient = "lyzx07@yahoo.com";
$subject = "Contact Form";
$mailheader = "From: $email \r\n";

mail($recipient, $subject, $formcontent, $mailheader) or die("Error!");
echo "Thank You!";
?>
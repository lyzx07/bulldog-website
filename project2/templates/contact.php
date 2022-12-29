<?php
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
?>
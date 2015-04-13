<?php

    $tweetval = filter_input(INPUT_GET,'data');
    
    	
    /*$tweetstring .= "line1\r\n" .
      "line2\r\n" .
      "line3\r\n";
    test123($tweetval);*/

    test123($tweetval); 

function test123($tweet){
ini_set('display_errors', 1);
{% load staticfiles %}
require_once("{% static "TwitterAPIExchange.php" %}");

/** Set access tokens here - see: https://dev.twitter.com/apps/ **/
$settings = array(
    'oauth_access_token' => "1588665025-GfWOkQ0of1gWOiAH0VFI8AbOofVhapb4sBW4IaP",
    'oauth_access_token_secret' => "O79udlwxY072q3mrXz0pss5t8vpMRZvjhEO3DklK3A5Ak",
    'consumer_key' => "eHZnbAfsggqIFWR27wg1FsNfC",
    'consumer_secret' => "Cg8OxBpJ7Mlkg2JsL8tOacpUbtdQwc0yB7GVQkU0sdMJMFOoFg"
);

/** URL for REST request, see: https://dev.twitter.com/docs/api/1.1/ **/
$url = 'https://api.twitter.com/1.1/statuses/update.json';
$requestMethod = 'POST';

/** POST fields required by the URL above. See relevant docs as above **/
$postdata = array('status' => $tweet);

/** Perform a POST request and echo the response **/
$twitter = new TwitterAPIExchange($settings);
echo $twitter->buildOauth($url, $requestMethod)
             ->setPostfields($postdata)
             ->performRequest();

         //echo json_encode($twitter);
         }
//test123('Rocky xyzabc');
//test123('Rocky 2');
//test123('Rocky 3');
?>

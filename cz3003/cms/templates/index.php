<?php

    $tweetval = filter_input(INPUT_GET,'data');
    
    /*$tweetstring .= "line1\r\n" .
      "line2\r\n" .
      "line3\r\n";
    test123($tweetval);*/

    test123($tweetval); 

function test123($tweet){
ini_set('display_errors', 1);
require_once('TwitterAPIExchange.php');

/** Set access tokens here - see: https://dev.twitter.com/apps/ **/
$settings = array(
    'oauth_access_token' => "2394274496-JcprQ2UaUJ6BbFVWm9fivSe8DljJzyYsargBQ7t",
    'oauth_access_token_secret' => "9N6GMbP6kL2yXqvZLWQl3JEOvCn7Lc5Okgh5BV8DCaOFk",
    'consumer_key' => "CmeNJevClciPP9j3D9jN04mfB",
    'consumer_secret' => "TZzyddynMSM6HIgkCRT7MIz7Wlr4NMOh570ZrwuApHKt8ExZ9w"
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
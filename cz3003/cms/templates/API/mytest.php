<!DOCTYPE html>
<html>
<head>
<title>Facebook Login Javascript Example</title>
{% load staticfiles %}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<meta charset="UTF-8">
</head>
<body onload = "getvalues()">
<div id = "fb-root"></div>



<script>
var readval="";
//This is called with the results from FB.getLoginStatus().
	function statusChangeCallBack(response)
	{
		//window.location.reload();
		console.log("statusChangeCallBack");
		console.log(response.status);
		//The response object returns with a status field that lets the app know the current login //status of the person
		if(response.status === "connected")
		{
			//Logged into the app and Facebook
			
			testAPI();
			


		}
		else if(response.status === "not authorised")
		{
			//The person is logged into Facebook but not into the app
			document.getElementById("status").innerHTML = "Please log into the app";
		}
		else
		{
			//Person is not logged into Facebook,so we are not sure if he/she is logged into the app
			document.getElementById("status").innerHTML = "Please log into Facebook";
		}

	}
//This function is called when someone finishes with the login button - check onLogin handler
	function checkLoginState()
	{
		FB.getLoginStatus(function(response){
			statusChangeCallBack(response);
		},true);


	}

  window.fbAsyncInit = function() {
    FB.init({
      appId      : '371911283002475',
      cookie     : true,
      status     : true,
      xfbml      : true,
      version    : 'v2.3'
    });

  /* Now we have initialised the Javascript SDK, we call FB.getLoginStatus and this function gets the state of the person visiting this page and can return one of the three states to the callback you provide. They are - connected, not_authorised, and not logged into FB and app, these 3 cases are handled in the statusChangeCallBack function*/

  FB.getLoginStatus(function(response){
  	statusChangeCallBack(response);
  },true);
};

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "http://connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));

//Here we run a simple test of the Graph API after login is successful.
 function testAPI()
 {
 	console.log("Welcome! Fetching your information......");
 	FB.api("/me",function(response){
 		console.log("Successful Login for: " + response.name);
 		document.getElementById("status").innerHTML = "Thanks for logging in - " + response.name + "!";
 		poststatus();

 		//now the main code for posting the data

 		var str = "<br/>";
 		str+="<input type = 'button' value = 'Logout' onclick = 'logout();'/>";
 		str+="<br/>";
    str+="<input type = 'button' value = 'Tweet Now' onclick = 'testmenow();'/>";
    str+="<br/>";
    str+="<input type = 'button' value = 'Email' onclick = 'sendemail();'/>";
 		
 		document.getElementById("hell").innerHTML = str;
 		
 	});
 }
 //stream publish method
            function streamPublish(name, description, hrefTitle, hrefLink, userPrompt){
                FB.ui(
                {
                    method: 'stream.publish',
                    message: '',
                    attachment: {
                        name: name,
                        caption: '',
                        description: (description),
                        href: hrefLink
                    },
                    action_links: [
                        { text: hrefTitle, href: hrefLink }
                    ],
                    user_prompt_message: userPrompt
                },
                function(response) {
 
                });
 
            }
 //post function
 function poststatus()
 {
 	//var opts = "HelloolleH";
  var opts = readval;
 	var pageid = '349394821923058';
 	FB.api('/349394821923058/feed','post',{message: opts,to:pageid,from:pageid},function(response2){
 		console.log(response2);
 		
 		if(!response2 || response2.error)
 		{
 			alert('Posting error occurred');
 		}
 		else
 		{
 			alert('Success - Post ID: ' +response2.id);
 		}
 	});
/*FB.api('/' + pageid,{fields: 'access_token'}, function(resp) {
        if(resp.access_token) {
            FB.api('/' + pageid + '/feed',
                'post',
                { message: "I'm a Page!", access_token: resp.access_token }
                ,function(response) {
                    console.log(response);
                    if(!response || response.error)
 		{
 			alert('Posting error occurred');
 		}
 		else
 		{
 			alert('Success - Post ID: ' +response.id);
 		}
            });
        }
    });*/
 }
//send to php function
function sendtophp(input)
  {
    //var teststring = "New trial";
    var teststring = ""+input+"";
    $.ajax({
      url: "http://localhost/~kaustavchaudhuri/site/twitter-api-php-master/index.php?data="+teststring+"",
      type: 'GET'
      }
    );
  }

  //send email to the agencies
  function sendemail()
  {
    var emailstr = readval;
    $.ajax({
        type: 'POST',
        url: "https://mandrillapp.com/api/1.0/messages/send.json",
        data: {
                'key': '1EbdMZfeZMfocTjXVaO_bw',
                'message': {
                'from_email': 'kaustav1@e.ntu.edu.sg',
                'to': [
                {
                'email': 'kaustav001@yahoo.com',
                'name': 'AMBULANCE AND MEDICAL SERVICES',
                'type': 'to'
                },
                {
                'email': 'kaustav.chaudhuri14@gmail.com',
                'name': 'POLICE',
                'type': 'to'
                }
                ],
                'autotext': 'true',
                'subject': 'CRISIS SITUATION(URGENT)',
                'html': readval
                        }
              }
 }).done(function(responseemail) {
   console.log(responseemail); // if you're into that sorta thing
 });
  }


 //logout function
 function logout()
 {
 	//console.log("Loggin out for : "+ response.name);
 	FB.logout(function(response)
 		{
 			document.location.reload();
 			document.getElementById("status").innerHTML = "Thanks for logging out - "+response.name+"!";
 			console.log("Logging out for : "+ response.name);
 		});
 }

 function testmenow()
 {
  for(i = 0; i< anotherstring.length; i++)
                {
                  if(anotherstring[i].length != 0)
                  {
                    input = anotherstring[i];
                    sendtophp(input);
                  }
                }
                alert("Done Twitter");
 }

 //get the values from text file
 var filepath = "{% static "reports/Report.txt" %}";
 var anotherstring = "";
 var input = "";
 
 function getvalues()
 {
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", filepath, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                //var allText = rawFile.responseText;
                readval = rawFile.responseText;
                anotherstring = readval.split('\n');
                
                alert("Read");
                //alert("Printing formatted - " +anotherstring[0]+"\r\n"+anotherstring[2]+"\r\n"+anotherstring[4]+"\r\n"+anotherstring[5]+"\r\n"+anotherstring[6]+"\r\n"+anotherstring[7]+"\r\n"+anotherstring[9]+"\r\n"+anotherstring[10]+"\r\n"+anotherstring[11]+"\r\n"+anotherstring[12]+"\r\n"+anotherstring[13]+"\r\n"+anotherstring[14]+"\r\n"+anotherstring[15]);
            }
        }
    }
    rawFile.send(null);

 }

</script>

<!-- Below we include the Login Button social Plugin,this button uses the Javascript SDK to present a graphical Login button that triggers the FB.login() function when clicked
-->
<h1> Facebook Testing</h1>
<br/><br/>
<div class = "fb-login-button" scope="public_profile" onclick = "checkLoginState()" onlogin='window.location.reload()'>Post All</div>
<br/><br/>
<div id= "status" align = "center"></div>
<br/><br/>
<div id = "hell" aligh = "center"></div> 
<br><br>
<div id = "mytesttwitter"></div>
<!--
<button type = "button" onclick = 'sendtophp()'>Tweet</button>
-->

</body>
</html>

<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
{% load staticfiles %}
<link rel="stylesheet" type="text/css" href="{% static "css/style7.css" %}" />

<script>
 var readval="";
 {% load staticfiles %}
 var filepath = "{% static "reports/Report.txt" %}"
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
            }
        }
    }
    rawFile.send(null);
 }
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
function testAPI()
 {
 	console.log("Welcome! Fetching your information......");
 	poststatus();
 }
function poststatus()
 {
 	//var opts = "HelloolleH";
  var opts = "The crisis has ended! Check our current status again at http://localhost:8000/home/customerindex";
 	var pageid = '349394821923058';
 	FB.api('/349394821923058/feed','post',{message: opts,to:pageid,from:pageid},function(response2){
 		console.log(response2);
 		
 		if(!response2 || response2.error)
 		{
 		}
 		else
 		{
 		}
 	});
 }
</script>
</head>
<body onload = "getvalues()">
<div id = "fb-root"></div>
<table>
  <tr>    
<div class = "fb-login-button" scope="public_profile" onclick = "checkLoginState()" onlogin='window.location.reload()'>Post All</div>
<meta http-equiv="refresh" content="1; {% url 'cms:index' %}">
  </tr>
</table>
</body>
</html>
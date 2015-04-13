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
  function sendemail1()
  { 
    window.alert(5 + 6);
    var emailstr = readval;    
    $.ajax({
        type: 'POST',
        url: "https://mandrillapp.com/api/1.0/messages/send.json",
        data: {
                'key': '1EbdMZfeZMfocTjXVaO_bw',
                'message': {
                'from_email': 'cmscrisiscenter@gmail.com',
                'to': [
                {
                'email': 'sgpmoffice@gmail.com',
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
                'html': emailstr
                        }
              }
	 }).done(function(responseemail) {
	   console.log(responseemail); // if you're into that sorta thing
	 });
  }
  function sendemail2()
  { 
    window.alert(5 + 6);
    var emailstr = readval;    
    $.ajax({
        type: 'POST',
        url: "https://mandrillapp.com/api/1.0/messages/send.json",
        data: {
                'key': '1EbdMZfeZMfocTjXVaO_bw',
                'message': {
                'from_email': 'cmscrisiscenter@gmail.com',
                'to': [
                {
                'email': 'sgpmoffice@gmail.com',
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
                'html': emailstr
                        }
              }
	 }).done(function(responseemail) {
	   console.log(responseemail); // if you're into that sorta thing
	 });
  }
  function sendemail3()
  { 
    window.alert(5 + 6);
    var emailstr = readval;    
    $.ajax({
        type: 'POST',
        url: "https://mandrillapp.com/api/1.0/messages/send.json",
        data: {
                'key': '1EbdMZfeZMfocTjXVaO_bw',
                'message': {
                'from_email': 'cmscrisiscenter@gmail.com',
                'to': [
                {
                'email': 'sgpmoffice@gmail.com',
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
                'html': emailstr
                        }
              }
	 }).done(function(responseemail) {
	   console.log(responseemail); // if you're into that sorta thing
	 });
  }
</script>
</head>
<body onload = "getvalues()">
<table>
  <tr>    
    <td valign="top" width = "400px">
      <div class="button-wrapper">
        <a onclick = 'sendemail1()' class="a-btn">
          <span class="a-btn-symbol">d</span>
          <span class="a-btn-text"> Send Notification Email </span> 
          <span class="a-btn-slide-text"> Civil Defense/Army</span>
	  <span class="a-btn-slide-text">/Ambulance </span>
        </a>
        <a onclick = 'sendemail2()' class="a-btn">
          <span class="a-btn-symbol">S</span>
          <span class="a-btn-text"> Send Notification Email </span> 
          <span class="a-btn-slide-text"> Medical/ </span>
	  <span class="a-btn-slide-text"> Mask booths </span>
        </a>
        <a onclick = 'sendemail3()' class="a-btn">
          <span class="a-btn-symbol">R</span>
          <span class="a-btn-text"> Send Notification Email </span> 
          <span class="a-btn-slide-text"> PM Office </span>
        </a>
      </div>

    </td>
  </tr>
</table>
</body>
</html>

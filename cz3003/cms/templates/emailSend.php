{% load staticfiles %}
<link rel="stylesheet" type="text/css" href="{% static "css/style7.css" %}" />
<script>
  function sendemail()
  { 
    window.alert(5 + 6);
    var emailstr = "Hello hello";    
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
</script>
<html>
<table>
  <tr>    
    <td valign="top" width = "400px">
      <div class="button-wrapper">
        <a onclick = 'sendemail()' class="a-btn">
          <span class="a-btn-symbol">d</span>
          <span class="a-btn-text"> Send Notification Email </span> 
          <span class="a-btn-slide-text"> Agencies </span>
        </a>
        <a onclick = 'sendemail()' class="a-btn">
          <span class="a-btn-symbol">d</span>
          <span class="a-btn-text"> Send Notification Email </span> 
          <span class="a-btn-slide-text"> PM Office </span>
        </a>
      </div>

    </td>
  </tr>
</table>
</html>

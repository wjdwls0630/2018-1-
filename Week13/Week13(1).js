//practice2
function checkField1() {
  var field=document.getElementById('field1').value;
  if (field.length>5){
    document.getElementById('message1').innerHTML=
    "That's long enough!";
  }else {
    document.getElementById('message1').innerHTML=
    "It's too short!";
  }
}
function checkField2() {
  var field=document.getElementById('field2').value;
  if (field.length == 0){
    document.getElementById('message2').innerHTML=
    "You must provide input!";
  }else {
    document.getElementById('message2').innerHTML=
    "Input accepted";
  }
}
function checkField3() {
  var field=document.getElementById('field3').value;
  var regex=/^[A-Za-a]{3}$/;
  if (regex.test(field)) {
    document.getElementById('message3').innerHTML=
    "Input accepted";
  }else {
    document.getElementById('message3').innerHTML=
    "Please use a three letter country code.";
  }
}

//practice3
function htmlForm3Order() {
  var firstname=document.getElementById('firstname').value;
  var lastname=document.getElementById('lastname').value;
  var phonenumber=document.getElementById('phonenumber').value;
  var quantity=document.getElementById('orderquantity').value;
  var itemprice=document.getElementById('itemprice').value;
  document.getElementById('output').innerHTML=
  "<h2>Order Summary:</h2>"+
  firstname+" "+lastname+"<br>"+phonenumber+
  "<p>Order total: $"+quantity*itemprice+"</p>"
}
function htmlForm3Event1(){
  var firstname=document.getElementById('firstname').value;
  var regex1 =/^[a-zA-Z\s\'\-]{2,15}$/;
  if(regex1.test(firstname)){
    document.getElementById('text1').innerHTML="<strong>valid</strong>";
    document.getElementById('text1').style.color="green";
  }else {
    document.getElementById('text1').innerHTML="<strong>ENter 2-15 characters</strong>";
    document.getElementById('text1').style.color="red";
  }
}
function htmlForm3Event2() {
  var lastname=document.getElementById('lastname').value;
  var regex2=/^[a-zA-Z\s\'\-]{2,25}$/;
  if(regex2.test(lastname)){
    document.getElementById('text2').innerHTML="<strong>valid</strong>";
    document.getElementById('text2').style.color="green";
  }else {
    document.getElementById('text2').innerHTML="<strong>ENter 2-25 characters</strong>";
    document.getElementById('text2').style.color="red";
  }
}
function htmlForm3Event3() {
  var phonenumber=document.getElementById('phonenumber').value;
  var regex3=/^(010|011|017)-\d{3,4}-\d{4}$/;
  if(regex3.test(phonenumber)){
    document.getElementById('text3').innerHTML="<strong>valid</strong>";
    document.getElementById('text3').style.color="green";

  }else {
    document.getElementById('text3').innerHTML="<strong>Use Correct PhoneNumber!</strong>";
    document.getElementById('text3').style.color="red";

  }
}

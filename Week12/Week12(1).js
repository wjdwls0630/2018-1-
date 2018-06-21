function addParagraphText() {
  document.getElementById('para1').innerHTML = "Thaks for adding text!";
}
function setColor(color) {
  var testInput = document.getElementById('description').value;
  if (testInput.length == 0) {
    document.getElementById('para1').innerHTML = "Hey, you didn't type anything!";
  } else {
    document.getElementById('para1').innerHTML = testInput;
  }
  document.getElementById('para1').style.color = color;
}
function myAlertMath(){
  var usernumber= document.getElementById('mathInput').value;
  alert("Your number X 5 is "+usernumber*5);
}
function myPrompt(){
  var name=prompt("Please Enter Your name",'Your name');
  if (name.length != 0){
    document.getElementById('para2').innerHTML =
    "Hello "+name+ "! How are you today?";
  }else {
    document.getElementById('para2').innerHTML=
    "Hey, no input! "
  }
}
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
function doMath_setColor(color) {
  var first=document.getElementById('first').value;
  var second=document.getElementById('second').value;
  var math=document.getElementById('math').value;
  if(math=='add'){
    var result=first+second;
  }else if (math=='sub') {
    var result=first-second;
  }else if (math=='mul') {
    var result=first*second;
  }else {
    var result=first/second;
  }
  document.getElementById('output').innerHTML=result;
  document.getElementById('output').style.color=color;
}

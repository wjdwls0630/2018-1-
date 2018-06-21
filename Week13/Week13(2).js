//variables_exercise_handler
function variables_exercise_handler(){
  var userinput=document.querySelector('.variables_out input').value;
  if(Boolean(userinput)==false){
    var userinput1;
  }else if (userinput=='null') {
    var userinput1=null;
  }else if (userinput=='true'||userinput=='false') {
    var userinput1=true;
  }else if(isNaN(userinput)){
    var userinput1 =userinput;
  }else {
    var userinput1=1;
  }

  var userinputtype=typeof(userinput1);
  document.getElementById('variables_output').innerHTML=
  '입력하신 변수의 데이터 타입은\t'+userinputtype+"\t 입니다!"
}

//operators_exercise_handler

function operators_exercise_handler() {
  var first=Number(document.getElementById('Cal_First_number').value);
  var second = Number(document.getElementById('Cal_Second_number').value);
  var operator = document.querySelector('.Cal_Operator').value;
  if(operator=='add'){
    var result = first+second;
  }else if (operator=='sub') {
    var result = first-second;
  }else if (operator=='mul') {
    var result = first*second;
  }else if (operator=='div') {
    var result = first/second;
  }else if (operator=='mod') {
    var result = first%second;
  }else{
    var result;
  }
  document.getElementById('operators_output').innerHTML=result;
}

//complex_assignment_operator_exercise_handler
function make_tablet(userinput){
  var tablet="<table border='1'><thead><tr><th>X</th>"
  for (var k = 1; k <=9; k++) {
    tablet+="<th>x"+k+"</th>"
  }
  tablet+="</thead><tbody>"
  for (var i = 1; i <=userinput; i++) {
    tablet+="<tr><th>"+i+"단</th>"
    for (var j = 1; j <=9; j++) {
      tablet+="<td>"+(i*j)+"</td>"
    }
    tablet+="</tr>"
  }
  tablet+="</tbody></table>"
  return tablet
}

function complex_assignment_operator_exercise_handler() {
  var userinput=Number(document.getElementById('Complex_Input_Number').value);
  var result = make_tablet(userinput)
  document.getElementById('complex_assignment_operator_output').innerHTML= result;

}

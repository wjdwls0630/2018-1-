function firsthandler() {
  var userinput = prompt("현재는 몇 월 입니까?")
  if ((userinput <= 2 && userinput >= 1) || userinput == 12) {
    document.getElementById('firstoutput').innerHTML =
      '스키의 계절 겨울이네요!';
  } else if (userinput <= 5) {
    document.getElementById('firstoutput').innerHTML =
      '햇살 가득한 봄이네요!';
  } else if (userinput <= 8) {
    document.getElementById('firstoutput').innerHTML =
      '여행가기 좋은 여름이네요!';
  } else {
    document.getElementById('firstoutput').innerHTML =
      '독서의 계절 가을이네요!';;
  }
}

function secondhandler() {
  var id = 'easy1004';
  var pw = '1234';
  var userid = prompt('아이디는?');
  if (id === userid) {
    var userpw = prompt('비밀번호는?');
    if (pw === userpw) {
      document.getElementById('secondoutput').innerHTML =
        id + '님 반갑습니다!';
    } else {
      alert('비밀번호가 일치하지 않습니다!');
      location.reload();
    }
  } else {
    alert("아이디가 일치하지 않습니다!");
    location.reload();
  }
}

function thirdhandler() {
  var usersite = prompt('네이버, 다음, 네이트, 구글 중 즐겨 사용하는 사이트의 이름은?', '구글')
  var url;
  switch (usersite) {
    case '구글':
      url = 'www.google.com';
      break;
    case '네이버':
      url = 'www.naver.com';
      break;
    case '다음':
      url = 'www.daum.net';
      break;
    case '네이트':
      url = 'www.nate.com';
      break;
    default:
      alert("보기 중에 없는 사이트 입니다 다시 입력하십시오!");
  }
  if (url) {
    location.href = 'http://' + url;
  }
}

function fourthhandler() {
  var a = 1;
  var result = ''
  while (a <= 10) {
    result += '안녕하세요' + a + '<br>';
    a++;

  }
  result += '===The End===';
  document.getElementById('fourthoutput').innerHTML = result;
}

function fifthhandler() {
  var a = 20;
  var result = ''
  while (a >= 10) {
    if (a % 2 == 0) {
      result += "<span style= 'color : blue'>" + a + '</span><br>'

    } else {
      result += "<span style= 'color : red'>" + a + '</span></br>'
    }
    a--;
  }
  document.getElementById('fifthoutput').innerHTML = result;
}

function sixhandler() {
  do {
    var usernumber = prompt("0 에서 10 사이의 정수를 입력하세요!");
    document.getElementById('sixoutput').innerHTML =
      '입력된 숫자는 ' + usernumber;
  } while (usernumber < 5);

}

function sevenhandler() {
  var result = '';
  for (var i = 1; i <= 100; i++) {
    if (i % 5 == 0) {
      if (i % 7 == 0) {
        result += "<span style='color : aqua'>" + i + "</span><br>"
      } else {
        result += "<span style='color : red'>" + i + "</span><br>"
      }
    } else if(i%7==0){
      result += "<span style='color : green'>" + i + "</span><br>"
    }
    else {
      continue;
    }
  }
  document.getElementById('sevenoutput').innerHTML=result;
}

function eighthandler() {
  var result='for문 continue<br>';
  for (var i = 1; i < 10; i++) {
    if(i%2==0){
      continue;
    }
    result+='for문 반복'+i+'<br>'
  }
  result+='while문 continue<br>'
  var k=0;
  while (k<10) {
    k++
    if (k%2==0) {
      continue;
    }
    result+='while문 반복'+k+'<br>'
  }
document.getElementById('eightoutput').innerHTML=result;
}

function ninehandler() {
  var result = '';
  var tv = new Object();
  tv.color='white';
  tv.price=30000;
  tv.info=function () {
    result+="<h2>tv 객체 메서드 호출</h2>";
    result+="tv 색상 : "+this.color+"<br>";
    result+="tv 가격 : "+this.price+"<br>";
  }
  var car={
    color : 'black',
    price : 50000,
    info : function () {
      result+="<h2>car 객체 메서드 호출</h2>";
      result+="car 색상 : "+this.color+"<br>";
      result+="car 가격 : "+this.price+"<br>";
    }
  };
  tv.info();
  car.info();
  document.getElementById('nineoutput').innerHTML=result;
}

function convert_getDay(input){
  if (input==0) {
    result='일'
  }else if (input==1) {
    result='월'
  }else if (input==2) {
    result='화'
  }else if (input==3) {
    result='수'
  }else if (input==4) {
    result='목'
  }else if (input==5) {
    result='금'
  }else {
    result='토'
  }
  return result;
}
function tenhandler() {
  var result;
  var today = new Date(),
      birthday= new Date('1995/06/30'),
      updateDate= new Date(2018,05,10),
      endDay=new Date('2018/6/20'),
      diffDate= endDay-today;
  result+="<h2>오늘 날짜 정보</h2>"+"지금은 "+(today.getMonth()+1)+"월 "+today.getDate()+"일 "+convert_getDay(today.getDay())+"요일<br>"
  result+=today.getHours()+"시 "+today.getMinutes()+"분 "+today.getSeconds()+"초입니다."
  result+="<h2>생일 정보</h2>"+birthday.getFullYear()+"년 "+(birthday.getMonth()+1)+"월 "+birthday.getDate()+"일 "+convert_getDay(birthday.getDay())+"요일<br>"
  result+="<h2>작성 날짜 정보</h2>"+(updateDate.getMonth()+1)+"월 "+updateDate.getDate()+"일 "+convert_getDay(updateDate.getDay())+"요일<br>"
  result+="<h2>종강 까지 남은 날</h2>"+"D-day : "+(Math.ceil(diffDate/(1000*60*60*24)))+"일 남았습니다!"
  document.getElementById('tenoutput').innerHTML=result;

}

function elevenhandler() {
  var result='';
  var num = 2.1234;

var maxNum = Math.max(10, 5, 8, 30),
  minNum = Math.min(10, 5, 8, 30),
  roundNum = Math.round(num),
  floorNum = Math.floor(num),
  ceilNum = Math.ceil(num),
  rndNum = Math.random(),
  piNum = Math.PI;
result+="num = 2.1234<br>"
result+="Math.max(10,5,8,30) -> "+maxNum+"<br>";
result+="Math.min(10,5,8,30) -> "+minNum+"<br>";
result+="Math.round(num) -> "+roundNum+"<br>";
result+="Math.floor(num) -> "+floorNum+"<br>";
result+="Math.ceil(num) -> "+ceilNum+"<br>";
result+="Math.PI() -> "+piNum+"<br>";
result+="<h2>0~1 사이의 난수(Math.random())</h2>"+rndNum+"<br>"
result+="<h2>0~9 사이의 난수인 정수 - Math.floor(Math.random()*10)</h2>"+Math.floor(rndNum*10)+"<br>"
result+="<h2>30~100 사이의 난수인 정수 - Math.floor(Math.random()*71)+30</h2>"+(Math.floor(rndNum*71)+30)+"<br>"
result+="<h3>[a,b]사이의 정수인 난수 공식 Math.floor(Math.random()*(b-a+1))+30</h3>"

document.getElementById('elevenoutput').innerHTML=result;

}

function twelvehandler() {
  var result='';
  var list1 = new Array();
  var list2= [0,1,2];
  var list3=new Array(3,4,5);
  list1[0]=0;
  list1[1]=1;
  list1[2]=2;
  var list4=list1.concat(list3);
  result+="Array 객체의 타입은 "+typeof(list1)+"<br>"
  result+="join('value')<br> list1.join('!') -> "+list1.join('!')+"<br>리턴 되는 값의 타입은 "+typeof(list1.join('!'))+"<br>"
  result+="pop() : 마지막 인덱스에 저장된 데이터 삭제 , push(value) : 마지막 인덱스에 value값 추가<br>"
  result+="현재 리스트 "+list1+"<br> pop() 실행 후<br>";
  list1.pop();
  result+=list1+"<br> push(3) 실행 후<br>";
  list1.push(3);
  result+=list1;
  result+="<br>shift() : 첫 번째 인덱스에 저장된 데이터 삭제 , unshift(value) : 첫 번째 인덱스에 value값 추가<br>"
  result+="현재 리스트 "+list1+"<br> shift() 실행 후<br>";
  list1.shift();
  result+=list1+"<br> unshift(3) 실행 후<br>";
  list1.unshift(4);
  result+=list1;
  list1=list2;
  result+="<br>concat() : 두 개의 리스트를 하나의 리스트로 합침<br>"
  result+="list1 = [0,1,2], list3=[3,4,5] <br> list1.concat(list3) 실행 하면 "
  result+=list4;
  result+="<br>slice(start,end) start에서 end구간 [start,end]까지 잘라서 리턴<br>[0,1,2,3,4,5]에서 1번째에서 4번째까지 : list4.slice(1,4) <br>"
  result+=list4.slice(1,5)
  result+="<br>splice(시작번호, 제거할 요소의 수, 삭제된 요소 대신 추가할 요소, ...) : 리스트에서 지정 데이터를 삭제하고 그 구간에 새로운 데이터 삽입<br> list4 = [0,1,2,3,4,5]에서 list4.splice(1,2,'a','b') 실행<br>"
  list4.splice(1,2,"a","b")
  result+=list4;
  result+="<br>sort() : 리스트를 오름차순 정렬  reverse() : 데이터 순서 거꾸로 바꾼 후 리턴<br> list4=[0,'a','b',3,4,5] sort() 적용<br>"
  list4.sort();
  result+=list4;
  result+="<br>reverse() 적용 <br>"
  list4.reverse();
  result+=list4;
  result+="<br> length 로 하면 배열의 요소 개수를 number 객체로 리턴 , list4의 개수 6개<br>list4.length 실행 -> "
  result+=list4.length+"<br> list4.length의 타입 -> "+typeof(list4.length)

document.getElementById('twelveoutput').innerHTML=result;


}

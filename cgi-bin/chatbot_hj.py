#!/usr/bin/env python3
import cgi
from botengine import make_reply
# 입력 양식의 글자 추출하기 --- (※1)
form = cgi.FieldStorage()
# 메인 처리 --- (※2)
def main():
    m = form.getvalue("m", default="")
    if   m == "" : show_form()
    elif m == "say" : api_say()
# 사용자의 입력에 응답하기 --- (※3)
def api_say():
    print("Content-Type: text/plain; charset=euc-kr")
    print("")
    txt = form.getvalue("txt", default="")
    if txt == "": return
    res = make_reply(txt)
    print(res)
# 입력 양식 출력하기 --- (※4)
def show_form():
    print("Content-Type: text/html; charset=euc-kr")
    print("")
    print("""
<html>
	<head>
	<title>Page Title</title>
    <meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css" />
	<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
	<script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
	</head>	
		
	<body>
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <style>
        div  { padding:2px; margin:10px;}
        span { border-radius: 3px; background-color: white ; padding:2px; margin:5px;}
        .c { background-color: white; }
        .bot { text-align: left; text-indent: -2em; margin-left: 2em; }
        .usr { text-align: right;}
        .mys {background-color:white;}
        .myt {color: white;}
        h1{ background-color: #ffffff}
        

    </style>
    <div style="padding:50px;background-image: url('https://t1.daumcdn.net/cafeattach/1D7bO/bcccdbb61dad188ceb3a47a9a294b973853b1737');"> 
    <div data-role="ui-bar">
			<h1 class="ui-bar ui-corner-all"><font size="8" color="#003399" 
            face ="tvN Enjoystories Medium"><center> Frozen 
            </center></font></h1></div>
    
    

	  <div id="chat"></div>
    
    <input id="txt" size="30">
    <button class="ui-btn ui-btn-inline ui-btn-b" onclick="say()">올라프</button>
    
    <script>
    var url = "./chatbot_hj.py";
    <!--enter키로 내용 보내는 방법-->
    $(document).ready(function(){
       $("#txt").keypress(function (e) {
        if (e.which == 13){
                   say();
        }
    });
});
    function say() {
      var txt = $('#txt').val();
      $.get(url, {"m":"say","txt":txt},
        function(res) {
          var html = "<div class='usr'><span>" + esc(txt) +
            "</span>: &#127908;</div><div class='bot'> 	&#129419;:<span class='c'>" + 
            esc(res) + "</span></div>";
          $('#chat').html($('#chat').html()+html);
          $('#txt').val('').focus();
        });
    }
    function esc(s) {
        return s.replace('&', '&amp;').replace('<','&lt;')
                .replace('>', '&gt;');
    }
    </script>
	</body>
	</html>

    """)
main()
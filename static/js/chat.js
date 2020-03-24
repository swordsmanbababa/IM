var id = $('#id').text();

setInterval(function(){
    Push();
    FriendsRqs();
    //alert("setInterval called");
},3000);
function Push(){
    var datat = {'news':"test",'userid':id};
    $.ajax({
           type:'GET',
           url:"/room/message/receive",
           data:datat,
           success:function (result) {
//           alert(result);
           if(result != ""){
//           alert(result)
           var str='';
            str+='<li>'+
                    '<div class="nesHead"><img src="/static/img/6.jpg"/><span>'+id+'</span></div>'+
                    '<div class="news"><img class="jiao" src="/static/img/20170926103645_03_02.jpg">'+result+'</div>'+
                '</li>';
            $('.newsList').append(str);
            }

         }})

}
function FriendsRqs(){
    var datat = {'userid':id};
    $.ajax({
           type:'GET',
           url:"/iffriensreq",
           data:datat,
           success:function (result) {
           if(result!=''){
            var msg = "确定添加"+result+"为好友吗？";
            if (confirm(msg)==true){
            var data = {'userid':id,'to_userid':result};
            }
               $.ajax({
               type:'GET',
               url:"/addfriendsres",
               data:data,
             })
             }
         }})

}

$('#add').on('click',function(){
    var msg = "确定添加此人为好友吗？";
    if (confirm(msg)==true){
        var touserid=$('.qqBox').children('.BoxHead').children('.touserid').text();
        var datat = {'news':"test",'userid':id,'to_userid':touserid};
        $.ajax({
               type:'GET',
               url:"/addfriends",
               data:datat,
               success:function (result) {   }
             })
        alert('请求已发出！');
        return true;
    }else{
        return false;
    }
})

$('.conLeft li').on('click',function(){
		$(this).addClass('bg').siblings().removeClass('bg');
		var intername=$(this).children('.liRight').children('.intername').text();
		var touserid=$(this).children('.liRight').children('.id').text();
	//	$('.headName').text("7yu8i");
	    $('.qqBox').children('.BoxHead').children('.touserid').html(touserid);
        $('.qqBox').children('.context').children('.conRight').children('.Righthead').children('.headName').html(intername);
//	    $('#name').html(intername);

		$('.newsList').html('');

	})
$('.sendBtn').on('click',function(){
    var touserid = $('.qqBox').children('.BoxHead').children('.touserid').text();
	var datat = {'userid':id,'to_userid':touserid};
	var news=$('#dope').val();
	$.ajax({
        type:'GET',
        url:"/checkfriends",
        data:datat,
        success:function (result) {
            if(result!='ok'){
                $.DialogByZ.Alert({Title: "提示", Content: "他还不是您的好友，请添加。",BtnL:"确定",FunL:function(){$.DialogByZ.Close();}})
            }else{
                if(news==''){
                     alert('不能为空');
                }else{
                        $('#dope').val('');
                        var answer='';
                        answer+='<li>'+
                                    '<div class="answerHead"><img src="/static/img/tou.jpg"/></div>'+
                                    '<div class="answers"><img class="jiao" src="/static/img/jiao.jpg">'+news+'</div>'+
                                '</li>';
                        $('.newsList').append(answer);
                        $('.conLeft').find('li.bg').children('.liRight').children('.infor').text(news);
                        $('.RightCont').scrollTop($('.RightCont')[0].scrollHeight );
                        var data_id = {
                            'news':news,
                            'userid':id,
                            'to_userid':touserid}
                        $.ajax({
                           type:'GET',
                           url:"/room/message/send",
                           data:data_id,
                           success:function (result) {

                         }})

                 }
            }
        }

     })


})

$('.ExP').on('mouseenter',function(){
    $('.emjon').show();
})
$('.emjon').on('mouseleave',function(){
    $('.emjon').hide();
})
$('.emjon li').on('click',function(){
    var imgSrc=$(this).children('img').attr('src');
    var str="";
    str+='<li>'+
            '<div class="nesHead"><img src="/static/img/6.jpg"/></div>'+
            '<div class="news"><img class="jiao" src="/static/img/20170926103645_03_02.jpg"><img class="Expr" src="'+imgSrc+'"></div>'+
        '</li>';
    $('.newsList').append(str);
    $('.emjon').hide();
    $('.RightCont').scrollTop($('.RightCont')[0].scrollHeight );
})

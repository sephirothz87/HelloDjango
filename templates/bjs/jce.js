console.log('jce.js');


let createSubscriber = new Vue({
    el: '#createSubscriber',
    data: {
        'help':''
    }
});

$('#btnCreateSubscriber').click(
    function(){
        let qxwxId = $('#qxwxId').val();
        console.log(createSubscriber);
        if(!qxwxId || qxwxId == ''){
            createSubscriber.help='请输入企业微信ID';
            return;
        }
        createSubscriber.help='';
        
        $.ajax({
            type: "POST",
            url: "../jceApp/createSubscriber",
            data: {
                'qxwx_login_id':qxwxId
            },
            async: false,
            success: function(res){
                console.log(res);
                createSubscriber.help='添加成功';
            },
            error: function(res){
                createSubscriber.help='该用户已是订阅者';
            }
        });
    }
);

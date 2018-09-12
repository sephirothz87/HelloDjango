console.log('index.js');

const coreData = [
    { 'theme': 'blue' },
    { 'theme': 'red' },
    { 'theme': 'green' },
    { 'theme': 'yellow' }
]

const mockData = {
    'coreData': [
        {
            'title': 'Clients',
            'tValue': '4 589',
            // 'boxchart': '5,6,7,2,0,4,2,4,8,2,3,3,2'
        },
        {
            'title': 'Transactions',
            'tValue': '789',
            // 'boxchart': '1,2,6,4,0,8,2,4,5,3,1,7,5'
        },
        {
            'title': 'Income',
            'tValue': '$1 999,99'
        },
        {
            'title': 'Account',
            'tValue': '$19 999,99'
        }
    ]
}

let content = new Vue({
    el: '#content',
    data: mockData
});

$.ajax({
    type: "POST",
    // url: "server/test.php",
    url: "server/getCoreData.php",
    data: {},
    async: false,
    success: function(res){
        console.log(res);
        resData = JSON.parse(res);
        console.log(resData);
        // content.coreData[3]['value'] = resData[3]['tValue'];
        // content.coreData[3]['tValue'] = resData['resB'];
        content.coreData=resData;
    }
});

// console.log(content.core_data[0].title);
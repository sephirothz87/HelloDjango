console.log('index.js');

//ajax&vue.js
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
    el: '#coreData',
    data: mockData,
    // data: {
    //     'coreData':[]
    // },
    // data: {}
});

$.ajax({
    type: "POST",
    // url: "server/test.php",
    url: "getCoreData",
    data: {},
    async: false,
    success: function(res){
        console.log(res);
        // resData = JSON.parse(res);
        console.log(resData);
        // content.coreData[3]['value'] = resData[3]['tValue'];
        // content.coreData[3]['tValue'] = resData['resB'];
        content.coreData=mockData;
        // content.coreData=resData;
    }
});

// console.log(content.core_data[0].title);


//echart.js tree
let dom = document.getElementById("treeContainer");
let myChart = echarts.init(dom);
let app = {};
let option = null;



myChart.showLoading();
$.get('bjs/testTree2.json', function (data) {
    console.log(data);
    myChart.hideLoading();

    echarts.util.each(data.children, function (datum, index) {
        index % 2 === 0 && (datum.collapsed = true);
    });

    myChart.setOption(option = {
        legend: {
            type: 'scroll'
        },
        tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove'
        },
        series: [
            {
                type: 'tree',

                data: [data],

                top: '1%',
                left: '20%',
                bottom: '1%',
                right: '20%',

                symbolSize: 18,

                label: {
                    normal: {
                        position: 'left',
                        verticalAlign: 'middle',
                        align: 'right',
                        fontSize: 12
                    }
                },

                initialTreeDepth:2,

                leaves: {
                    label: {
                        normal: {
                            position: 'right',
                            verticalAlign: 'middle',
                            align: 'left'
                        }
                    }
                },

                expandAndCollapse: true,
                animationDuration: 550,
                animationDurationUpdate: 750
            }
        ]
    });
    if (option && typeof option === "object") {
        console.log('if');
        myChart.setOption(option, true);
    }
});

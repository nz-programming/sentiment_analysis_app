
const data_label =  dataset["labels"];
const data_average_polality = dataset["average_polality"]
const data_polality_json = dataset["polality_json"]
const data_keyword = dataset["keyword_count"]


// chart with chart.js
var context = document.getElementById("myChart");
var myLineChart  = new Chart(context, {
type: 'line',
data: {
    // labels: data.labels,
    labels: data_label,
    datasets: [{
        label: 'Sentiment Score',
        // data:data.data,
        data:data_average_polality,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255,99,132,1)',
        borderWidth: 1
    }]
},
options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            }
        }]
    }
}
});

// const polality_json = data.polality_json
// console.log(polality_json)
// const id = data.id
// console.log(id)


function clickHandler(click){
const points = myLineChart.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true);
if(points[0]){
    // console.log(points[0].datasetIndex)
    // console.log(points[0].index)

    // set index of cliked item on html
    const dataset = points[0].datasetIndex;
    const index = points[0].index;
    console.log(index)
    const label= myLineChart.data.labels[index];
    const keyword = data_keyword[index]
    const polality_json = data_polality_json[index]
    // console.log(polality_json)
    // console.log(polality_json["create_date"])
    // console.log(polality_json["create_date"]["0"])
    // console.log(typeof(polality_json["create_date"]))
    // console.log(typeof(polality_json["create_date"]["0"]))
    // // console.log(myLineChart.data.labels[index])
    const sample =  document.querySelector('.sample');
    const sample_2 =  document.querySelector('.sample_2');

    // grab html tag for user icon for sentiment score ranking
    const sent_icon_1 =  document.querySelector('.sent_icon_1');
    const sent_icon_2 =  document.querySelector('.sent_icon_2');
    const sent_icon_3 =  document.querySelector('.sent_icon_3');

    // grab html tag for sentiment score for sentiment score ranking
    const sent_score_1 =  document.querySelector('.sent_score_1');
    const sent_score_2 =  document.querySelector('.sent_score_2');
    const sent_score_3 =  document.querySelector('.sent_score_3');

    // grab html tag for text for sentiment score ranking
    const sent_text_1 =  document.querySelector('.sent_text_1');
    const sent_text_2 =  document.querySelector('.sent_text_2');
    const sent_text_3 =  document.querySelector('.sent_text_3');

    sample.innerText = label;
    sample_2.innerText = keyword;

    const sentiment_score = polality_json["sentiment_score"]

    // sort object accoring to sentiment score
    let arr = Object.keys(sentiment_score).map((e)=>({ key: e, value: sentiment_score[e] }));
    arr.sort(function(a,b){
        if(a.value < b.value) return 1;
        if(a.value > b.value) return -1;
        return 0;
    });

    // user icon for sentiment score ranking
    sent_icon_1.setAttribute('src', polality_json["profile_img"][arr[0].key]);
    sent_icon_2.setAttribute('src', polality_json["profile_img"][arr[1].key]);
    sent_icon_3.setAttribute('src', polality_json["profile_img"][arr[2].key]);

    // sentiment score for sentiment score ranking
    sent_score_1.innerText = polality_json["sentiment_score"][arr[0].key];
    sent_score_2.innerText = polality_json["sentiment_score"][arr[1].key];
    sent_score_3.innerText = polality_json["sentiment_score"][arr[2].key];

    // text for sentiment score ranking
    sent_text_1.innerText = polality_json["text"][arr[0].key];
    sent_text_2.innerText = polality_json["text"][arr[1].key];
    sent_text_3.innerText = polality_json["text"][arr[2].key];




}
}
myLineChart.canvas.onclick = clickHandler;
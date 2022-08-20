
const data_label =  dataset["labels"];
const data_average_polality = dataset["average_polality"]
const data_polality_json = dataset["polality_json"]
const data_keyword = dataset["keyword_count"]

// const data = JSON.parse('{{data_json|safe}}')

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
// console.log(click)
const points = myLineChart.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true);
// console.log(points)
if(points[0]){
    // console.log(points[0].datasetIndex)
    // console.log(points[0].index)
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
    const sample_3 =  document.querySelector('.sample_3');
    sample.innerText = label;
    sample_2.innerText = keyword;

    const sentimentscore = polality_json["sentiment_score"]
    console.log(sentimentscore)


    let arr = Object.keys(sentimentscore).map((e)=>({ key: e, value: sentimentscore[e] }));
    console.log(arr);
    arr.sort(function(a,b){
        if(a.value < b.value) return 1;
        if(a.value > b.value) return -1;
        return 0;
    });
    console.log(arr);
    let key_arr = Object.keys(arr);
    console.log(key_arr);


    sample_3.setAttribute('src', polality_json["profile_img"]["1"]);
    // sample_3.src = polality_json["profile_img"]["0"];
    console.log(sample_3);
}
}
myLineChart.canvas.onclick = clickHandler;
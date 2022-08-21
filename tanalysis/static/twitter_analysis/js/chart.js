const data_label =  dataset["labels"];
const data_average_polality = dataset["average_polality"]

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
// function return_variables(){
//     var chart_data = myLineChart;
//     return chart_data;
// }
// const polality_json = data.polality_json
// console.log(polality_json)
// const id = data.id
// console.log(id)



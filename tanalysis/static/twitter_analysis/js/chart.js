const create_date =  dataset["create_date"];
const sentiment_score = dataset["average_polality"];

// chart with chart.js
var context = document.getElementById("myChart");
var myLineChart  = new Chart(context, {
    type: 'line',
    data: {
        labels: create_date,
        datasets: [{
            label: 'Daily Average Sentiment Score',
            // data:data.data,
            data:sentiment_score,
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

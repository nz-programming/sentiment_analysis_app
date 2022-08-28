const create_date =  dataset["create_date"];
const sentiment_score = dataset["average_polality"];

// show analyzed period
const period_start =  document.querySelector(`.period_start`);
period_start.innerText = create_date[0];
const period_end =  document.querySelector(`.period_end`);
period_end.innerText = create_date[create_date.length - 1];

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
            y: {
                title: {
                    display: true,
                    text: 'Sentiment Score'
                },
                ticks: {
                    beginAtZero:true
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Date'
                },
            },
        }
    }
});

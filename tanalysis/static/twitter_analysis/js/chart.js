const create_date =  dataset["create_date"];
const sentiment_score = dataset["average_polality"];

console.log(typeof(create_date))
console.log(create_date)

const term_start =  document.querySelector(`.term_start`);
term_start.innerText = create_date[0];
const term_end =  document.querySelector(`.term_end`);
term_end.innerText = create_date[create_date.length - 1];

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

/* 

This file create the chart on index.html page

*/

const create_date =  dataset["create_date"];
const sentiment_score = dataset["average_polality"];
const number_tweet = dataset["number_tweet"];

// show analyzed period
const period_start =  document.querySelector(`.period_start`);
period_start.innerText = create_date[0];
const period_end =  document.querySelector(`.period_end`);
period_end.innerText = create_date[create_date.length - 1];

// create chart with chart.js
var context = document.getElementById("myChart").getContext('2d');
var myLineChart  = new Chart(context, {
    data: {
        labels: create_date,
        datasets: [{
            type: 'line',
            label: 'Average Sentiment Score',
            data:sentiment_score,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            yAxisID:"sentimentscoreChart",
            borderWidth: 1
        }, {
            type: 'bar',
            label: 'Number of Tweet',
            data:number_tweet,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235,  1)',
            yAxisID:"numbertweetChart",
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            "sentimentscoreChart": {
                type: "linear", 
                position: "left",
                title: {
                    display: true,
                    text: 'Sentiment Score'
                },
                ticks: {
                    max: 1,
                    min: -1,
                    beginAtZero:true,
                },
            },
            "numbertweetChart": {
                type: "linear",
                position: "right",
                title: {
                    display: true,
                    text: 'Number of Tweet'
                },
                ticks: {
                    beginAtZero:true,
                },
                grid: {
                    display: false,
                },
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

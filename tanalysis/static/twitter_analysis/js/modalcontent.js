// get data at the cliked point
function createModal(click){
    const points = myLineChart.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true);
    if (points[0]){
        // show modal
        let myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {});
        myModal.show();

        // get index of the cliked point
        const index = points[0].index;

        // create sentiment ranking and retweet ranking
        let showexampletweet = new showExampleTweet(index);
        // sentiment score ranking
        showexampletweet.setContent("sentiment");
        showexampletweet.setHtml();
        // number of retweet ranking
        showexampletweet.setContent("retweet");
        showexampletweet.setHtml();

        // create keyword chart

        let showmodalchart = new showModalChart(index);
        showmodalchart.setContent("keyword")
        showmodalchart.setVariable()
        showmodalchart.createKeyWordChart();
        showmodalchart.setContent("keyphrase")
        showmodalchart.setVariable()
        showmodalchart.createKeyPhraseChart();

        // createKeywordChart(index);
    }
}
myLineChart.canvas.onclick = createModal;
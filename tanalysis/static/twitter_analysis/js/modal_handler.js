/* 

This file integrate and call class and function to create modal content

*/

// get data at the cliked point
function createModal(click){
    const points = myLineChart.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true);
    if (points[0]){
        // show modal
        let myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {});
        myModal.show();

        // get index of the cliked point
        const index = points[0].index;

        // create ranking
        let creatmodalranking = new createModalRanking(index);
        // sentiment score ranking
        creatmodalranking.setContent("sentiment");
        creatmodalranking.createRanking();
        // number of retweet ranking
        creatmodalranking.setContent("retweet");
        creatmodalranking.createRanking();

        // create charts
        let createmodalchart = new createModalChart(index);
        // keyword chart
        createmodalchart.setContent("keyword")
        createmodalchart.setVariable()
        createmodalchart.createKeyWordChart();
        // keyphrase chart
        createmodalchart.setContent("keyphrase")
        createmodalchart.setVariable()
        createmodalchart.createKeyPhraseChart();
    }
}
myLineChart.canvas.onclick = createModal;
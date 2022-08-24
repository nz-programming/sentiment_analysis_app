// get data at the cliked point
function getIndex(click){
    const points = myLineChart.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true);
    if (points[0]){
        // show modal
        let myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {});
        myModal.show();
        // set value on modal
        const index = points[0].index;
        let createmodalcontent = new createModalContent(index);
        // set sentiment score ranking content
        createmodalcontent.setContent("sentiment");
        createmodalcontent.setHtml();
        // set number of retweet ranking content
        createmodalcontent.setContent("retweet");
        createmodalcontent.setHtml();
    }
}
myLineChart.canvas.onclick = getIndex;
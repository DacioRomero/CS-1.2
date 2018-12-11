var refreshButton = document.getElementById("refresh");
var paragraph = document.getElementById("paragraph");

function getNewParagrah() {
    refreshButton.classList.add("spin");

    axios.get("/api")
    .then(function(result) {
        paragraph.innerHTML = result.data;
        refreshButton.classList.remove("spin");
    })
    .catch(function(error) {
        console.error(error);
        refreshButton.classList.remove("spin");
    })
};

refreshButton.addEventListener("click", function(e) {
    getNewParagrah();
});

getNewParagrah();

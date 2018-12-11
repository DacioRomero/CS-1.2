var refreshButton = document.getElementById("refresh");
var paragraph = document.getElementById("paragraph");

function getNewParagrah() {
    refreshButton.classList.add("clicked");

    axios.get("/api")
    .then(function(result) {
        paragraph.innerHTML = result.data;
        refreshButton.classList.remove("clicked");
    })
    .catch(function(error) {
        console.error(error);
        refreshButton.classList.remove("clicked");
    })
};

refreshButton.addEventListener("click", function(e) {
    getNewParagrah();
});

getNewParagrah();

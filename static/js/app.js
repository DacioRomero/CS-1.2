var refreshButton = document.getElementById("refresh");
var paragraph = document.getElementById("paragraph");
var searchParams = new URLSearchParams(window.location.search);

function getNewParagrah() {
    refreshButton.classList.add("clicked");

    axios.get("/api?" + searchParams.toString())
    .then(function(result) {
        paragraph.innerHTML = result.data.paragraph;

        searchParams.set('seed', result.data.seed);
        setUrlParams();

        refreshButton.classList.remove("clicked");
    })
    .catch(function(error) {
        console.error(error);
        paragraph.innerHTML = "API ERRORED!"
        refreshButton.classList.remove("clicked");
    })
};

refreshButton.addEventListener("click", function(e) {
    searchParams.delete('seed')
    getNewParagrah();
});

function setUrlParams() {
    var url = [location.protocol, '//', location.host, location.pathname].join('');
    history.pushState("", "", url + "?" + searchParams.toString());
}

getNewParagrah();

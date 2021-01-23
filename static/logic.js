console.log("logic.js is running and executed by html")

function CloseMessage()
{
    var model = document.getElementById("update");

    if (model === null) return;
    
    $(model).remove();

}

function OpenLatest()
{
    window.open("https://www.github.com/TheE7Player/CSEV2/releases/latest");
    CloseMessage();
}

function ToggleLanguage()
{
    var shown = document.getElementById('dropdown-menu2').style.visibility;

    shown = (shown === "hidden") ? "visible" : "hidden";

    document.getElementById('dropdown-menu2').style.visibility = shown;

}

function ChangeLanguage(elm)
{
    // Get the current url
    let currentUrl = window.location;

    window.location = `/change/${elm.id}/0`;
}

// Filter the select (listbox) by text but prevent it from deleting itself
// https://stackoverflow.com/a/62896822
function filter() {
    var keyword = document.getElementById("search").value;
    var select = document.getElementById("select");

    if (select === null) return;

    for (var i = 0; i < select.length; i++) {
        var txt = select.options[i].text;
        if (!txt.startsWith(keyword)) {
            $(select.options[i]).attr('disabled', 'disabled').hide();
        } else {
            $(select.options[i]).removeAttr('disabled').show();
        }
    }
}

// https://stackoverflow.com/a/45010416
function removeActive() 
{
    $("li").each(function() {
        $(this).removeClass("is-active");
    }); 
    
    $("#client_event").addClass("is-hidden");
    $("#game_event").addClass("is-hidden");
    $("#server_event").addClass("is-hidden");
    $("#default").addClass("is-hidden");
}

function setActive(className)
{
    let target = "#" + className
    $(target).addClass("is-active");
    $(target).removeClass("is-hidden");
}

function GotoClient()
{
    removeActive();
    setActive("client_event")
}

function GotoGame()
{
    removeActive();
    setActive("game_event")
}

function GotoServer()
{
    removeActive();
    setActive("server_event")
}
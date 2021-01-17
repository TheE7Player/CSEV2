console.log("logic.js is running and executed by html")


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
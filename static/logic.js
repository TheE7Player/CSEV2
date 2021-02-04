console.log("logic.js is running and executed by html")

function CloseMessage()
{
    var model = document.getElementById("update");

    if (model === null) return;
    
    $(model).remove();
}

// Used to get typed in filter -> To keep track of what was typed in
function FetchSession()
{
    // Textbox -> search
    // Session Key to look for: "searchKey"
    // "searchKey" contains the text input that was used
    console.log("Fetching Session from Client-End")

    var inputText = document.getElementById('search').value;
    var word = sessionStorage.getItem("searchKey");

    if(word === null)
    {
        console.log("Ignoring session log for input text")
        return;
    }
    else
    {
        document.getElementById('search').value = word;
        
        // Run the filter as if we had typed it in (to get the other events filtered out)
        filter()
    }
}

function SetInputSession()
{
    // Session Key to look for: "searchKey"
    // "searchKey" contains the text input that was used
    var inputText = document.getElementById('search').value;
   
    if ( inputText.length < 1 )
        sessionStorage.removeItem("searchKey");
    else
        sessionStorage.setItem("searchKey", inputText);
}

function OpenLatest()
{
    let ver = document.getElementById('updateversion').dataset.version;

    if(ver === "None")
    {
        console.log("Update tag was left empty - ignoring")
        return;
    }

    window.open('https://github.com/TheE7Player/CSEV2/releases/tag/' + ver);
    
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

    var startsWithSearch = false;

    if(keyword.length > 0)
        if(keyword[0] == "=")
            startsWithSearch = true;

    if (select === null) return;

    for (var i = 0; i < select.length; i++) {
        
        var txt = select.options[i].text;
        
        $(select.options[i]).attr('disabled', 'disabled').hide();
             
        if (startsWithSearch)
        {
            if(txt.startsWith(keyword.substring(1)))
            $(select.options[i]).removeAttr('disabled').show();
        } 
        else if (txt.includes(keyword)) {
            $(select.options[i]).removeAttr('disabled').show();
        } 
    }

    // Set a session key to keep track of the input
    SetInputSession()
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
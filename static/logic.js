console.log("logic.js is running and executed by html")

function CloseMessage()
{
    $("#update")?.remove();
}

// Used to get typed in filter -> To keep track of what was typed in
function FetchSession()
{
    // Textbox -> search
    // Session Key to look for: "searchKey"
    // "searchKey" contains the text input that was used
    console.log("Fetching Session from Client-End")

    const inputText = $('#search').val();
    var word = sessionStorage.getItem("searchKey");

    if(word === null)
    {
        console.log("Ignoring session log for input text")
        return;
    }
    else
    {
        $('#search').val(word);
        
        // Run the filter as if we had typed it in (to get the other events filtered out)
        filter()
    }
}

function SetInputSession()
{
    // Session Key to look for: "searchKey"
    // "searchKey" contains the text input that was used
    const inputText = $('#search').val();
    const targetKey = "searchKey"

    if ( inputText.length < 1 ) { sessionStorage.removeItem(targetKey); return; }

    sessionStorage.setItem(targetKey, inputText);
}

function OpenLatest()
{
    const ver = $('#updateversion').dataset.version;

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
    $('#dropdown-menu2').toggle();
}

function ToggleStyleMode()
{
    fetch('/change-style').then(() => location.reload(true))
}

function ChangeLanguage(elm)
{
    window.location = `/change/${elm.id}/0`;
}

// Filter the select (listbox) by text but prevent it from deleting itself
// https://stackoverflow.com/a/62896822
function filter() {
    var keyword = $("#search").val();
    var select = $("#select").children();

    const startsWithSearch = keyword.length > 0 && keyword[0] === "=";

    if (!select || select.length < 1) return;

    var txt = null;
    const startsWithCondition = keyword.substring(1);
    const len = select.length

    for (var i = 0; i < len; i++) {
        
        txt = $(select[i]).text();
        
        $(select[i]).attr('disabled', 'disabled').hide();
            
        if((startsWithSearch && txt.startsWith(startsWithCondition)) || txt.includes(keyword)) $(select[i]).removeAttr('disabled').show();
    }

    // Set a session key to keep track of the input
    SetInputSession()
}

// https://stackoverflow.com/a/45010416
function removeActive() 
{
    $("li").each(function() { $(this).removeClass("is-active"); }); 
    $("#client_event").addClass("is-hidden");
    $("#game_event").addClass("is-hidden");
    $("#server_event").addClass("is-hidden");
    $("#default").addClass("is-hidden");
}

function setActive(className)
{
    //let target = "#" + className
    $(className).addClass("is-active");
    $(className).removeClass("is-hidden");
}

function GotoClient()
{
    removeActive();
    setActive("#client_event")
}

function GotoGame()
{
    removeActive();
    setActive("#game_event")
}

function GotoServer()
{
    removeActive();
    setActive("#server_event")
}
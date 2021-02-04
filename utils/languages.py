# Languages.py - Holds texts to support different languages

# Flags found from: https://www.iconfinder.com/search/?designer=Mr.hopnguyen&q=flag

DEFAULT_LANGUAGE = "ENG"

def IfValidSupport(lang: str) -> bool:

    supportedLanguages = ["ENG", "ESP", "POL", "RUS", "POR"]

    return True if lang in supportedLanguages else False


def GetSupportedList():
    return {
            'English': 'ENG', 
            'Español': 'ESP',
            'Русский': 'RUS',
            'Polski': 'POL',
            'Português': 'POR'
           }

def GetLanguage(lang: str):

    LANG = {}

    """
    RULE: The language must be 3 characters long and in caps/uppercase

    English (UK/US/AU etc) -> "ENG"
    Russian -> "RUS"
    German -> "GER"
    """

    # English Translations
    LANG['ENG'] = {

        'Title': "English",
        "Shorthand": "ENG",
        'ChangeError': "A fault occured while attempting to change a language",
        'ChangeErrorSubtext': "Return back",
        'Version': 'Version',
        'NoEvent': 'No Event Selected',
        'EventSubText':"Please select an event from the side bar",

        'UpdateMessageA': "You are running an",
        'UpdateMessageB': "older edition",
        'UpdateMessageC': "of this program - a newer one exists",
        'UpdateMessageD': "here",

        'SearchPlaceHolder': "Enter event here",

        'Game':"Game Event", "Client":"Client Event", "Server":"Server Event",
        'NotClient': "Sorry this event doesn't invoke from the Player",
        'NotGame': "Sorry this event doesn't invoke from the Game Mode",
        'NotServer':" Sorry this event doesn't invoke from the Server",

        "InformationHeader": "Information:",

        "HintYes": "Yes", "HintNo": "No",

        "PlayerHint": "Does player cause the event to trigger?",
        "GameHint": "Does the game or game type cause the event to trigger?",
        "ServerHint": "Does the server invoke the event to trigger?",

        "LanguageDemo": "Are you able to read this text perfectly fine? If so press Yes or press No to revert",

        "NoArgumentsTitle": "This event is just an empty invoker",
        "NoArgumentsText": "That means that this event doesn't pass or carry any information - It just invokes the event argumentless.",
        "ArgumentID": "Param Order",
        "ArgumentName": "Param Name",
        "ArgumentType": "Param Type",
        "ArgumentComment": "Param Comment"
    }

    # Spanish Translation ~ Thank you Vulc4n#9999 (302235332391206914)
    LANG['ESP'] = {

        'Title': "Español",
        "Shorthand": "ESP",
        'ChangeError': "Ocurrió un error al intentar cambiar de idioma",
        'ChangeErrorSubtext': "Retroceder",
        'Version': 'Versión',
        'NoEvent': 'Ningun evento seleccionado',
        'EventSubText':"Por favor selecciona un evento de la lista",

        'UpdateMessageA': "Estás usando una",
        'UpdateMessageB': "versión antigua",
        'UpdateMessageC': "del programa - existe una nueva",
        'UpdateMessageD': "aquí",

        'SearchPlaceHolder': "Busca un evento aquí",

        'Game':"Evento del Juego", 
        "Client":"Evento del Cliente", 
        "Server":"Evento del Servidor",

        'NotClient': "Lo sentimos, este evento no es invocado desde el Jugador",
        'NotGame': "Lo sentimos, este evento no es invocado desde el Modo de Juego",
        'NotServer':"Lo sentimos, este evento no es invocado desde el Servidor",

        "InformationHeader": "Información:",

        "HintYes": "Si", "HintNo": "No",

        "PlayerHint": "¿El jugador provoca este evento?",
        "GameHint": "¿El juego o modo de juego provocan este evento?",
        "ServerHint": "¿El servidor provoca este evento?",

        "LanguageDemo": "¿Puedes leer este texto sin problemas? Si puedes, presiona SI, en caso no puedas, presiona NO para cancelar",
        "NoArgumentsTitle": "Este evento es solo un invocador vacío",
        "NoArgumentsText": "Esto significa que este evento no puede ni almacenar ni pasar ninguna información - Tan solo invoca un evento sin argumentos.",
        "ArgumentID": "Orden del Parámetro",
        "ArgumentName": "Nombre del Parámetro",
        "ArgumentType": "Tipodel Parámetro",
        "ArgumentComment": "Comentario acerca del Parámetro"
    }

    # Polish Translation  ~ Thank you Helosx#1288 (378965373682188288)
    LANG['POL'] = {

        'Title': "Polski",
        "Shorthand": "POL",
        'ChangeError': "Wystąpił błąd podczas zmiany języka",
        'ChangeErrorSubtext': "Powrót",
        'Version': 'Wersja',
        'NoEvent': 'Nie wybrano zdarzenia',
        'EventSubText':"Wybierz zdarzenie z listy",

        'UpdateMessageA': "Korzystasz ze",
        'UpdateMessageB': "starszej wersji",
        'UpdateMessageC': "tego programu - nowsza wersja jest dostępna",
        'UpdateMessageD': "tutaj",

        'SearchPlaceHolder': "Wyszukaj zdarzenie",

        'Game':"Zdarzenie Gry", "Client":"Zdarzenie Gracza", "Server":"Zdarzenie Serwerowe",
        'NotClient': "To zdarzenie nie jest wywoływane przez Gracza",
        'NotGame': "To zdarzenie nie jest wywoływane przez Grę",
        'NotServer': "To zdarzenie nie jest wywoływane przez Serwer",

        "InformationHeader": "Informacje:",

        "HintYes": "Tak", "HintNo": "Nie",

        "PlayerHint": "Czy gracz wywołuje to zdarzenie?",
        "GameHint": "Czy gra wywołuje to zdarzenie?",
        "ServerHint": "Czy serwer wywołuje to zdarzenie?",

        "LanguageDemo": "Jesteś w stanie przeczytać ten tekst? Naciśnij Tak aby potwierdzić lub Nie aby cofnąć",
        "NoArgumentsTitle": "To zdarzenie jest pustym wywoływaczem",
        "NoArgumentsText": "Oznacza to, że zdarzenie nie przekazuje ani nie przechowuje żadnych informacji - poprostu wywołuje zdarzenie bez żadnych argumentów",
        "ArgumentID": "Kolejność",
        "ArgumentName": "Nazwa Parametru",
        "ArgumentType": "Typ Parametru",
        "ArgumentComment": "Komentarz"
    }

    # Russian Translation ~ Thank you DMax#3317   (443364273243160577)
    LANG['RUS'] = {

        'Title': "Русский",
        "Shorthand": "RUS",
        'ChangeError': "При попытке изменить язык произошла ошибка",
        'ChangeErrorSubtext': "Вернуться назад",
        'Version': 'Версия',
        'NoEvent': 'Нет выбранного события',
        'EventSubText':"Пожалуйста, выберите событие из боковой панели",

        'UpdateMessageA': "Вы используете",
        'UpdateMessageB': "старую версию",
        'UpdateMessageC': "этой программы - более новая версия находится",
        'UpdateMessageD': "здесь",

        'SearchPlaceHolder': "Введите сюда событие",

        'Game':"Игровое событие", "Client":"Клиентское событие", "Server":"Серверное событие",
        'NotClient': "Извините, это событие не вызывается из игрока",
        'NotGame': "Извините, это событие не вызывается из игры",
        'NotServer':"Извините, это событие не вызывается из сервера",

        "InformationHeader": "Информация:",

        "HintYes": "Да", "HintNo": "Нет",

        "PlayerHint": "Вызывает ли игрок это событие?",
        "GameHint": "Вызывает ли игра это событие?",
        "ServerHint": "Вызывает ли сервер это событие?",

        "LanguageDemo": "Можете ли Вы прочитать этот текст? Если можете, нажмите Да. В противном случае нажмите нет",
        "NoArgumentsTitle": "Это пустое событие",
        "NoArgumentsText": "Это значит, что событие не содержит никакой информации. Оно вызывается без аргументов.",
        "ArgumentID": "Номер аргумента",
        "ArgumentName": "Имя аргумента",
        "ArgumentType": "Тип аргумента",
        "ArgumentComment": "Описание аргумента"
    }

    # Portuguese Translation ~ Thank you Gela-1511#9299 (244159872004915201)
    LANG['POR'] = {

        'Title': "Português",
        "Shorthand": "POR",
        'ChangeError': "Ocorreu um erro ao trocar de idioma",
        'ChangeErrorSubtext': "Retroceder",
        'Version': 'Versão',
        'NoEvent': 'Nenhum evento selecionado',
        'EventSubText':"Por favor seleciona um evento da lista",

        'UpdateMessageA': "Estás a usar uma",
        'UpdateMessageB': "versão anterior",
        'UpdateMessageC': "deste programa - existe uma nova",
        'UpdateMessageD': "aqui",

        'SearchPlaceHolder': "Insira o evento aqui",

        'Game':"Evento de Jogo", "Client":"Evento de Cliente", "Server":"Evento de Servidor",
        'NotClient': "O evento em questão não é chamado pelo Jogador",
        'NotGame': "O evento em questão não é chamado pelo Modo de Jogo",
        'NotServer':"O evento em questão não é chamado pelo Servidor",

        "InformationHeader": "Informação:",

        "HintYes": "Sim", "HintNo": "Não",

        "PlayerHint": "O jogador invoca o evento?",
        "GameHint": "O jogo ou o modo de jogo invoca o evento?",
        "ServerHint": "O servidor invoca o evento?",

        "LanguageDemo": "És capaz de ler este texto perfeitamente? Se sim, pressiona Sim, senão pressiona Não para reverter",

        "NoArgumentsTitle": "Este evento é um invocador vazio",
        "NoArgumentsText": "Este evento não passa nem possui qualquer tipo de informação - Só é possível ser invocado.",
        "ArgumentID": "Ordem do Parâmetro",
        "ArgumentName": "Nome do Parâmetro",
        "ArgumentType": "Tipo de Parâmetro",
        "ArgumentComment": "Comentário do Parâmetro"
    }


    result = None

    try:
        result = LANG[lang]
    except:
        print("Failed to find support for:", lang)

    return result
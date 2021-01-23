# Languages.py - Holds texts to support different languages

# Flags found from: https://www.iconfinder.com/search/?designer=Mr.hopnguyen&q=flag

def IfValidSupport(lang: str) -> bool:

    supportedLanguages = ["ENG", "ESP", "POL", "RUS"]

    return True if lang in supportedLanguages else False


def GetSupportedList():
    return {
            'English': 'ENG', 
            'Español': 'ESP',
            'Русский': 'RUS',
            'Polski': 'POL'
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

        "LanguageDemo": "Are you able to read this text perfectly fine? If so press Yes or press No to revert"
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

        'Game':"Evento del Juego", "Cliente":"Evento del Cliente", "Servidor":"Evento del Servidor",
        'NotClient': "Lo sentimos, este evento no es implementado desde el Jugador",
        'NotGame': "Lo sentimos, este evento no es implementado desde el Modo de Juego",
        'NotServer':"Lo sentimos, este evento no es implementado desde el Servidor",

        "InformationHeader": "Información:",

        "HintYes": "Si", "HintNo": "No",

        "PlayerHint": "¿El jugador provoca este evento?",
        "GameHint": "¿El juego o modo de juego provocan este evento?",
        "ServerHint": "¿El servidor provoca este evento?",

        "LanguageDemo": "¿Puedes leer este texto sin problemas? Si puedes, presiona SI, en caso no puedas, presiona NO para cancelar"
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

        "LanguageDemo": "Jesteś w stanie przeczytać ten tekst? Naciśnij Tak aby potwierdzić lub Nie aby cofnąć"
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

        "LanguageDemo": "Можете ли Вы прочитать этот текст? Если можете, нажмите Да. В противном случае нажмите нет"
    }
    result = None

    try:
        result = LANG[lang]
    except:
        print("Failed to find support for:", lang)

    return result
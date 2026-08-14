from enum import StrEnum


class Language(StrEnum):
    RU = "ru"
    EN = "en"
    HY = "hy"


class Branch(StrEnum):
    FIRST = "branch_1"
    SECOND = "branch_2"
    THIRD = "branch_3"


LANGUAGE_NAMES = {
    Language.RU: "🇷🇺 Русский",
    Language.EN: "🇬🇧 English",
    Language.HY: "🇦🇲 Հայերեն",
}

BRANCH_NAMES = {
    Branch.FIRST: {
        Language.RU: "Филиал 1",
        Language.EN: "Branch 1",
        Language.HY: "Մասնաճյուղ 1",
    },
    Branch.SECOND: {
        Language.RU: "Филиал 2",
        Language.EN: "Branch 2",
        Language.HY: "Մասնաճյուղ 2",
    },
    Branch.THIRD: {
        Language.RU: "Филиал 3",
        Language.EN: "Branch 3",
        Language.HY: "Մասնաճյուղ 3",
    },
}

TEXTS = {
    "welcome_choose_language": {
        Language.RU: (
            "Здравствуйте! Я виртуальный помощник стоматологической клиники Implantum.\n\n"
            "Hello! I am the virtual assistant of Implantum dental clinic.\n\n"
            "Բարև ձեզ։ Ես Implantum ստոմատոլոգիական կլինիկայի վիրտուալ օգնականն եմ։\n\n"
            "Выберите язык / Choose your language / Ընտրեք լեզուն։"
        ),
    },
    "choose_language": {
        Language.RU: "Выберите язык:",
        Language.EN: "Choose your language:",
        Language.HY: "Ընտրեք լեզուն։",
    },
    "choose_branch": {
        Language.RU: "Выберите интересующий вас филиал:",
        Language.EN: "Choose the branch you are interested in:",
        Language.HY: "Ընտրեք ձեզ հետաքրքրող մասնաճյուղը։",
    },
    "language_changed_greeting": {
        Language.RU: "Язык изменён! Чем могу помочь?",
        Language.EN: "Language changed! How can I help you?",
        Language.HY: "Լեզուն փոխված է։ Ինչպե՞ս կարող եմ օգնել։",
    },
    "branch_selected": {
        Language.RU: "Вы выбрали: {branch}. Чем могу помочь?",
        Language.EN: "You selected: {branch}. How can I help you?",
        Language.HY: "Դուք ընտրել եք՝ {branch}։ Ինչպե՞ս կարող եմ օգնել։",
    },
    "greeting": {
        Language.RU: (
            "Здравствуйте! Я виртуальный помощник стоматологической клиники Implantum. "
            "Чем могу помочь?"
        ),
        Language.EN: (
            "Hello! I am the virtual assistant of Implantum dental clinic. "
            "How can I help you?"
        ),
        Language.HY: (
            "Բարև ձեզ։ Ես Implantum ստոմատոլոգիական կլինիկայի վիրտուալ օգնականն եմ։ "
            "Ինչպե՞ս կարող եմ օգնել։"
        ),
    },
    "appointment": {
        Language.RU: "🦷 Записаться на приём",
        Language.EN: "🦷 Book an appointment",
        Language.HY: "🦷 Գրանցվել այցի",
    },
    "help_button": {
        Language.RU: "ℹ️ Помощь",
        Language.EN: "ℹ️ Help",
        Language.HY: "ℹ️ Օգնություն",
    },
    "change_language": {
        Language.RU: "🌐 Сменить язык",
        Language.EN: "🌐 Change language",
        Language.HY: "🌐 Փոխել լեզուն",
    },
    "change_branch": {
        Language.RU: "🏥 Выбрать филиал",
        Language.EN: "🏥 Choose a branch",
        Language.HY: "🏥 Ընտրել մասնաճյուղ",
    },
    "menu_placeholder": {
        Language.RU: "Выберите действие",
        Language.EN: "Choose an action",
        Language.HY: "Ընտրեք գործողությունը",
    },
    "help": {
        Language.RU: (
            "Я помогу записаться на приём и узнать информацию о клинике. "
            "Выберите нужный пункт в меню."
        ),
        Language.EN: (
            "I can help you book an appointment and learn more about the clinic. "
            "Choose an option from the menu."
        ),
        Language.HY: (
            "Ես կօգնեմ գրանցվել այցի և տեղեկանալ կլինիկայի մասին։ "
            "Ընտրեք անհրաժեշտ կետը ցանկից։"
        ),
    },
    "appointment_soon": {
        Language.RU: "Сценарий записи на приём скоро будет доступен.",
        Language.EN: "The appointment flow will be available soon.",
        Language.HY: (
            "Այցի գրանցման հնարավորությունը շուտով հասանելի կլինի։ Այստեղ կավելացնենք "
            "ծառայության, բժշկի, ամսաթվի և ժամի ընտրությունը։"
        ),
    },
}


def t(key: str, language: Language) -> str:
    return TEXTS[key][language]


def branch_name(branch: Branch, language: Language) -> str:
    return BRANCH_NAMES[branch][language]

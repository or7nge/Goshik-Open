TOKEN = ''
BOT_STATUS = 'на тебя'
SERVER_ID = 553839993739804692
GOSHIK_ID = 702472488600207371

REACT_ROLES = {
    'role_csgo': 750050307458859009,
    'role_r6': 750052190915264543,
    'role_fortnite': 587215830677454863,
    'role_minecraft': 750352560338108466,
    'role_thunder': 793848511569068062,
    'role_valorant': 880719378365153331,
    'role_rocket': 766317865271820308,
    'role_terraria': 750052115442827264,
    'role_krunker': 880719080397635614,
    'role_gachi': 835208156493119538,
    'role_roblox': 881273818084179978,
    'role_anime': 893509875181715586,
    'role_amongus': 933683953930469416,
    'role_sot': 939446869841563718,
    'role_cycle': 954680980780748820,
}
MESSAGE_ROLES = 880792819034357811

ANSWER_BALL = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется — «да»', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят — «да»', 'Да', 'Пока не ясно, попробуй снова',
               'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ — «нет»', 'По моим данным — «нет»', 'Перспективы не очень хорошие', 'Весьма сомнительно']
ANSWER_BEN = ['ЙЕЕЕЕЕЕС', 'НННОУ', 'ХО-ХО-ХО', 'БЭЭЭЭЭЭ']
ANSWER_COIN = ['🦅 Орёл', '🟡 Решка']

CHANNEL_MEMES = 710052934150258768
CHANNEL_CHAT = 553839994192658448
CHANNEL_GOSHIK = 779682620249735191
CHANNEL_MEMEGEN = 786856984950472754
CHANNEL_MAIN = 553839994192658448

VC_START = 887043266749546506
VC_AFK = 884731929507807303

ROLE_BOTER = 767726874506821672
ROLE_ADMIN = 587217034614669312
ROLE_MUTER = 934147547986001991

MONEY_FOR_MSG = 1
MONEY_FOR_MEME = 2
MONEY_FOR_VC = 1

MONEY_MAX_MSG = 8
MONEY_MAX_VC = 8
MONEY_MAX_VC = 20


class ShopItem():
    def __init__(self, name, price, desc):
        self.name = name
        self.price = price
        self.desc = desc


SHOP_ITEMS = [
    ShopItem('Роль Багатый', 0, 'Роль ...'),
    ShopItem('Своя роль', 0, 'Роль с твоим цветом и названием'),
    ShopItem('Свой канал', 0, 'Канал, в котором ты админ'),
    ShopItem('Своя команда', 0, 'Сделаю любую команду в Гошика'),
    ShopItem('Писать от Гошика', 0, 'Право писать от аккаунта Гошика'),
    ShopItem('Изменить ник любого человека', 0,
             'Изменить ник любого человека на сервере без предупреждения'),
]

# -*- coding: utf-8 -*-
"""Constant lookup tables for hdate modules."""

from collections import namedtuple

# Joined Parash flags
JOIN_FLAGS = [
    [
        [1, 1, 1, 1, 0, 1, 1],  # 1 be erez israel
        [1, 1, 1, 1, 0, 1, 0],  # 2
        [1, 1, 1, 1, 0, 1, 1],  # 3
        [1, 1, 1, 0, 0, 1, 0],  # 4
        [1, 1, 1, 1, 0, 1, 1],  # 5
        [0, 1, 1, 1, 0, 1, 0],  # 6
        [1, 1, 1, 1, 0, 1, 1],  # 7
        [0, 0, 0, 0, 0, 1, 1],  # 8
        [0, 0, 0, 0, 0, 0, 0],  # 9
        [0, 0, 0, 0, 0, 1, 1],  # 10
        [0, 0, 0, 0, 0, 0, 0],  # 11
        [0, 0, 0, 0, 0, 0, 0],  # 12
        [0, 0, 0, 0, 0, 0, 1],  # 13
        [0, 0, 0, 0, 0, 1, 1]   # 14
    ],
    [
        [1, 1, 1, 1, 0, 1, 1],  # 1 in diaspora
        [1, 1, 1, 1, 0, 1, 0],  # 2
        [1, 1, 1, 1, 1, 1, 1],  # 3
        [1, 1, 1, 1, 0, 1, 0],  # 4
        [1, 1, 1, 1, 1, 1, 1],  # 5
        [0, 1, 1, 1, 0, 1, 0],  # 6
        [1, 1, 1, 1, 0, 1, 1],  # 7
        [0, 0, 0, 0, 1, 1, 1],  # 8
        [0, 0, 0, 0, 0, 0, 0],  # 9
        [0, 0, 0, 0, 0, 1, 1],  # 10
        [0, 0, 0, 0, 0, 1, 0],  # 11
        [0, 0, 0, 0, 0, 1, 0],  # 12
        [0, 0, 0, 0, 0, 0, 1],  # 13
        [0, 0, 0, 0, 1, 1, 1]   # 14
    ]
]

DIGITS = [
    [u" ", u"א", u"ב", u"ג", u"ד", u"ה", u"ו", u"ז", u"ח", u"ט"],
    [u"ט", u"י", u"כ", u"ל", u"מ", u"נ", u"ס", u"ע", u"פ", u"צ"],
    [u" ", u"ק", u"ר", u"ש", u"ת"]
]

DAYS_TABLE = [
    [   # begin english long
        [u"Sunday", u"Monday", u"Tuesday", u"Wednesday", u"Thursday",
         u"Friday", u"Saturday"],
        # begin english short
        [u"Sun", u"Mon", u"Tue", u"Wed", u"Thu", u"Fri", u"Sat"],
    ],
    [   # begin hebrew long
        [u"ראשון", u"שני", u"שלישי", u"רביעי", u"חמישי", u"שישי", u"שבת"],
        # begin hebrew short
        [u"א", u"ב", u"ג", u"ד", u"ה", u"ו", u"ש"]
    ]
]

PARASHAOT = [
    [  # begin english
        u"none", u"Bereshit", u"Noach",
        u"Lech-Lecha", u"Vayera", u"Chayei Sara",
        u"Toldot", u"Vayetzei", u"Vayishlach",
        u"Vayeshev", u"Miketz", u"Vayigash",     # 11
        u"Vayechi", u"Shemot", u"Vaera",
        u"Bo", u"Beshalach", u"Yitro",
        u"Mishpatim", u"Terumah", u"Tetzaveh",     # 20
        u"Ki Tisa", u"Vayakhel", u"Pekudei",
        u"Vayikra", u"Tzav", u"Shmini",
        u"Tazria", u"Metzora", u"Achrei Mot",
        u"Kedoshim", u"Emor", u"Behar",        # 32
        u"Bechukotai", u"Bamidbar", u"Nasso",
        u"Beha'alotcha", u"Sh'lach", u"Korach",
        u"Chukat", u"Balak", u"Pinchas",      # 41
        u"Matot", u"Masei", u"Devarim",
        u"Vaetchanan", u"Eikev", u"Re'eh",
        u"Shoftim", u"Ki Teitzei", u"Ki Tavo",      # 50
        u"Nitzavim", u"Vayeilech", u"Ha'Azinu",
        u"Vezot Habracha",                             # 54
        u"Vayakhel-Pekudei", u"Tazria-Metzora", u"Achrei Mot-Kedoshim",
        u"Behar-Bechukotai", u"Chukat-Balak", u"Matot-Masei",
        u"Nitzavim-Vayeilech"],
    [     # begin hebrew
        u"none", u"בראשית", u"נח",
        u"לך לך", u"וירא", u"חיי שרה",
        u"תולדות", u"ויצא", u"וישלח",
        u"וישב", u"מקץ", u"ויגש",  # 11
        u"ויחי", u"שמות", u"וארא",
        u"בא", u"בשלח", u"יתרו",
        u"משפטים", u"תרומה", u"תצוה",  # 20
        u"כי תשא", u"ויקהל", u"פקודי",
        u"ויקרא", u"צו", u"שמיני",
        u"תזריע", u"מצורע", u"אחרי מות",
        u"קדושים", u"אמור", u"בהר",  # 32
        u"בחוקתי", u"במדבר", u"נשא",
        u"בהעלתך", u"שלח", u"קרח",
        u"חקת", u"בלק", u"פנחס",  # 41
        u"מטות", u"מסעי", u"דברים",
        u"ואתחנן", u"עקב", u"ראה",
        u"שופטים", u"כי תצא", u"כי תבוא",  # 50
        u"נצבים", u"וילך", u"האזינו",
        u"וזאת הברכה",  # 54
        u"ויקהל-פקודי", u"תזריע-מצורע", u"אחרי מות-קדושים",
        u"בהר-בחוקתי", u"חוקת-בלק", u"מטות מסעי",
        u"נצבים-וילך"]
]

HEBREW_MONTHS = [
    [  # begin english
        u"Tishrei", u"Cheshvan", u"Kislev", u"Tevet",
        u"Sh'vat", u"Adar", u"Nisan", u"Iyyar",
        u"Sivan", u"Tammuz", u"Av", u"Elul", u"Adar I",
        u"Adar II"
    ],
    [  # begin hebrew
        u"תשרי", u"חשון", u"כסלו", u"טבת", u"שבט", u"אדר", u"ניסן", u"אייר",
        u"סיון", u"תמוז", u"אב", u"אלול", u"אדר א", u"אדר ב"
    ]
]

GREGORIAN_MONTHS = [  # NOT IN USE
    [
        u"January", u"February", u"March",
        u"April", u"May", u"June",
        u"July", u"August", u"September",
        u"October", u"November", u"December"
    ],
    [
        u"Jan", u"Feb", u"Mar", u"Apr", u"May",
        u"Jun", u"Jul", u"Aug", u"Sep", u"Oct",
        u"Nov", u"Dec"
    ]
]


def year_is_after(year):
    '''
    Return a lambda function that checks that a given HDate object's hebrew
    year is after the requested year.
    '''
    return lambda x: x._h_year > year


def year_is_before(year):
    '''
    Return a lambda function that checks that a given HDate object's hebrew
    year is before the requested year.
    '''
    return lambda x: x._h_year < year


def move_if_not_on_dow(original, replacement, dow_not_orig, dow_replacement):
    '''
    Return a lambda function that checks that either the original day does not
    fall on a given weekday, or that the replacement day does fall on the
    expected weekday.
    '''
    return lambda x: (
        (x._h_day == original and x._gdate.weekday() != dow_not_orig) or
        (x._h_day == replacement and x._gdate.weekday() == dow_replacement))


HOLIDAY = namedtuple("HOLIDAY", [
    "index", "type", "name", "date", "israel_diaspora", "date_functions_list",
    "english", "hebrew_long", "hebrew_short"])

HOLIDAYS = (
    HOLIDAY(1, 1, "rosh_hashana_i", (1, 1), "", [],
            u"Rosh Hashana I", u"א' ראש השנה", u"א ר\"ה"),
    HOLIDAY(2, 1, "rosh_hashana_ii", (2, 1), "", [],
            u"Rosh Hashana II", u"ב' ראש השנה", u"ב' ר\"ה"),
    HOLIDAY(3, 5, "tzom_gedaliah", ([3, 4], 1), "",
            [move_if_not_on_dow(3, 4, 5, 6)],
            u"Tzom Gedaliah", u"צום גדליה", u"צום גדליה"),
    HOLIDAY(4, 1, "yom_kippur", (10, 1), "", [],
            u"Yom Kippur", u"יום הכפורים", u"יוה\"כ"),
    HOLIDAY(5, 1, "sukkot", (15, 1), "", [],
            u"Sukkot", u"סוכות", u"סוכות"),
    HOLIDAY(6, 3, "hol_hamoed_sukkot", (16, 1), "ISRAEL", "",
            u"Hol hamoed Sukkot", u"חול המועד סוכות", u"חוה\"מ סוכות"),
    HOLIDAY(6, 3, "hol_hamoed_sukkot", ([17, 18, 19, 20], 1), "", "",
            u"Hol hamoed Sukkot", u"חול המועד סוכות", u"חוה\"מ סוכות"),
    HOLIDAY(7, 3, "hoshana_raba", (21, 1), "", [],
            u"Hoshana Raba", u"הושענא רבה", u"הוש\"ר"),
    HOLIDAY(8, 1, "simchat_torah", (23, 1), "DIASPORA", [],
            u"Simchat Torah", u"שמחת תורה", u"שמח\"ת"),
    HOLIDAY(9, 4, "chanukah", (list(range(25, 30)), 3), "", [],
            u"Chanukah", u"חנוכה", u"חנוכה"),
    HOLIDAY(9, 4, "chanukah", ([1, 2, 3], 4), "",
            [lambda x: (
                (x.short_kislev() and x._h_day == 3) or
                (x._h_day in [1, 2]))],
            u"Chanukah", u"חנוכה", u"חנוכה"),
    HOLIDAY(10, 5, "asara_btevet", (10, 4), "", [],
            u"Asara B'Tevet", u"צום עשרה בטבת", u"י' בטבת"),
    HOLIDAY(11, 7, "tu_bshvat", (15, 5), "", [],
            u"Tu B'Shvat", u"ט\"ו בשבט", u"ט\"ו בשבט"),
    HOLIDAY(12, 5, "taanit_esther", ([11, 13], [6, 14]), "",
            [move_if_not_on_dow(13, 11, 5, 3)],
            u"Ta'anit Esther", u"תענית אסתר", u"תענית אסתר"),
    HOLIDAY(13, 4, "purim", (14, [6, 14]), "", [],
            u"Purim", u"פורים", u"פורים"),
    HOLIDAY(14, 4, "shushan_purim", (15, [6, 14]), "", [],
            u"Shushan Purim", u"שושן פורים", u"שושן פורים"),
    HOLIDAY(15, 1, "pesach", (15, 7), "", "",
            u"Pesach", u"פסח", u"פסח"),
    HOLIDAY(16, 3, "hol_hamoed_pesach", (16, 7), "ISRAEL", [],
            u"Hol hamoed Pesach", u"חול המועד פסח", u"חוה\"מ פסח"),
    HOLIDAY(16, 3, "hol_hamoed_pesach", ([17, 18, 19, 20], 7), "", [],
            u"Hol hamoed Pesach", u"חול המועד פסח", u"חוה\"מ פסח"),
    HOLIDAY(17, 6, "yom haatzmaut", ([3, 4, 5, 6], 8), "", ["atsmaut()"],
            u"Yom HaAtzma'ut", u"יום העצמאות", u"יום העצמאות"),
    HOLIDAY(18, 7, "lag_bomer", (18, 8), "", [],
            u"Lag B'Omer", u"ל\"ג בעומר", u"ל\"ג בעומר"),
    HOLIDAY(19, 9, "erev_shavuot", (5, 9), "", [],
            u"Erev Shavuot", u"ערב שבועות", u"ערב שבועות"),
    HOLIDAY(20, 1, "shavuot", (6, 9), "", [],
            u"Shavuot", u"שבועות", u"שבועות"),
    HOLIDAY(21, 5, "tzom_tammuz", ([17, 18], 10), "",
            [move_if_not_on_dow(17, 18, 5, 6)],
            u"Tzom Tammuz", u"צום שבעה עשר בתמוז", u"צום תמוז"),
    HOLIDAY(22, 5, "tisha_bav", ([9, 10], 11), "",
            [move_if_not_on_dow(9, 10, 5, 6)],
            u"Tish'a B'Av", u"תשעה באב", u"ט' באב"),
    HOLIDAY(23, 7, "tu_bav", (15, 11), "", [],
            u"Tu B'Av", u"ט\"ו באב", u"ט\"ו באב"),
    HOLIDAY(24, 8, "yom_hashoah", ([26, 27, 28], 7), "",
            [move_if_not_on_dow(27, 26, 4, 3),
             move_if_not_on_dow(27, 28, 6, 0),
             year_is_after(5719)],
            u"Yom HaShoah", u"יום השואה", u"יום השואה"),
    HOLIDAY(25, 8, "yom_hazikaron", ([2, 3, 4, 5], 8), "", ["zikaron()"],
            u"Yom HaZikaron", u"יום הזכרון", u"יום הזכרון"),
    HOLIDAY(26, 6, "yom_yerushalayim", (28, 8), "", [year_is_after(5727)],
            u"Yom Yerushalayim", u"יום ירושלים", u"יום י-ם"),
    HOLIDAY(27, 1, "shmini_atzeret", (22, 1), "", [],
            u"Shmini Atzeret", u"שמיני עצרת", u"שמיני עצרת"),
    HOLIDAY(28, 1, "pesach_vii", (21, 7), "", [],
            u"Pesach VII", u"שביעי פסח", u"ז' פסח"),
    HOLIDAY(29, 1, "pesach_viii", (22, 7), "DIASPORA", [],
            u"Pesach VIII", u"אחרון של פסח", u"אחרון של פסח"),
    HOLIDAY(30, 1, "shavuot_ii", (7, 9), "DIASPORA", [],
            u"Shavuot II", u"שני של שבועות", u"ב' שבועות"),
    HOLIDAY(31, 1, "sukkot_ii", (16, 1), "DIASPORA", [],
            u"Sukkot II", u"שני של סוכות", u"ב' סוכות"),
    HOLIDAY(32, 1, "pesach_ii", (16, 7), "DIASPORA", [],
            u"Pesach II", u"שני של פסח", u"ב' פסח"),
    HOLIDAY(33, 9, "family_day", (30, 5), "ISRAEL", [],
            u"Family Day", u"יום המשפחה", u"יום המשפחה"),
    HOLIDAY(34, 9, "memorial_day_unknown", (7, [6, 14]), "ISRAEL", [],
            u"Memorial day for fallen whose place of burial is unknown",
            u"יום זכרון...", u"יום זכרון..."),
    HOLIDAY(35, 9, "rabin_memorial_day", ([11, 12], 2), "ISRAEL",
            [move_if_not_on_dow(12, 11, 4, 3), year_is_after(5757)],
            u"Yitzhak Rabin memorial day",
            u"יום הזכרון ליצחק רבין", u"יום הזכרון ליצחק רבין"),
    HOLIDAY(36, 9, "zeev_zhabotinsky_day", (29, 10), "ISRAEL",
            [year_is_after(5765)],
            u"Zeev Zhabotinsky day", u"יום ז\'בוטינסקי", u"יום ז\'בוטינסקי"),
    HOLIDAY(37, 2, "erev_yom_kippur", (9, 1), "", [],
            u"Erev Yom Kippur", u"עיוה\"כ", u"עיוה\"כ")
    )

ZMAN = namedtuple('ZMAN', 'zman, english, hebrew')
ZMANIM = (
    ZMAN("first_light", u"Alot HaShachar", u"עלות השחר"),
    ZMAN("talit", u"Talit & Tefilin's time", u"זמן טלית ותפילין"),
    ZMAN("sunrise", u"Sunrise", u"הנץ החמה"),
    ZMAN("sunset", u"Sunset", u"שקיעה"),
    ZMAN("first_stars", u"First stars", u"צאת הככבים"),
    ZMAN("plag_mincha", u"Plag Mincha", u"פלג מנחה"),
    ZMAN("big_mincha", u"Big Mincha", u"מנחה גדולה"),
    ZMAN("small_mincha", u"Small Mincha", u"מנחה קטנה"),
    ZMAN("mga_end_shma", u"Shema EOT MG\"A", u"סוף זמן ק\"ש מג\"א"),
    ZMAN("gra_end_shma", u"Shema EOT GR\"A", u"סוף זמן ק\"ש הגר\"א"),
    ZMAN("mga_end_tfila", u"Tefila EOT MG\"A", u"סוף זמן תפילה מג\"א"),
    ZMAN("gra_end_tfila", u"Tefila EOT GR\"A", u"סוף זמן תפילה גר\"א"),
    ZMAN("midnight", u"Midnight", u"חצות הלילה"),
    ZMAN("midday", u"Midday", u"חצות היום")
    )

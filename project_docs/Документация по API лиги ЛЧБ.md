```toc
```
P.S. В ЛЧБ в год проходит 2 сезона соревнований
## Получение данных игрока
### Получение ID игрока
`https://basketball.businesschampions.ru/season-{season_id}/players/{player_id}`
`player_id` - id игрока
`season_id` - id сезона (изменяется от 2 конечного предела пока нет)
>[!info] Пример (GET)
>https://basketball.businesschampions.ru/season-27/players/5687
#### Пример ответа
```html
<!DOCTYPE HTML>  
<html lang="ru" xmlns:og="http://ogp.me/ns#">  
<head>  
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>  
    <meta http-equiv="X-UA-Compatible" content="IE=9"/>  
    <meta charset="utf-8">  
    <meta name="viewport" content="width=1020"/>  
    <title>Веселенко Никита Юрьевич (Группа МТС) - «Лига Чемпионов Бизнеса» - корпоративный чемпионат по баскетболу</title>  
    <link rel="shortcut icon" href="/nox-themes/basketball/images/icon16.ico" />  
  
    <link rel="stylesheet" type="text/css" href="/nox-themes/common/css/jquery.datepick.css"  />  
    <link rel="stylesheet" type="text/css" href="/nox-themes/basketball/css/jquery.jscrollpane.css"  />  
    <link rel="stylesheet" type="text/css" href="/nox-themes/common/css/framework.css"  />  
    <link rel="stylesheet" type="text/css" href="/nox-themes/basketball/css/common.css?1727950518"  />  
    <!--[if IE]><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->  
    <script type="text/javascript" src="/nox-themes/common/js/jquery.js"></script>  
    <script type="text/javascript" src="/nox-themes/common/js/jquery.datepick.min.js"></script>  
    <script type="text/javascript" src="/nox-themes/basketball/js/jquery.mousewheel.js"></script>  
    <script type="text/javascript" src="/nox-themes/basketball/js/jquery.jscrollpane.min.js"></script>  
    <script type="text/javascript" src="/nox-themes/common/js/framework.js"></script>  
    <script type="text/javascript" src="/nox-themes/basketball/js/common.js?2"></script>  
    <script type="text/javascript" src="/nox-themes/basketball/js/scrollup.js"></script>  
    <script src="https://cdn.jsdelivr.net/npm/lazyload@2.0.0-rc.2/lazyload.js"></script>  
  
    <script type="text/javascript" src="//vk.com/js/api/openapi.js?116"></script>  
    <script type="text/javascript">  
        VK.init({  
            apiId: 4829810, onlyWidgets: true  
        });  
    </script>  
  
    <link rel="alternate" type="application/rss+xml" title="Новости" href="/news/rss" />  
    <meta name="keywords" content="баскетбол" />  
<meta name="description" content="Регулярный корпоративный турнир по баскетболу в России. В нашей бизнес-лиге по баскетболу участвует более 50 команд. Корпоративная лига - лучший способ проверить в деле боевой коллектив!" />  
    <!-- Open Graph -->  
    <meta property="og:title" content="Веселенко Никита Юрьевич (Группа МТС)" />  
    <meta property="og:type" content="website" />  
    <meta property="og:image" content="http://basketball.businesschampions.ru/nox-data/teams/gruppa_mts/players/veselenko_nikita_yurevich_2024-10-19.jpg" />  
    <meta property="og:url" content="http://basketball.businesschampions.ru/season-29/players/5687" />  
    <meta property="og:site_name" content="ЛЧБ Баскетбол" />  
  
    <script>        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){  
                    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),  
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)  
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');  
  
        ga('create', 'UA-16944600-1', 'auto');  
        ga('send', 'pageview');  
  
    </script>  
</head>  
<body class="happy-new-year">  
<div id="fb-root"></div><script src="http://connect.facebook.net/ru_RU/all.js#xfbml=1"></script>  
  
  
<div id="background">  
    <div id="header-background"></div>  
    <div id="footer-background"></div>  
    <div id="body">  
        <div id="top-banner">  
                    </div>  
        <nav class="partners top"></nav>  
  
        <header>            <a href="/" rel="index" title="На главную страницу" id="main-logo"></a>  
            <a href="/" rel="index" title="На главную страницу" id="main-logo-small"></a>  
  
            <nav id="lcb-links" class="header-menu">  
                <div class="header">Вид спорта: <span class="title">Баскетбол</span></div>  
                <div class="body">  
                    <ul>  
                                                <li>  
                            <a href="http://football.businesschampions.ru"><img src="/nox-themes/basketball/images/topicon_football.png" alt="Футбол" /> ФУТБОЛ</a>  
                        </li>  
                                                <li>                            <a href="http://basketball.businesschampions.ru"><img src="/nox-themes/basketball/images/topicon_basketball.png" alt="Баскетбол" /> БАСКЕТБОЛ</a>  
                        </li>  
                                                <li>                            <a href="http://volleyball.businesschampions.ru"><img src="/nox-themes/basketball/images/topicon_volleyball.png" alt="Волейбол" /> ВОЛЕЙБОЛ</a>  
                        </li>  
                                                <li>                            <a href="http://hockey.businesschampions.ru"><img src="/nox-themes/basketball/images/topicon_hockey.png" alt="Хоккей" /> ХОККЕЙ</a>  
                        </li>  
                                                <li>                            <a href="http://bowling.businesschampions.ru"><img src="/nox-themes/basketball/images/topicon_bowling.png" alt="Боулинг" /> БОУЛИНГ</a>  
                        </li>  
                                                <li>                            <a href="http://tabletennis.businesschampions.ru"><img src="/nox-themes/basketball/images/topicon_tabletennis.png" alt="Настольный теннис" /> НАСТОЛЬНЫЙ ТЕННИС</a>  
                        </li>  
                                            </ul>  
                </div>  
            </nav>  
  
            <nav id="seasons-links" class="header-menu"><div class="header">Сезон: <span class="title">Осень 2024</span></div>  
<div class="body">  
    <ul>  
                      <li>       <a href="/season-29/players/5687">Осень 2024</a><br />  
                      <a href="/season-28/players/5687">Весна 2024</a><br />  
        </li>      <li>       <a href="/season-27/players/5687">Осень 2023</a><br />  
                      <a href="/season-26/players/5687">Весна 2023</a><br />  
        </li>      <li>       <a href="/season-25/players/5687">Осень 2022</a><br />  
                      <a href="/season-24/players/5687">Весна 2022</a><br />  
        </li>      <li>       <a href="/season-23/players/5687">Осень 2021</a><br />  
                      <a href="/season-22/players/5687">Весна 2021</a><br />  
        </li>      <li>       <a href="/season-21/players/5687">Осень 2020</a><br />  
                      <a href="/season-20/players/5687">Весна 2020</a><br />  
        </li>      <li>       <a href="/season-18/players/5687">Осень 2019</a><br />  
                      <a href="/season-17/players/5687">Весна 2019</a><br />  
        </li>      <li>       <a href="/season-16/players/5687">Осень 2018</a><br />  
                      <a href="/season-15/players/5687">Весна 2018</a><br />  
        </li>      <li>       <a href="/season-14/players/5687">Осень 2017</a><br />  
                      <a href="/season-13/players/5687">Весна 2017</a><br />  
        </li>      <li>       <a href="/season-12/players/5687">Осень 2016</a><br />  
                      <a href="/season-11/players/5687">Весна 2016</a><br />  
        </li>      <li>       <a href="/season-10/players/5687">Осень 2015</a><br />  
                      <a href="/season-9/players/5687">Весна 2015</a><br />  
        </li>      <li>       <a href="/season-8/players/5687">Осень 2014</a><br />  
                      <a href="/season-7/players/5687">Весна 2014</a><br />  
        </li>      <li>       <a href="/season-6/players/5687">Осень 2013</a><br />  
                      <a href="/season-5/players/5687">Весна 2013</a><br />  
        </li>      <li>       <a href="/season-4/players/5687">Осень 2012</a><br />  
                      <a href="/season-3/players/5687">Весна 2012</a><br />  
        </li>      <li>       <a href="/season-2/players/5687">Осень 2011</a><br />  
                      <a href="/2010-2011/players/5687">Осень 2010</a><br />  
        </li>    </ul>  
</div>  
</nav>  
  
                        <nav id="city-links" class="header-menu">  
                <div class="header">Город: <span class="title">Москва</span></div>  
                <div class="body">  
                    <ul>  
                                                <li>  
                            <a href="http://basketball.businesschampions.ru"><img src="//basketball.businesschampions.ru/nox-themes/basketball/images/bcl-msk-icon.png" alt="Москва" /> Москва</a>  
                        </li>  
                                                <li>                            <a href="http://obninsk.basketball.businesschampions.ru"><img src="//basketball.businesschampions.ru//nox-themes/basketball/images/bcl-obn-icon.png" alt="Обнинск" /> Обнинск</a>  
                        </li>  
                                            </ul>  
                </div>  
            </nav>  
  
            <nav id="header-menu"><ul><li><a href="/about/project.html" title="О проекте" class="">О проекте</a></li><li><a href="/about/documents.html" title="Документы" class="">Документы</a></li><li><a href="/about/place.html" title="Площадки" class="">Площадки</a></li><li><a href="/about/contacts.html" title="Контакты" class="">Контакты</a></li></ul></nav>  
  
            <div id="login-block">  
                    <span class="buttons"><a href="/users/registration">Регистрация</a><a href="/users/login" onclick="$('#auth-menu').toggle(); return false;">Войти</a></span>  
<div id="auth-menu" class="hidden">  
    <form method="POST" action="/users/login">  
        Email: <input type="email" name="email" required="required" /><br />  
        Пароль: <input type="password" name="password" required="required" /><br />  
        <input type="submit" name="submit" value="Вход" class="right" />  
        <a href="/users/remind-password" class="right">Забыли пароль?</a>  
        <br class="clear" />  
    </form>  
</div>  
                <div id="search-block">  
                    <form method="get" action="https://google.ru/search">  
                        <input type="hidden" name="as_sitesearch" value="basketball.businesschampions.ru" />  
                        <input type="text" value="" placeholder="Поиск..." name="q" class="query" />  
                        <input type="submit" value="" name="submit" class="submit" />  
                    </form>  
                </div>  
            </div>  
        </header>  
  
        <nav id="main-menu">  
            <!--<a id="forum-link" href="http://forum.businesschampions.ru">Форум</a>-->  
            <a id="become-member-link" href="/about/become-a-member.html">Стать участником</a>  
            <div class="main"><ul><li><a href="/season-29" title="Главная" class="first">Главная</a></li><li><a href="/season-29/championship" title="Таблицы и расписание" class="turnir-menu">Таблицы и расписание</a></li><li><a href="/season-29/teams" title="Команды" class="teams-menu">Команды</a></li><li><a href="/season-29/statistic/teams" title="Статистика" class="stat-menu">Статистика</a></li><li><a href="/season-29/gallery" title="Медиа" class="photo-menu">Медиа</a></li><li><a href="/season-29/ratings/tour-teams" title="Сборная тура" class="">Сборная тура</a></li><li><a href="/about/contacts.html" title="Информация" class="info-menu">Информация</a></li></ul></div>  
            <div class="sub">  
                <div class="turnir-menu">  
                    <div class="table">  
                        <div class="row">  
                            <div class="col">  
                                <a href="/season-29/championship">Турнирные таблицы<br />  
                                <img src="/nox-themes/basketball/images/menu-turnir-championship.png" alt="" />  
                                </a>  
                            </div>  
  
                            <div class="col">  
                                <a href="/season-29/championship/schedule">Расписание чемпионата<br />  
                                    <img src="/nox-themes/basketball/images/menu-turnir-championship-schedule.png" alt="" />  
                                </a>  
                            </div>  
  
                            <div class="col">  
                                <a href="/season-29/cup">Схемы Кубков<br />  
                                    <img src="/nox-themes/basketball/images/menu-turnir-cup.png" alt="" />  
                                </a>  
                            </div>  
  
                            <div class="col">  
                                <a href="/season-29/cup/schedule">Расписание Кубков<br />  
                                    <img src="/nox-themes/basketball/images/menu-turnir-cup-schedule.png" alt="" />  
                                </a>  
                            </div>  
                        </div>  
                    </div>  
                </div>  
                <div class="teams-menu"><div class="table">  
    <div class="row">  
                                <div class="col">  
            <div class="division-name sport-color">Агат</div>  
            <ol>                                <li><a href="/season-29/teams/172"><img src="/nox-data/teams/moskovski-metropoliten/Moskovskii-transport_24x24pix.jpg" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/172" class="team-name">Московский метрополитен</a></li>  
                                <li><a href="/season-29/teams/165"><img src="/nox-data/teams/gazprom-energohold/gazprom-energohold_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/165" class="team-name">Газпром энергохолдинг</a></li>  
                                <li><a href="/season-29/teams/37"><img src="/nox-data/teams/giprotruboprovod/logo_for_sait_BCL_Transneft-GTP_24x24pix.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/37" class="team-name">Гипротрубопровод</a></li>  
                                <li><a href="/season-29/teams/193"><img src="/nox-data/teams/logo_for_sait_BCL_MKK_24x24pix.jpg" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/193" class="team-name">МКК</a></li>  
                                <li><a href="/season-29/teams/27"><img src="/nox-data/teams/t1consalt/t1consalt_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/27" class="team-name">Холдинг Т1</a></li>  
                                <li><a href="/season-29/teams/2"><img src="/nox-data/teams/rosenergoatom/rosenergoatom_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/2" class="team-name">Росэнергоатом</a></li>  
                            </ol>  
        </div>  
                        <div class="col">  
            <div class="division-name sport-color">Изумруд</div>  
            <ol>                                <li><a href="/season-29/teams/13"><img src="/nox-data/teams/vtb/vtb_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/13" class="team-name">Банк ВТБ</a></li>  
                                <li><a href="/season-29/teams/210"><img src="/nox-data/teams/med/logo_for_sait_BCL_Med_24x24pix (1).png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/210" class="team-name">МЭД</a></li>  
                                <li><a href="/season-29/teams/22"><img src="/nox-data/teams/lukoil/lukoil_logo_24.gif" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/22" class="team-name">ЛУКОЙЛ</a></li>  
                                <li><a href="/season-29/teams/125"><img src="/nox-data/teams/bks/BCS-MI_Logo_2022_24x24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/125" class="team-name">БКС</a></li>  
                                <li><a href="/season-29/teams/138"><img src="/nox-data/teams/nornikel/nornikel_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/138" class="team-name">Норникель</a></li>  
                                <li><a href="/season-29/teams/206"><img src="/nox-data/teams/rosatom/logo_for_sait_BCL_Rosatom_24х24pix.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/206" class="team-name">Росатом</a></li>  
                            </ol>  
        </div>  
                        <div class="col">  
            <div class="division-name sport-color">Янтарь</div>  
            <ol>                                <li><a href="/season-29/teams/116"><img src="/nox-data/teams/nspk/nspk_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/116" class="team-name">НСПК</a></li>  
                                <li><a href="/season-29/teams/213"><img src="/nox-data/badges/logo_for_sait_BCL_sibur_24x24pix.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/213" class="team-name">СИБУР</a></li>  
                                <li><a href="/season-29/teams/198"><img src="/nox-data/teams/komus/2022 komus_24x24pix.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/198" class="team-name">Комус</a></li>  
                                <li><a href="/season-29/teams/139"><img src="/nox-data/teams/sovkombank/sovkombank_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/139" class="team-name">Совкомбанк</a></li>  
                                <li><a href="/season-29/teams/104"><img src="/nox-data/teams/sberlizing/logo_for_sait_BCL_sber-lizing_24х24pix.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/104" class="team-name">СберЛизинг</a></li>  
                                <li><a href="/season-29/teams/203"><img src="/nox-data/teams/avito/logo_for_sait_BCL_Avito_24х24pix (1).png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/203" class="team-name">Авито</a></li>  
                            </ol>  
        </div>  
                        <div class="col">  
            <div class="division-name sport-color">Алмаз</div>  
            <ol>                                <li><a href="/season-29/teams/167"><img src="/nox-data/teams/liga_cyfrovoy_ekon/liga_cyfrovoy_ekon_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/167" class="team-name">Лига Цифровой Экономики</a></li>  
                                <li><a href="/season-29/teams/21"><img src="/nox-data/teams/transneft/transneft_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/21" class="team-name">Транснефть</a></li>  
                                <li><a href="/season-29/teams/171"><img src="/nox-data/teams/lanit/lanit_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/171" class="team-name">ЛАНИТ</a></li>  
                                <li><a href="/season-29/teams/31"><img src="/nox-data/teams/psb/psb_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/31" class="team-name">ПСБ</a></li>  
                                <li><a href="/season-29/teams/62"><img src="/nox-data/teams/vniia/logo-vniia-24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/62" class="team-name">ВНИИА</a></li>  
                                <li><a href="/season-29/teams/47"><img src="/nox-data/teams/tmk/tmk_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/47" class="team-name">ТМК-Москва</a></li>  
                            </ol>  
        </div>  
                </div><div class="row">        <div class="col">  
            <div class="division-name sport-color">Рубин</div>  
            <ol>                                <li><a href="/season-29/teams/200"><img src="/nox-data/teams/ozon/logo_for_sait_BCL_Ozon_24х24pix.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/200" class="team-name">OZON</a></li>  
                                <li><a href="/season-29/teams/173"><img src="/nox-data/teams/krok/krok_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/173" class="team-name">Крок</a></li>  
                                <li><a href="/season-29/teams/72"><img src="/nox-data/teams/gruppa_mts/logo_for_sait_BCL_mts_24x24pix.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/72" class="team-name">Группа МТС</a></li>  
                                <li><a href="/season-29/teams/218"><img src="/nox-data/badges/ГМ МИНИ.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/218" class="team-name">Газпром-Медиа</a></li>  
                                <li><a href="/season-29/teams/190"><img src="/nox-data/teams/yandex/yandex_logo_24x24pix 2022.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/190" class="team-name">Yandex Black</a></li>  
                                <li><a href="/season-29/teams/170"><img src="/nox-data/teams/marks/logo_for_sait_BCL_marks-group_24х24pix.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/170" class="team-name">MARKS GROUP</a></li>  
                            </ol>  
        </div>  
                        <div class="col">  
            <div class="division-name sport-color">Малахит</div>  
            <ol>                                <li><a href="/season-29/teams/196"><img src="/nox-data/teams/vk/vk_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/196" class="team-name">VK</a></li>  
                                <li><a href="/season-29/teams/75"><img src="/nox-data/teams/alfa-bank/lbc-2303-site-logos-06.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/75" class="team-name">Альфа-Банк</a></li>  
                                <li><a href="/season-29/teams/155"><img src="/nox-data/teams/skoltech/skoltech_logo_24.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/155" class="team-name">Skoltech</a></li>  
                                <li><a href="/season-29/teams/30"><img src="/nox-data/teams/raiffeisen/raiffeisen_logo_24.gif" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/30" class="team-name">РБ Банк</a></li>  
                                <li><a href="/season-29/teams/194"><img src="/nox-data/teams/yandex/yandex_logo_24x24pix 2022.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/194" class="team-name">Yandex Red</a></li>  
                                <li><a href="/season-29/teams/202"><img src="/nox-data/badges/logo_for_sait_BCL_24x24px.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/202" class="team-name">X5 Tech</a></li>  
                            </ol>  
        </div>  
                        <div class="col">  
            <div class="division-name sport-color">Сапфир</div>  
            <ol>                                <li><a href="/season-29/teams/212"><img src="/nox-data/teams/level_group/logo_for_sait_BCL_Level_24x24pix (1).png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/212" class="team-name">Level group</a></li>  
                                <li><a href="/season-29/teams/216"><img src="/nox-data/badges/logo_for_sait_BCL_s8-capital_24x24pix.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/216" class="team-name">S8 Capital</a></li>  
                                <li><a href="/season-29/teams/220"><img src="/nox-data/badges/logo_for_sait_BCL_gradostroitelnii_kompleks_24x24pix.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/220" class="team-name">Градостроительный комплекс</a></li>  
                                <li><a href="/season-29/teams/217"><img src="/nox-data/badges/Москвич мини.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/217" class="team-name">Москвич</a></li>  
                                <li><a href="/season-29/teams/215"><img src="/nox-data/badges/logo_for_sait_BCL_technolight_24x24pix.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/215" class="team-name">Technolight</a></li>  
                                <li><a href="/season-29/teams/214"><img src="/nox-data/badges/logo_for_sait_BCL_medci_24x24pix.png" class="w16 h16 m0" alt="" /></a>&nbsp;<a href="/season-29/teams/214" class="team-name">ГК Медси</a></li>  
                            </ol>  
        </div>  
                <div class="col"></div>  
    </div>  
</div></div>  
                <div class="stat-menu">  
                    <div class="table">  
                        <div class="row">  
                            <div class="col">  
                                <a href="/season-29/statistic/teams">Команды<br />  
                                    <img src="/nox-themes/basketball/images/menu-stat-teams.png" alt="" />  
                                </a>  
                            </div>  
  
                            <div class="col">  
                                <a href="/season-29/statistic/players">Игроки<br />  
                                    <img src="/nox-themes/basketball/images/menu-stat-players.png" alt="" />  
                                </a>  
                            </div>  
  
  
                            <div class="col">  
                                <a href="/season-29/referees">Судьи<br />  
                                    <img src="/nox-themes/basketball/images/menu-stat-referees.png" alt="" />  
                                </a>  
                            </div>  
  
                            <div class="col">  
  
                            </div>                        </div>  
                    </div>  
                </div>  
                <div class="photo-menu" style="width:500px;margin-left:340px;"><!-- <section id="index-banner-4"></section> -->  
<div class="table">  
    <div class="row">  
        <!--                                 <div class="col">  
                <a href="/season-29/gallery/612" class="title">10-й тур. Дивизионы &quot;Алмаз&quot;, &quot;Изумруд&quot;, &quot;Сапфир&quot;</a>                <div class="bordered-image">                    <a href="/season-29/gallery/612">                        <span><img src="/nox-data/photos/games/title/title_2024.12.15f.jpg" alt="Нет файла" /></span>                    </a>                </div>                <span class="gray left small">15.12.2024</span>                            </div>                                <div class="col">                <a href="/season-29/gallery/611" class="title">10-й тур. Дивизионы &quot;Агат&quot;, &quot;Малахит&quot;, &quot;Рубин&quot;, &quot;Янтарь&quot;</a>                <div class="bordered-image">                    <a href="/season-29/gallery/611">                        <span><img src="/nox-data/photos/games/title/title_2024.12.14f.jpg" alt="Нет файла" /></span>                    </a>                </div>                <span class="gray left small">14.12.2024</span>                            </div>                                <div class="col">                <a href="/season-29/gallery/610" class="title">9-й тур. Дивизионы &quot;Алмаз&quot;, &quot;Изумруд&quot;, &quot;Сапфир&quot;</a>                <div class="bordered-image">                    <a href="/season-29/gallery/610">                        <span><img src="/nox-data/photos/games/title/title_2024.12.08f.jpg" alt="Нет файла" /></span>                    </a>                </div>                <span class="gray left small">08.12.2024</span>                            </div>                 -->        <div class="col">  
            <a href="/season-29/gallery"><!-- Все фотоленты -->Фото<br>  
                <img src="/nox-themes/basketball/images/menu-photos.png" alt="">  
            </a>  
        </div>  
        <div class="col">  
            <a href="/season-29/video"><!-- Все фотоленты -->Видео<br>  
                <img src="/nox-themes/basketball/images/menu-photos.png" alt="">  
            </a>  
        </div>  
    </div>  
</div></div>  
  
                <div class="info-menu">  
                    <div class="table">  
                        <div class="row">  
                            <div class="col">  
                                <a href="/about/contacts.html">Контакты<br />  
                                    <img src="/nox-themes/basketball/images/menu-info-contacts.png" alt="" />  
                                </a>  
                            </div>  
  
                            <div class="col">  
                                <a href="/about/documents.html">Документы<br />  
                                    <img src="/nox-themes/basketball/images/menu-info-documents.png" alt="" />  
                                </a>  
                            </div>  
  
                            <div class="col">  
                                <a href="/about/place.html">Площадки<br />  
                                    <img src="/nox-themes/basketball/images/menu-info-areas.png" alt="" />  
                                </a>  
                            </div>  
  
                            <div class="col">  
                                <a href="/about/project.html">О проекте<br />  
                                    <img src="/nox-themes/basketball/images/menu-info-about.png" alt="" />  
                                </a>  
                            </div>  
                        </div>  
                    </div>  
                </div>  
            </div>  
        </nav>  
  
        <div class="content"><section id="index-banner-4"><div class="banner">  
       <a href="https://training.businesschampions.ru/" title="training.businesschampions.ru" target="_blank" class="pointer"><img src="/nox-data/banners/banners-2011/BCL_Sportobespechenie_Banner.jpg" alt="training.businesschampions.ru" /></a>  
    </div>  
</section>  
<style type="text/css">  
    .activity {  
  
    }    .activity > div {  
        width:340px;  
        border-bottom: 1px solid #eee;  
        margin-bottom: 13px;  
        padding-bottom: 13px;  
    }  
    .activity > div:last-child {  
        border:none;  
        margin:0;  
        padding:0;  
    }  
    .activity .text {  
        font-style:italic;  
    }  
</style>  
  
<div class="left w250">  
    <section>  
        <header>Веселенко Никита</header>  
        <div class="content half-padding">  
            <div class="bordered-image">  
                                <a href="/nox-data/teams/gruppa_mts/players/veselenko_nikita_yurevich_2024-10-19.jpg" class="zoom-link"><img src="/nox-data/teams/gruppa_mts/players/veselenko_nikita_yurevich_2024-10-19.jpg" class="w130" alt="Веселенко Никита Юрьевич" /></a>  
                            </div>  
        </div>  
    </section>  
  
    <section>        <header>Информация</header>  
        <article>        <table class="values-table w100p no-hover">  
            <tbody>  
  
            <tr><th>Команда:</th><td><a href="/season-29/teams/72" class="gray">Группа МТС</a></td></tr>  
  
            <tr><th>Амплуа:</th><td>Полевой игрок</td></tr>  
  
            <tr><th>Должность:</th><td>Сотрудник</td></tr>  
  
            <tr><th>Рост:</th><td>-</td></tr>  
  
            <tr><th>Вес:</th><td>-</td></tr>  
  
            <tr>                                                        <th>Дата рождения:</th><td>19.04.1999</td>  
                                            </tr>  
            </tbody>  
        </table>  
        </article>  
    </section>  
  
    </div>  
  
<div class="right w750">  
  
  
    <section>  
        <header>Статистика</header>  
        <article>        <table class="ruler small w100p text-center no-wrap no-hover">  
            <thead>  
            <tr>  
                <th class="w24">Игр</th>  
                <th class="w20" title="Первая пятерка">F5</th>  
                <th class="w60">1x %</th>  
                <th class="w60">2x %</th>  
                <th class="w60">3x %</th>  
                <th class="w30">Очки</th>  
                <th class="w20" title="Передачи">ПР</th>  
                <th class="w20" title="Перехваты">ПХ</th>  
                <th class="w20" title="Блокшоты">БШ</th>  
                <th class="w20" title="Свой щит">СЩ</th>  
                <th class="w20" title="Чужой щит">ЧЩ</th>  
                <th class="w20" title="Подборы">ПБ</th>  
                <th class="w20" title="Фолы">Ф</th>  
                <th class="w20" title="Фолы соперника">ФС</th>  
                <th class="w20" title="Потери">ПТ</th>  
                <th class="w40" title="Время на площадке">ВР</th>  
                <th class="w20" title="Коэффициент полезности">КП</th>  
            </tr>  
            </thead>  
            <tbody>            <tr>  
                <td>10</td>  
                <td>2</td>  
                <td>5/10 (50%)</td>  
                <td>16/34 (47%)</td>  
                <td>1/8 (13%)</td>  
                <td>40</td>  
                <td>4</td>  
                <td>8</td>  
                <td>1</td>  
                <td>16</td>  
                <td>13</td>  
                <td>29</td>  
                <td>16</td>  
                <td>7</td>  
                <td>13</td>  
                                <td>0:00</td>  
                <td>3</td>  
            </tr>  
            </tbody>  
        </table>  
        </article>  
    </section>  
  
    <section>        <header>Матчи</header>  
        <article>        <table class="ruler w100p text-center sort small">  
            <thead>  
            <tr>  
                <th class="w100">Матч</th>  
                <th class="w16" title="Первая пятерка">F5</th>  
                <th class="w70">1x %</th>  
                <th class="w70">2x %</th>  
                <th class="w70">3x %</th>  
                <th class="w30">Очки</th>  
                <th class="w20" title="Передачи">ПР</th>  
                <th class="w20" title="Перехваты">ПХ</th>  
                <th class="w20" title="Блокшоты">БШ</th>  
                <th class="w20" title="Свой щит">СЩ</th>  
                <th class="w20" title="Чужой щит">ЧЩ</th>  
                <th class="w20" title="Подборы">ПБ</th>  
                <th class="w20" title="Фолы">Ф</th>  
                <th class="w20" title="Фолы соперника">ФС</th>  
                <th class="w20" title="Потери">ПТ</th>  
                <th class="w40" title="Время на площадке">ВР</th>  
                <th class="w20" title="Коэффициент полезности">КП</th>  
            </tr>  
            </thead>  
            <tbody>                        <tr>  
                <td><a href="/season-29/teams/190">Yandex Black</a> - <a href="/season-29/teams/72">Группа МТС</a></td>  
                <td>&nbsp;</td>  
                <td>1/2 (50%)</td>  
                <td>1/2 (50%)</td>  
                <td>0/0 (0%)</td>  
                <td>3</td>  
                <td>0</td>  
                <td>1</td>  
                <td>0</td>  
                <td>5</td>  
                <td>0</td>  
                <td>5</td>  
                <td>3</td>  
                <td>1</td>  
                <td>3</td>  
                <td>18:36</td>  
                <td>2</td>  
            </tr>  
                        <tr>                <td><a href="/season-29/teams/72">Группа МТС</a> - <a href="/season-29/teams/173">Крок</a></td>  
                <td>&nbsp;</td>  
                <td>0/0 (0%)</td>  
                <td>1/4 (25%)</td>  
                <td>0/2 (0%)</td>  
                <td>2</td>  
                <td>1</td>  
                <td>0</td>  
                <td>0</td>  
                <td>4</td>  
                <td>2</td>  
                <td>6</td>  
                <td>0</td>  
                <td>0</td>  
                <td>1</td>  
                <td>22:57</td>  
                <td>3</td>  
            </tr>  
                        <tr>                <td><a href="/season-29/teams/218">Газпром-Медиа</a> - <a href="/season-29/teams/72">Группа МТС</a></td>  
                <td>&nbsp;</td>  
                <td>0/0 (0%)</td>  
                <td>0/3 (0%)</td>  
                <td>0/1 (0%)</td>  
                <td>0</td>  
                <td>0</td>  
                <td>1</td>  
                <td>0</td>  
                <td>2</td>  
                <td>1</td>  
                <td>3</td>  
                <td>2</td>  
                <td>0</td>  
                <td>0</td>  
                <td>13:44</td>  
                <td>-2</td>  
            </tr>  
                        <tr>                <td><a href="/season-29/teams/72">Группа МТС</a> - <a href="/season-29/teams/200">OZON</a></td>  
                <td>&nbsp;</td>  
                <td>1/2 (50%)</td>  
                <td>2/3 (67%)</td>  
                <td>0/0 (0%)</td>  
                <td>5</td>  
                <td>0</td>  
                <td>1</td>  
                <td>1</td>  
                <td>2</td>  
                <td>2</td>  
                <td>4</td>  
                <td>2</td>  
                <td>1</td>  
                <td>2</td>  
                <td>15:31</td>  
                <td>6</td>  
            </tr>  
                        <tr>                <td><a href="/season-29/teams/72">Группа МТС</a> - <a href="/season-29/teams/170">MARKS GROUP</a></td>  
                <td>&radic;</td>  
                <td>1/2 (50%)</td>  
                <td>1/2 (50%)</td>  
                <td>0/0 (0%)</td>  
                <td>3</td>  
                <td>1</td>  
                <td>0</td>  
                <td>0</td>  
                <td>2</td>  
                <td>2</td>  
                <td>4</td>  
                <td>1</td>  
                <td>1</td>  
                <td>1</td>  
                <td>24:24</td>  
                <td>5</td>  
            </tr>  
                        <tr>                <td><a href="/season-29/teams/72">Группа МТС</a> - <a href="/season-29/teams/218">Газпром-Медиа</a></td>  
                <td>&nbsp;</td>  
                <td>1/2 (50%)</td>  
                <td>0/1 (0%)</td>  
                <td>0/0 (0%)</td>  
                <td>1</td>  
                <td>1</td>  
                <td>0</td>  
                <td>0</td>  
                <td>1</td>  
                <td>1</td>  
                <td>2</td>  
                <td>1</td>  
                <td>1</td>  
                <td>2</td>  
                <td>8:09</td>  
                <td>0</td>  
            </tr>  
                        <tr>                <td><a href="/season-29/teams/72">Группа МТС</a> - <a href="/season-29/teams/190">Yandex Black</a></td>  
                <td>&nbsp;</td>  
                <td>0/0 (0%)</td>  
                <td>0/0 (0%)</td>  
                <td>0/0 (0%)</td>  
                <td>0</td>  
                <td>0</td>  
                <td>0</td>  
                <td>0</td>  
                <td>0</td>  
                <td>0</td>  
                <td>0</td>  
                <td>0</td>  
                <td>0</td>  
                <td>0</td>  
                <td>0:00</td>  
                <td>0</td>  
            </tr>  
                        <tr>                <td><a href="/season-29/teams/200">OZON</a> - <a href="/season-29/teams/72">Группа МТС</a></td>  
                <td>&nbsp;</td>  
                <td>0/0 (0%)</td>  
                <td>3/3 (100%)</td>  
                <td>0/0 (0%)</td>  
                <td>6</td>  
                <td>0</td>  
                <td>1</td>  
                <td>0</td>  
                <td>0</td>  
                <td>1</td>  
                <td>1</td>  
                <td>1</td>  
                <td>2</td>  
                <td>0</td>  
                <td>10:19</td>  
                <td>9</td>  
            </tr>  
                        <tr>                <td><a href="/season-29/teams/173">Крок</a> - <a href="/season-29/teams/72">Группа МТС</a></td>  
                <td>&nbsp;</td>  
                <td>1/2 (50%)</td>  
                <td>1/5 (20%)</td>  
                <td>1/2 (50%)</td>  
                <td>6</td>  
                <td>0</td>  
                <td>2</td>  
                <td>0</td>  
                <td>0</td>  
                <td>2</td>  
                <td>2</td>  
                <td>5</td>  
                <td>1</td>  
                <td>3</td>  
                <td>18:08</td>  
                <td>-3</td>  
            </tr>  
                        <tr>                <td><a href="/season-29/teams/170">MARKS GROUP</a> - <a href="/season-29/teams/72">Группа МТС</a></td>  
                <td>&radic;</td>  
                <td>0/0 (0%)</td>  
                <td>7/11 (64%)</td>  
                <td>0/3 (0%)</td>  
                <td>14</td>  
                <td>1</td>  
                <td>2</td>  
                <td>0</td>  
                <td>0</td>  
                <td>2</td>  
                <td>2</td>  
                <td>1</td>  
                <td>0</td>  
                <td>1</td>  
                <td>29:11</td>  
                <td>10</td>  
            </tr>  
                        </tbody>  
        </table>  
        </article>  
    </section>  
    </div>  
  
<br class="clear" />  
  
</div>  
        <nav class="partners bottom"><div>  
       <a href="http://https://rusporting.ru" title="Руспортинг" target="_blank" class="inline-block"><img src="/nox-data/partners/rusporting-new.png" alt="Руспортинг" /></a>  
       <a href="http://cskabasket.com/" title="ПБК ЦСКА" target="_blank" class="inline-block"><img src="/nox-data/partners/cska_partner.png" alt="ПБК ЦСКА" /></a>  
       <a href="http://terball.ru/" title="Территория мяча" target="_blank" class="inline-block"><img src="/nox-data/partners/territoria_myaca_partner.png" alt="Территория мяча" /></a>  
       <a href="http://https://kalinovrodnik.ru" title="Калинов Родник" target="_blank" class="inline-block"><img src="/nox-data/partners/logo_for_sait_BCL_KalinovRodnik_300х300pix.png" alt="Калинов Родник" /></a>  
    </div>  
</nav>  
  
        <footer>            <div class="quarter">  
                <img src="/nox-themes/basketball/images/footer-icon.png" alt="ЛЧБ" class="left"/>  
                <div class="right" >&copy; 2010-2025<br />ЛИГА ЧЕМПИОНОВ БИЗНЕСА - корпоративный чемпионат по баскетболу<br /></div>  
            </div>  
             <!-- noindex -->  
             <div class="right">  
                <!--LiveInternet counter--><script type="text/javascript"><!--  
            document.write("<a href='http://www.liveinternet.ru/click' "+  
                    "target=_blank><img src='//counter.yadro.ru/hit?t13.5;r"+  
                    escape(document.referrer)+((typeof(screen)=="undefined")?"":  
                    ";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?  
                            screen.colorDepth:screen.pixelDepth))+";u"+escape(document.URL)+  
                    ";"+Math.random()+  
                    "' alt='' title='LiveInternet: показано число просмотров за 24"+  
                    " часа, посетителей за 24 часа и за сегодня' "+  
                    "border='0' width='88' height='31'><\/a>")  
            //--></script><!--/LiveInternet-->  
  
                <!--Rating@Mail.ru counter-->                <script language="javascript"><!--  
                d=document;var a='';a+=';r='+escape(d.referrer);js=10;//--></script>  
                <script language="javascript1.1"><!--  
                a+=';j='+navigator.javaEnabled();js=11;//--></script>  
                <script language="javascript1.2"><!--  
                s=screen;a+=';s='+s.width+'*'+s.height;  
                a+=';d='+(s.colorDepth?s.colorDepth:s.pixelDepth);js=12;//--></script>  
                <script language="javascript1.3"><!--  
                js=13;//--></script><script language="javascript" type="text/javascript"><!--  
            d.write('<a href="http://top.mail.ru/jump?from=2044294" target="_top">'+  
                    '<img src="http://d1.c3.bf.a1.top.mail.ru/counter?id=2044294;t=52;js='+js+  
                    a+';rand='+Math.random()+'" alt="Рейтинг@Mail.ru" border="0" '+  
                    'height="31" width="88"><\/a>');if(11<js)d.write('<'+'!-- ');//--></script>  
                <noscript><a target="_top" href="http://top.mail.ru/jump?from=2044294">  
                    <img src="http://d1.c3.bf.a1.top.mail.ru/counter?js=na;id=2044294;t=52"  
                         height="31" width="88" border="0" alt="Рейтинг@Mail.ru"></a></noscript>  
                <script language="javascript" type="text/javascript"><!--  
                if(11<js)d.write('--'+'>');//--></script>  
                <!--// Rating@Mail.ru counter-->  
  
                <!-- begin of Top100 code -->  
                <script id="top100Counter" type="text/javascript" src="http://counter.rambler.ru/top100.jcn?2476223"></script>  
                <noscript>                    <a href="http://top100.rambler.ru/navi/2476223/">  
                        <img src="http://counter.rambler.ru/top100.cnt?2476223" alt="Rambler's Top100" border="0" />  
                    </a>  
                </noscript>  
                <!-- end of Top100 code -->  
            </div>  
            <!-- /noindex -->  
<!-- <div class="quarter" >  
                <div class="right" style="width:400px">Тел.\Факс: +7 (495) 150-07-37<br/>                    E-mail: <a href = "mailto: liga@businesschampions.ru">liga@businesschampions.ru</a><br/>                    Отдел маркетинга: partners(a)rusporting.ru</div>  
            </div> -->  
            <!--<div class="quarter">                <a href="http://rusporting.ru" target="_blank" class="left"><img src="/nox-themes/basketball/images/rusporting.png" alt="РУСПОРТИНГ" /></a>                <div class="right">Организатор турнира<br />                    Компания РУСПОРТИНГ<br />                    <a href="http://rusporting.ru" target="_blank">www.rusporting.ru</a><br /><br />                    <a href="http://rusporting.ru/services" target="_blank">Услуги</a><br />                    <a href="http://rusporting.ru/portfolio" target="_blank">Портфолио</a><br />                    <a href="http://rusporting.ru/special" target="_blank">Спецпроекты</a><br />                    <a href="http://rusporting.ru/about-us" target="_blank">О компании</a>                 </div>  
            </div>            <div class="quarter">            </div>            <div class="quarter rm"><a href="http://rusporting.ru" target="_blank" class="left"><img src="/nox-themes/basketball/images/rusporting_marketing.png" alt=""/></a>  
                <div class="right"><a href="http://marketing.rusporting.ru" target="_blank" title="">Разработка<br />и дизайн сайта</a></div>  
            </div>-->  
            <br class="clear" />  
            <hr />            <!-- <nav class="left menu"><ul><li><a href="/about/project.html" title="О проекте" class="">О проекте</a></li><li><a href="/about/documents.html" title="Документы" class="">Документы</a></li><li><a href="/about/place.html" title="Площадки" class="">Площадки</a></li><li><a href="/about/contacts.html" title="Контакты" class="bold">Контакты</a></li></ul><ul><li><a href="/season-29/championship" title="Турнирные таблицы" class="bold">Турнирные таблицы</a></li><li><a href="/season-29/championship/schedule" title="Расписание чемпионта" class="">Расписание чемпионта</a></li><li><a href="/season-29/cup" title="Схемы Кубков" class="">Схемы Кубков</a></li><li><a href="/season-29/cup/schedule" title="Расписание Кубков" class="">Расписание Кубков</a></li><li><a href="/season-29/teams" title="Команды" class="bold">Команды</a></li></ul><ul><li><a href="/season-29/statistic/teams" title="Статистика" class="bold">Статистика</a></li><li><a href="/season-29/statistic/players" title="Игроки" class="">Игроки</a></li><li><a href="/season-29/statistic/podbory" title="Подборы" class="">Подборы</a></li><li><a href="/season-29/statistic/peredachi" title="Передачи" class="">Передачи</a></li><li><a href="/season-29/statistic/perehvaty" title="Перехваты" class="">Перехваты</a></li><li><a href="/season-29/statistic/referees" title="Судьи" class="">Судьи</a></li><li><a href="/season-29/gallery" title="Фотолента" class="bold">Фотолента</a></li></ul></nav> -->  
  
            <br class="clear" />  
        </footer>  
    </div>  
</div>  
<script type="text/javascript" src="/nox-themes/basketball/js/snowfall.min.jquery.js"></script>  
<script type="text/javascript">  
    $(document).ready(function(){  
        $('#body > header').snowfall({  
            round: true, maxSize: 3, flakeCount : 50, minSpeed: 1, maxSpeed:2});  
    });  
</script>  
<!-- если просто вставить Яндекс-метрику в html-страницу, шаблонизатор выдаёт ошибку из-за попытки парсить insertBefore() -->  
<!-- Yandex.Metrika counter -->  
          <script type="text/javascript">  
              (function (d, w, c) {  
                  (w[c] = w[c] || []).push(function() {  
                      try {  
                          w.yaCounter43673679 = new Ya.Metrika({  
                              id:43673679,  
                              clickmap:true,  
                              trackLinks:true,  
                              accurateTrackBounce:true,  
                              webvisor:true  
                          });  
                      } catch(e) { }  
                  });  
  
                  var n = d.getElementsByTagName("script")[0],  
                      s = d.createElement("script"),  
                      f = function () { n.parentNode.insertBefore(s, n); };  
                  s.type = "text/javascript";  
                  s.async = true;  
                  s.src = "https://mc.yandex.ru/metrika/watch.js";  
  
                  if (w.opera == "[object Opera]") {  
                      d.addEventListener("DOMContentLoaded", f, false);  
                  } else { f(); }  
              })(document, window, "yandex_metrika_callbacks");  
          </script>  
          <noscript><div><img src="https://mc.yandex.ru/watch/43673679" style="position:absolute; left:-9999px;" alt="" /></div></noscript>  
          <!-- /Yandex.Metrika counter --></body>  
</html>  
  
  
Напиши код на python, который распарсит следующую таблицу из секции на словар:  
<section>  
        <header>Статистика</header>  
        <article>        <table class="ruler small w100p text-center no-wrap no-hover">  
            <thead>  
            <tr>  
                <th class="w24">Игр</th>  
                <th class="w60">1x %</th>  
                <th class="w20" title="Передачи">ПР</th>  
                <th class="w40" title="Время на площадке">ВР</th>  
                <th class="w20" title="Коэффициент полезности">КП</th>  
            </tr>  
            </thead>  
            <tbody>            <tr>  
                <td>10</td>  
                <td>5/10 (50%)</td>  
                <td>40</td>  
                <td>0:00</td>  
                <td>3</td>  
            </tr>  
            </tbody>  
        </table>  
        </article>  
    </section>
```
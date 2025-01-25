```toc
```
## Получение данных игрока
### Получение ID игрока
`https://ablforpeople.com/player/{local_player_id}?seasonId={season_id}`
`local_player_id` - локальное id игрока
`season_id` - id сезона
>[!info] Пример (GET)
>https://ablforpeople.com/player/76755?seasonId=48
### Получения персональной информации об игроке
`https://mtgame.ru/api/v1/league_player/{local_player_id}/`
`local_player_id` - локальное id игрока
>[!info] Пример (GET)
>https://mtgame.ru/api/v1/league_player/76755/

Пример ответа:
```json
{
  "additional_data":null,
  "birth_date":"1999-04-19",
  "field_values":[
    {
      "file":null,
      "id":53492,
      "league_player_field":{
        "id":31,
        "is_multiple":false,
        "league_id":2,
        "name":"Мед. справка",
        "show_in_application_file":false,
        "sort":null,
        "type":"select",
        "variants":[
          {
            "name":"сдал",
            "uuid":"7afe8081-4530-4748-b5ca-efe52ea08a1b"
          },
          {
            "name":"не сдал",
            "uuid":"2ee12565-bc4e-478e-8ac0-c38b102bc800"
          }
        ]
      },
      "league_player_field_id":31,
      "league_player_id":76755,
      "value":"7afe8081-4530-4748-b5ca-efe52ea08a1b",
      "value_text":"сдал"
    }
  ],
  "first_name":"Никита",
  "gender":"male",
  "has_changes":false,
  "id":76755,
  "last_name":"Базаров",
  "league_id":2,
  "license_number":null,
  "middle_name":null,
  "photo":{
    "created_at":"2023-05-12T20:28:31.503243",
    "engine":"yandex_s3",
    "id":4211442,
    "mime_type":"image/jpeg",
    "name":"veselenko_nikita_yurevich_2023-04-03.jpg",
    "original_name":"veselenko_nikita_yurevich_2023-04-03.jpg",
    "path":"https://fs.mtgame.ru/veselenko_nikita_yurevich_2023-04-03.jpg",
    "size":36342
  },
  "qualification":null,
  "rating":null,
  "user":{
    "basketball_profile":{
      "position":"small_forward",
      "work_hand":"right"
    },
    "birth_date":"1999-01-19",
    "city":{
      "country":"RU",
      "id":1,
      "name":"Москва"
    },
    "created_by_league_id":null,
    "first_name":"Никита",
    "football_profile":null,
    "gender":"male",
    "handball_profile":null,
    "hockey_profile":null,
    "id":60868,
    "is_active":true,
    "last_name":"Базаров",
    "middle_name":null,
    "photo":{
      "created_at":"2024-06-13T11:15:40.288187",
      "engine":"yandex_s3",
      "id":6536315,
      "mime_type":"image/jpeg",
      "name":"1000024605.jpg",
      "original_name":"1000024605.jpg",
      "path":"https://fs.mtgame.ru/1000024605.jpg",
      "size":33869
    },
    "profile":{
      "height":186,
      "weight":86
    },
    "rsv_account_id":null,
    "rugby_profile":null,
    "teams":[ ],
    "telegram_chat_id":null,
    "unique_code":"QXKU",
    "volleyball_profile":null,
    "waterpolo_profile":null,
    "wrestball_profile":null
  },
  "user_id":60868
}
```
### Получение статистики игрока по играм
**НЕ НАЙДЕНО КОРОТКОГО ПУТИ**
1. По полученной ссылке игрока вытащить `user_id` (см. выше)
2. Получить список сыгранных игр `https://mtgame.ru/api/v1/tournament_season/{season_id}/games/?page=1&size=999&league_player_id={local_player_id}`
`season_id` - id сезона из url присланного игроком
`local_player_id` - id  игрока из url присланного игроком
Получить `id` игры + дату и время проведения (см. ниже)
>[!info] Пример (GET)
>https://mtgame.ru/api/v1/tournament_season/64/games/?page=1&size=999&league_player_id=50107

Пример ответа:
```json
[
  {
    "additional_data":{ },
    "competitor_team":{
      "city":{
        "country":"RU",
        "id":1,
        "name":"Москва"
      },
      "id":3140,
      "logo":{
        "created_at":"2024-11-28T03:20:35.818168",
        "engine":"yandex_s3",
        "id":7359911,
        "mime_type":"image/png",
        "name":"1000032796.png",
        "original_name":"1000032796.png",
        "path":"https://fs.mtgame.ru/1000032796.png",
        "size":71101
      },
      "name":"99 Problems",
      "sport":{
        "id":3,
        "is_hidden":false,
        "name":"Баскетбол",
        "name_en":null,
        "parent_id":1
      },
      "unique_code":"42FR"
    },
    "competitor_team_id":3140,
    "competitor_team_name":null,
    "competitor_team_score":73,
    "competitor_tournament_team":{
      "additional_data":{
        "color":null,
        "nickname":null
      },
      "id":13474,
      "logo":{
        "created_at":"2024-11-28T03:20:35.818168",
        "engine":"yandex_s3",
        "id":7359911,
        "mime_type":"image/png",
        "name":"1000032796.png",
        "original_name":"1000032796.png",
        "path":"https://fs.mtgame.ru/1000032796.png",
        "size":71101
      },
      "name":"99 Problems"
    },
    "competitor_tournament_team_id":13474,
    "datetime":"2024-12-21T17:40:00.000000Z",
    "division_id":null,
    "game_config":{
      "timer_type":1,
      "period_time":12,
      "timeout_time":60,
      "overtime_time":4,
      "overtime_type":null,
      "periods_count":4,
      "timeout_count":2,
      "game_time_type":2,
      "overtime_score":null,
      "statistic_type":2,
      "game_up_to_score":null,
      "max_game_players":5,
      "shot_clock_enabled":false,
      "overtime_timeout_count":1
    },
    "id":89065,
    "location":"Россия, Москва, Авиамоторная улица, 55к8",
    "media_count":null,
    "media_live_count":null,
    "mhl_carousel":null,
    "playoff_number":null,
    "playoff_round":null,
    "playoff_stage":"",
    "result_type":"competitor_team_won",
    "score_by_period":{
      "1":[
        9,
        17
      ],
      "2":[
        13,
        11
      ],
      "3":[
        10,
        19
      ],
      "4":[
        16,
        26
      ]
    },
    "status":"closed",
    "team":{
      "city":{
        "country":"RU",
        "id":1,
        "name":"Москва"
      },
      "id":8402,
      "logo":{
        "created_at":"2024-08-21T09:13:00.833823",
        "engine":"yandex_s3",
        "id":6646496,
        "mime_type":"image/png",
        "name":"LOGOTIP.png",
        "original_name":"ЛОГОТИП.png",
        "path":"https://fs.mtgame.ru/LOGOTIP.png",
        "size":182546
      },
      "name":"Russian Wolves Жулебино",
      "sport":{
        "id":3,
        "is_hidden":false,
        "name":"Баскетбол",
        "name_en":null,
        "parent_id":1
      },
      "unique_code":"BPW1"
    },
    "team_id":8402,
    "team_score":48,
    "tournament":{
      "alias":"grow",
      "id":1578,
      "league_id":2,
      "logo":{
        "created_at":"2024-09-05T13:33:06.044127",
        "engine":"yandex_s3",
        "id":6690353,
        "mime_type":"image/png",
        "name":"grow_line_no_bg.png",
        "original_name":"grow_line_no_bg.png",
        "path":"https://fs.mtgame.ru/grow_line_no_bg.png",
        "size":16508
      },
      "name":"GROW",
      "preview_image":{
        "created_at":"2024-08-21T14:37:40.541994",
        "engine":"yandex_s3",
        "id":6647245,
        "mime_type":"image/png",
        "name":"oblojkadivizionov_dCk75.png",
        "original_name":"обложка дивизионов.png",
        "path":"https://fs.mtgame.ru/oblojkadivizionov_dCk75.png",
        "size":104258
      }
    },
    "tournament_court":{
      "address":"Россия, Москва, Авиамоторная улица, 55к8",
      "id":146,
      "league_id":2,
      "name":"Авиамоторная"
    },
    "tournament_group":{
      "id":2665,
      "name":"GROW",
      "sort":1,
      "tournament_stage_id":null,
      "tournament_round_id":null,
      "division_id":null
    },
    "tournament_id":1578,
    "tournament_playoff":null,
    "tournament_playoff_id":null,
    "tournament_round_id":null,
    "tournament_stage":null,
    "tournament_stage_id":null,
    "tournament_team":{
      "additional_data":{
        "color":null,
        "nickname":null
      },
      "id":13456,
      "logo":{
        "created_at":"2024-08-21T09:13:00.833823",
        "engine":"yandex_s3",
        "id":6646496,
        "mime_type":"image/png",
        "name":"LOGOTIP.png",
        "original_name":"ЛОГОТИП.png",
        "path":"https://fs.mtgame.ru/LOGOTIP.png",
        "size":182546
      },
      "name":"Russian Wolves"
    },
    "tournament_team_id":13456,
    "tournament_tour":14
  }
  ]
```
3. По полученному `id` игры осуществляем запрос `https://mtgame.ru/api/v1/tournament_game/{game_id}/users/`
`game_id` - id игры, полученный из п. 2
>[!info] Пример (GET)
>https://mtgame.ru/api/v1/tournament_game/89065/users/

Пример ответа:
```json
[
{
    "id":1226106,
    "game_id":89065,
    "team_user":{
      "id":133140,
      "user":{
        "id":31275,
        "first_name":"Николай",
        "last_name":"Сахаров",
        "middle_name":null,
        "photo":{
          "id":4825820,
          "name":"yRh_O7r-wxw.jpg",
          "original_name":"yRh_O7r-wxw.jpg",
          "path":"https://fs.mtgame.ru/yRh_O7r-wxw.jpg",
          "mime_type":"image/jpeg",
          "size":36357,
          "engine":"yandex_s3",
          "created_at":"2023-10-18T20:22:15.270865Z"
        },
        "gender":"male",
        "birth_date":"1996-03-05",
        "city":{
          "id":1,
          "name":"Москва",
          "name_en":"Moscow",
          "country":"RU"
        },
        "profile":{
          "user_id":31275,
          "height":190,
          "weight":110
        },
        "basketball_profile":null,
        "volleyball_profile":null,
        "hockey_profile":null,
        "football_profile":null,
        "handball_profile":null,
        "rugby_profile":null,
        "waterpolo_profile":null,
        "wrestball_profile":null,
        "is_active":true,
        "unique_code":"2TQB",
        "rsv_account_id":null,
        "teams":[ ]
      },
      "role":"member",
      "permission_role":"member",
      "number":"98",
      "team_id":8402,
      "created_at":"2024-08-28T20:21:30.369099Z",
      "updated_at":"2024-10-05T14:13:14.785481Z"
    },
    "tournament_team_user":{
      "id":273541,
      "tournament_team_id":13456,
      "team_user_id":133140,
      "disqualified":false,
      "league_player":{
        "id":50107,
        "user_id":31275,
        "league_id":2,
        "rating":null,
        "first_name":"Николай",
        "last_name":"Сахаров",
        "middle_name":null,
        "photo":{
          "id":4825820,
          "name":"yRh_O7r-wxw.jpg",
          "original_name":"yRh_O7r-wxw.jpg",
          "path":"https://fs.mtgame.ru/yRh_O7r-wxw.jpg",
          "mime_type":"image/jpeg",
          "size":36357,
          "engine":"yandex_s3",
          "created_at":"2023-10-18T20:22:15.270865Z"
        },
        "gender":"male",
        "birth_date":"1996-03-05",
        "has_changes":false,
        "license_number":null,
        "additional_data":null,
        "qualification":null,
        "field_values":[
          {
            "id":53544,
            "league_player_id":50107,
            "league_player_field_id":31,
            "league_player_field":{
              "id":31,
              "league_id":2,
              "name":"Мед. справка",
              "type":"select",
              "is_multiple":false,
              "variants":[
                {
                  "uuid":"7afe8081-4530-4748-b5ca-efe52ea08a1b",
                  "name":"сдал"
                },
                {
                  "uuid":"2ee12565-bc4e-478e-8ac0-c38b102bc800",
                  "name":"не сдал"
                }
              ],
              "show_in_application_file":false,
              "sort":null
            },
            "file":null,
            "value":"7afe8081-4530-4748-b5ca-efe52ea08a1b",
            "value_text":"сдал"
          }
        ]
      },
      "last_name":null,
      "first_name":null,
      "middle_name":null,
      "photo":null,
      "active":true
    },
    "is_mvp":false,
    "updated_at":"2024-12-21T18:41:05.926710Z",
    "number":98
  },
]
```
4. Из п. 4 в ответе найти игрока, у которого `user_id == team_user.user.id (через точку вложенность)` и взять `id` у самой верхней структуры - это `game_user_id`. Сделать запрос `https://mtgame.ru/api/v1/tournament_basketball_game/{game_id}/user_statistic/`
`game_id` - id игры, полученный из п. 2
>[!info] Пример (GET)
>https://mtgame.ru/api/v1/tournament_basketball_game/89065/user_statistic/

**И наконец-то мы сможем получить статистику 1 игры**
Пример ответа:
```json
[
{
    "game_user_id":1226106,
    "points":0,
    "two_points_made":0,
    "three_points_made":0,
    "free_throws_made":0,
    "two_point_attempts":3,
    "three_point_attempts":0,
    "one_point_attempts":0,
    "one_points_made":0,
    "free_throw_attempts":2,
    "two_point_percent":0.0,
    "three_point_percent":0.0,
    "free_throw_percent":0.0,
    "one_point_percent":0.0,
    "four_point_percent":0.0,
    "assists":1,
    "blocks":0,
    "rebounds":7,
    "offensive_rebounds":3,
    "defensive_rebounds":4,
    "steals":1,
    "turnovers":0,
    "personal_fouls":3,
    "technical_fouls":0,
    "unsportsmanlike_fouls":0,
    "game_time":2365,
    "plus_minus":-20,
    "disqualification_fouls":0,
    "drawn_fouls":2,
    "player_efficiency":3,
    "four_point_attempts":0,
    "four_points_made":0,
    "dunk_attempts":0,
    "dunks_made":0,
    "shootouts_won":0,
    "shootouts_lost":0,
    "shootout_won_percent":0.0,
    "shootouts_total":0,
    "moneyball_free_throw_attempts":0,
    "moneyball_free_throws_made":0
  }
]
```
### Получение статистики по сезонам (по 1 сезону)
Отправка POST-запроса
`https://mtgame.ru/api/v1/basketball_statistic/`
`body={"league_player_id": {local_player_id}, "group_by": {group_by_type}, "per_game": {per_game}}`
`local_player_id` - локальное id игрока
`per_game` - 1 - среднее за игру, 0 - суммарно
`group_by_type` - тип группировки: 1) `month`; 2) `win_loses`; 3) `team`; 4) `user`; 5) `league_player`.
>[!info] Пример (POST)
>https://mtgame.ru/api/v1/basketball_statistic/
>`body = {"league_player_id": 76755, "tournament_season_id": 48, "group_by": "user", "per_game": "1"}`

Пример ответа:
```json
[
  {
    "user_id":60868,
    "two_point_percent":42.2,
    "three_point_percent":18.3,
    "free_throw_percent":39.0,
    "one_point_percent":0.0,
    "true_shooting_attempts":7.3,
    "true_shooting_percent":38.4,
    "four_point_percent":0.0,
    "shootout_won_percent":0.0,
    "shootouts_total":0.0,
    "total_fouls":2.0,
    "moneyball_free_throw_percent":0.0,
    "unsportsmanlike_fouls":0.0,
    "drawn_fouls":1.1,
    "rebounds":4.9,
    "three_point_attempts":2.0,
    "free_throws_made":0.5,
    "dunk_attempts":0.0,
    "free_throw_attempts":1.3,
    "points":5.6,
    "offensive_rebounds":1.4,
    "two_points_made":2.0,
    "defensive_rebounds":3.5,
    "steals":1.2,
    "four_point_attempts":0.0,
    "personal_fouls":2.0,
    "dunks_made":0.0,
    "assists":1.3,
    "three_points_made":0.3,
    "player_efficiency":3.5,
    "blocks":0.0,
    "two_point_attempts":4.7,
    "one_points_made":0.0,
    "technical_fouls":0.0,
    "moneyball_free_throw_attempts":0.0,
    "turnovers":3.5,
    "disqualification_fouls":0.0,
    "one_point_attempts":0.0,
    "shootouts_lost":0.0,
    "moneyball_free_throws_made":0.0,
    "game_time":1728.8,
    "shootouts_won":0.0,
    "four_points_made":0.0,
    "games_count":31,
    "draw_games_count":0,
    "won_games_count":7,
    "lose_games_count":24,
    "team_score_sum":1389,
    "team_missed_sum":1939,
    "user":{
      "basketball_profile":{
        "position":"small_forward",
        "work_hand":"right"
      },
      "first_name":"Никита",
      "id":60868,
      "last_name":"Базаров",
      "middle_name":null,
      "photo":{
        "created_at":"2024-06-13T11:15:40.288187",
        "engine":"yandex_s3",
        "id":6536315,
        "mime_type":"image/jpeg",
        "name":"1000024605.jpg",
        "original_name":"1000024605.jpg",
        "path":"https://fs.mtgame.ru/1000024605.jpg",
        "size":33869
      }
    }
  }
]
```
## Получение данных команды (в которой играет игрок)
### Получение id команды из ссылки
`https://ablforpeople.com/team/{team_id}?seasonId={season_id}&tournamentId={tournament_id}`
`team_id` - id команды
`season_id` - 
`tournament_id` - id дивизиона/турнира (надо запрашивать ссылки при смене турниров)
>[!info] Пример (GET)
>https://ablforpeople.com/team/8402?seasonId=64&tournamentId=1578

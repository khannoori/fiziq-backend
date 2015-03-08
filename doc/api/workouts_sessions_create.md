/workouts/sessions/create
-------------------------
**Method**: `POST`

# Request

|     Parameter     |     Type     |   Required   |
|-------------------|--------------|:------------:|
| user_key          | `string`     | Yes          |
| started_at        | `string`     | Yes          |
| ended_at          | `string`     | Yes          |

The `user_key` parameter is the datastore key of the user, see [user registration](users_register.md) for more 
information.

The `started_at` and `ended_at` parameters must be specified as date time using the ISO 8601
standard, e.g. `2011-07-14T19:43:37+0100`.

## Example

```
POST https://fiziq-backend.appspot.com/_ah/api/default/v1/workouts/sessions/create

{
    "user_key": "ahFkZXZ-Zml6aXEtYmFja2VuZHIfCxIEVXNlciIEcm9vdAwLEgRVc2VyGICAgICAwL8JDA",
    "started_at": "2015-03-08T18:00:00+0100",
    "ended_at": "2015-03-08T18:45:00+0100"
}
```


# Response
On success this API endpoint returns the following response as JSON:

|     Parameter     |     Type     |   Required   |
|-------------------|--------------|:------------:|
| session_key       | `string`     | Yes          |

The `session_key` parameter is the datastore key of the workout session that was created.

## Example

```JSON
{
    "session_key": "bhFPR-Zml6aXEtYmFja2VuZHIfCxIEVXNlciIEcm9vdAwLEgRVc2VyGICAgICAwL8JDA"
}
```

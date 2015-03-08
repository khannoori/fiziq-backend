/workouts/set/create
--------------------
**Mehtod**: `POST`

# Request

|     Parameter     |     Type     |   Required   |
|-------------------|--------------|:------------:|
| session_key       | `string`     | Yes          |
| workout_key       | `string`     | Yes          |
| repetitions       | `integer`    | Yes          |
| weight            | `float`      | Yes          |
| elapsed_time      | `integer`    | Yes          |

The `session_key` and `workout_key` parameters are the datastore keys of
a specific workout session and a workout, respectively.

The `elapsed_time` prarameter must be specified as a number of seconds.

## Example

```
POST https://fiziq-backend.appspot.com/_ah/api/default/v1/workouts/set/create

{
    "session_key": "bhFPR-Zml6aXEtYmFja2VuZHIfCxIEVXNlciIEcm9vdAwLEgRVc2VyGICAgICAwL8JDA",
    "workout_key": "ahFkZXZ-Zml6aXEtYmFja2VuZHIlCxIHV29ya291dCIEcm9vdAwLEgdXb3Jrb3V0GICAgICAwO8IDA",
    "repetitions": 10,
    "weight": 60.0,
    "elapsed_time": 100
}
```


# Response
On success this API endpoint returns the following response as JSON:

|     Parameter     |     Type     |   Required   |
|-------------------|--------------|:------------:|
| set_key           | `string`     | Yes          |

The `set_key` parameter is the datastore key of the workout sest that was created.

## Example

```JSON
{
    "set_key": "mnwroKT-Zml6aXEtYmFja2VuZHIfCxIEVXNlciIEcm9vdAwLEgRVc2VyGICAgICAwL8JDA"
}
```

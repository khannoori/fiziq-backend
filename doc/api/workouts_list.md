/workouts/list
--------------
**Method**: `GET`

# Request
This endpoint accepts no request parameters.


## Example

```
GET https://fiziq-backend.appspot.com/_ah/api/default/v1/workouts/list
```


# Response
On success, this endpoint returns the following response as JSON:

|     Parameter     |     Type     |   Required   |
|-------------------|--------------|:------------:|
| items             | `Workout[]`  | No           |

The `Workout` type is documented [below](#workout).

On failure, this endpoint returns an empty JSON object, i.e. `{}`.

## Example

```JSON
{
    "items": [
        {
            "workout_key": "ahFkZXZ-Zml6aXEtYmFja2VuZHIlCxIHV29ya291dCIEcm9vdAwLEgdXb3Jrb3V0GICAgICAwO8IDA",
            "name": "Barbell Bench Press",
            "muscle_group": {
                "id": 1,
                "name": "Chest"
            },
            "description": "The classic bench press exercise known by every one.",
            "images": [
                "https://fiziq-backend.appspot.com/images/rqoS6-GwdgWHa_zGHH6K4g==",
                "https://fiziq-backend.appspot.com/images/wUck4rCG4gKkO95fX3lRCQ=="
            ]
        },
        ...
    ]
}
```

### Workout
This type represents a workout (an exercise) returned as a JSON object with the following properties:

|     Parameter     |     Type      |   Required   |
|-------------------|---------------|:------------:|
| workout_key       | `string`      | Yes          |
| name              | `string`      | Yes          |
| muscle_group      | `MuscleGroup` | Yes          |
| description       | `string`      | No           |
| images            | `string[]`    | No           |

The `MuscleGroup` type is documented [below](#musclegroup).

The `images` parameter is a list of URLs that can be used to access the images describing the workout.


### MuscleGroup
This type represents a muscle group returned as a JSON object with the following properties:

|     Parameter     |     Type      |   Required   |
|-------------------|---------------|:------------:|
| id                | `integer`     | Yes          |
| name              | `string`      | Yes          |

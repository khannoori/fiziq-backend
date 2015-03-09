/muscle/groups/list
-------------------
**Method**: `GET`

# Request
This endpoint accepts no request parameters.


## Example

```
GET https://fiziq-backend.appspot.com/_ah/api/default/v1/muscle/groups/list
```


# Response
On success, this endpoint returns the following response as JSON:

|     Parameter     |        Type      |   Required   |
|-------------------|------------------|:------------:|
| items             | `MuscleGroup[]`  | No           |

The `MuscleGroup` type is documented [below](#musclegroup).

On failure, this endpoint returns an empty JSON object, i.e. `{}`.

## Example

```JSON
{
    "items": [
        {
            "id": 1,
            "name": "Chest"
        },
        ...
    ]
}
```

### MuscleGroup
This type represents a muscle group returned as a JSON object with the following properties:

|     Parameter     |     Type      |   Required   |
|-------------------|---------------|:------------:|
| id                | `integer`     | Yes          |
| name              | `string`      | Yes          |

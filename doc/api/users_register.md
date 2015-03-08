/users/register
---------------
**Mehtod**: `POST`

# Request

|     Parameter     |     Type     |   Required   |
|-------------------|--------------|:------------:|
| name              | `string`     | Yes          |
| email             | `string`     | Yes          |

## Example

```
POST https://fiziq-backend.appspot.com/_ah/api/default/v1/users/register

{
    "name": "Ismail Faizi",
    "email": "kanafghan@gmail.com"
}
```


# Response
On success this API endpoint returns the following response as JSON:

|     Parameter     |     Type     |   Required   |
|-------------------|--------------|:------------:|
| user_key          | `string`     | Yes          |

The `user_key` parameter is the datastore key of the user which is required by
every API endpoint that updates resources of a specific user. Thus, it should 
be stored by the clients for subsequent requests.

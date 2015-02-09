# Datamodel
The following diagram presents the datamodel behind the Fiziq app.

![Fiziq Datamodel](fiziq_datamodel.png)

In the following, the concepts presented in the above diagram are ellaborated.

### User
This concept represents any end-user of the app and does not need to be
ellaborated. A user has a [TrainingJournal](#TrainingJournal).

User has the following properties:
| Property Name        | Type              | Remarks                         |
|----------------------|:-----------------:|---------------------------------|
| name                 | `string`          |                                 |
| email                | `string`          |                                 |
| createdAt            | `datetime`        |                                 |
| updatedAt            | `datetime`        |                                 |
| trainingJournal      | `TrainingJournal` |                                 |


### TrainingJournal
This concept represents the log over all trainings sessions performed by a user.

TrainingJournal has the following properties:
| Property Name        | Type          | Remarks                             |
|----------------------|:-------------:|-------------------------------------|
| createdAt            | `datetime`    |                                     |
| user                 | `User`        |                                     |


### WorkoutSession
This concept represents a period of time where a number of physiqual exercises
are performed by a person.

WorkoutSession has the following properties:
| Property Name        | Type             | Remarks                          |
|----------------------|:----------------:|----------------------------------|
| name                 | `string`         |                                  |
| workoutSession       | `WorkoutSession` |                                  |
| datetime             | `datetime`       |                                  |

### WorkoutSet
This concept consists of a workout/exercise, the number of time it is repeated
and the weights/intensity used to perform it each time.

WorkSet has the following properties
| Property Name        | Type             | Remarks                          |
|----------------------|:----------------:|----------------------------------|
| name                 | `string`         |                                  |
| Repetition           | `int`            |                                  |
| Weight               | `float`          |                                  |
| workoutSession       | `WorkoutSession` |                                  |

### Workout
This concept represents a physiqual exercise that targets one or multiple
muscle groups and can be performed by a person.

Workout has the following properties
| Property Name        | Type          | Remarks                             |
|----------------------|:-------------:|-------------------------------------|
| name                 | `string`      |                                     |
| muscleGroup          | `MuscleGroup` |                                     |

### MuscleGroup
There are 7 major muscle groups that all workouts are divided into:
1. Chest
2. Shoulders
3. Back
4. Biceps
5. Triceps
6. Legs
7. Abs

MuscleGroup has the following properties
| Property Name        | Type          | Remarks                             |
|----------------------|:-------------:|-------------------------------------|
| name                 | `string`      |                                     |

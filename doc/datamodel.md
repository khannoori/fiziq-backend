# Datamodel
The following diagram presents the datamodel behind the Fiziq app.

![Fiziq Datamodel](fiziq_datamodel.png)

In the following, the concepts presented in the above diagram are ellaborated.

### User
This concept represents any end-user of the app and does not need to be
ellaborated. A user has a [TrainingJournal](#TrainingJournal).


| Property Name | Type         | Remarks                                    |
|----------------------|:-------------:|-------------------------------------------|
| name                | `string`      |                                                    |
| email                | `string`      |                                                    |
| createdAt         | `datetime` |                                                    |
| updatedAt        | `datetime` |                                                    |
| TrainingJournal        | `TrainingJournal` |                                                    |

### TrainingJournal
This concept represents the log over all trainings sessions performed by a user.

| Property Name | Type         | Remarks                                    |
|----------------------|:-------------:|-------------------------------------------|
| name                | `string`      |                                                    |
| User         | `User` |                                                    |


### WorkoutSession
This concept represents a period of time where a number of physiqual exercises
are performed by a person.

| Property Name | Type         | Remarks                                    |
|----------------------|:-------------:|-------------------------------------------|
| name                | `string`      |                                                    |
| WorkoutSession         | `WorkoutSession` |                                                    |
| datetime         | `datetime` |                                                    |

### WorkoutSet
This concept consists of a workout/exercise, the number of time it is repeated
and the weights/intensity used to perform it each time.

| Property Name | Type         | Remarks                                    |
|----------------------|:-------------:|-------------------------------------------|
| name                | `string`      |                                                    |
| Repetition                | `int`      |                                                    |
| Weight         | `float` |                                                    |
| WorkoutSession         | `WorkoutSession` |                                                    |
### Workout
This concept represents a physiqual exercise that targets one or multiple
muscle groups and can be performed by a person.

| Property Name | Type         | Remarks                                    |
|----------------------|:-------------:|-------------------------------------------|
| name                | `string`      |                                                    |
| MuscleGroup         | `MuscleGroup` |                                                    |

### MuscleGroup
There are 7 major muscle groups that all workouts are divided into:

| Property Name | Type         | Remarks                                    |
|----------------------|:-------------:|-------------------------------------------|
| name                | `string`      |                                                    |

1. Chest
2. Shoulders
3. Back
4. Biceps
5. Triceps
6. Legs
7. Abs

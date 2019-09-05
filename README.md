# User and Notes

This is a small application which implements a Micro-services architecture using Docker and Docker Compose, and multiple containers for each service and database.

**Containers**

- web: Serves the static website that consumes the Api's, and the user to interact with the data
- users: Api for users management made with flask
- users_db: Mongo database service for users
- user_notes: Api to handle the notes for each user, also made with flask
- user_notes_db: Mongo database service for users_notes

## API Reference

### Manage the user's data with the users API**

**/v1/users**

http://localhost:4001/v1/users

*Methods allowed: Get*

Fetch the list of registered users, it allow filtering if the URL parameters are sent like in this example: http://localhost:4001/v1/users?email=jesus@steer.com

**/v1/user**

http://localhost:4001/v1/user

*Methods allowed: Get, Post, Patch, Delete*

Manage the user data, it allow to send parameters in JSON format, to do that please confirm that you are sending the header: Content-Type: application/json

**Get**

For the get method, to query a specific user it is required to send the email as a parameter: http://localhost:4001/v1/user?email=jesus@steer.com

**Post**

It's used to create users in the database. To send the data for Post method please do it like in this example:

```json
{
    "name": "Jesus",
    "lastname": "Steer Varela",
    "gender": "Male",
    "email": "jesus3@steer.com"
}
```

**Patch**

It's used to update data for existing users. To send Patch request please use follow this example:

``` json
{
    "query": {
       "email": "jesus@steer.com"
    },
    "payload": {
        "name": "Jesus David"
    }
}
```

**Delete**

``` json
{
    "email": "jesus@steer.com"
}
```

### Manage the notes data for users with the user_notes API

**/v1/user_notes**

http://localhost:4002/v1/user_notes

*Methods allowed: Get*

Fetch the list of notes for an specific user, it required to send the email parameter like http://localhost:4002/v1/user_notes?email=jesus3@steer.com

**/v1/user_note**

http://localhost:4002/v1/user_note

*Methods allowed: Get, Post, Patch, Delete*

Manage the user notes data, it allows to send parameters in JSON format, to do that please confirm that you are sending the header: Content-Type: application/json

**Get**

For the get method, to query a specific user it is required to send the email as a parameter: http://localhost:4001/v1/user?email=jesus@steer.com

**Post**

It's used to create user notes in the database. To send the data for Post method please do it like in this example:

```json
{
    "email":    "jesus2@steer.com",
    "title":    "Testing",
    "body":     "This is the body."
}
```

Others request methods are used similar to the user API.

## Requirements

To run this project locally you need Docker and Docker Compose, to install it you can follow the instructions in these links:

- https://docs.docker.com/install/
- https://docs.docker.com/compose/install/

## Prerequisites

Clone the files locally. Move to the root directory using the console and run this command and wait for the containers to get ready and running.:

```console
foo@bar:~$ docker-compose up --build
```

## Running the application:

Please, run the docker containers:

```console
foo@bar:~$ docker-compose up
```

*If the containers are already running, just continue with the next step.*

Open a browser and access to: http://localhost:4000/

Should be able to see the user list, please add some users. You can also edit or delete them.

With some users created you can create some notes using the 'New node' icon in each row.

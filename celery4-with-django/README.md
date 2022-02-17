# celery4 with django

https://betterprogramming.pub/breaking-down-celery-4-x-with-python-and-django-e95eeb7de2a6

## NOTE

### what is celery

the message queue model to distributed computation across one or more nodes leveraging the AMQP (Advanced Message Queuing Protocol).

![high-level python celery architecture flow](https://miro.medium.com/max/1400/1*0iENRKlQlqeVOcYjEQHR-A.png)

> in this example `celery` use redis as **message broker**

### setup

```sh
brew install redis

pipenv shell
```

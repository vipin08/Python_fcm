# Notify-fcm

Simple FCM (Firebase Cloud Messaging) Gem for sending Push Notifications to iOS as well as Android devices

## Installation

```python
$ pip install python_fcm
```


## Requirements

* One of the following, tested Ruby versions:

```python
2.7.x
```
```python
3.6.x
```

## Usage

* Example sending notifications:

```python
from python_fcm import Fcm

fcm = Fcm("API-KEY")

device_token= ["xxxxxxxx", "xxxxxxx"] # an array of one or more client device tokens

fcm.title="My Title"                  # Set Title

fcm.body ="My Body"                   # Set Body

fcm.color = "#000000"                 # Set Colour Code

fcm.sound = "default"                 # Set your Notification sound

response = fcm.send(device_token)     # Send Notification
```

# MIT License

* Copyright (c) 2017 Vipin Kumar. See LICENSE.txt for details.

# Thanks and Support us
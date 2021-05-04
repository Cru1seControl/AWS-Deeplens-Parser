# AWS-Deeplens-Parser
A simple parser written in python for [Amazon Deeplens](https://aws.amazon.com/deeplens/).

This simple parser allows for Amazon Deeplens owners to easily
parse their downloaded data from the MQTT test client.

## Usage 
```python3
from deeplens import deeplens

with open("subscription.json", "r") as sub:
    sub = sub.read()

deeplens = deeplens(sub)
```

The data then can be parsed 3 different ways using the different
download types featured: JSON, strings, raw.

## Functions 
```python3
deeplens.face()       #returns an array containing chance of face data.
deeplens.max()        #maxium chance of face.
deeplens.min()        #minium chance of face.
deeplens.avg()        #average chance of face total.
deeplens.timestamps() #list containing timestamps logged.
deeplens.format()     #formatting type returns python object type dict, str, or bytes.
deeplens.topic()      #topic id set
deeplens.qos()        #Quality of Service returns a bool.
```

# MQTT-Protocol

## Intoduction

MQTT stands for message Queue Telemetry transport, it is a protocol used for low bandwidth machine to machine communication(specially for IoT applications). For a brief introduction you can use this [link](https://www.youtube.com/watch?v=EIxdz-2rhLs)

MQTT broker is the core of this protocol as it is responsiblefor communication. It is available as an application and you can install it [here](https://bytesofgigabytes.com/mqtt/installing-mqtt-broker-on-windows/) 

There are two types of MQTT clients , MQTT publisher(one who sends the data to the channel) and MQTT subscriber(one who receives the data from the channel). A client can be an application on your system or a sensor/actuator.

## PROBLEM STATEMENT
Two set of codes have been written
1. Publisher
2. Subscriber
In this model Publisher sends a message which will be received by the Subscriber who is constantly listening to the message port. The connection between them is handled by a ‘Broker’.
- Codes have been written in Python Language with the help of ‘paho’
which provides a client class with MQTT Protocol
- Here, both the publisher and subscriber has been set up in the same machine, i.e., we use the ‘localhost’ address to loopback to the same machine.
- We made use of port 1883 which is the default for MQTT and set the status as ‘LISTEN’

## ALGORITHM

1. Once the connection has been set up, At the publisher end, the user will be asked for the control of the LED i.e., ON or OFF or Exit from the loop.
2. If the user selects ‘ON’, then the command of turning ‘ON’ the LED with brightness level 1 will be send.
3. So now the LED will be with brightness level 1 and now the user is asked to choose the level of brightness from 5 different levels. There will also be an option to turn off the LED.
4. If the user chose to turn OFF the LED, then program will loopback to the step 1 again
5. Simultaneously the messages which are send to the subscriber will be displayed in the subscriber terminal.

## SCREENSHOTS
- PUBLISHER:

![image](https://user-images.githubusercontent.com/86975877/148678268-df6b25f8-a7eb-4f1e-8415-524615279fd4.png)

- SUBSCRIBER

![image](https://user-images.githubusercontent.com/86975877/148678293-55eece1c-0499-4456-b068-42eb0884608c.png)



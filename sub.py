import paho.mqtt.client as paho

broker="localhost"  #loopback
topic="LED"

#Function to display palyload received      
def on_message(client, userdata, message):
  print('INSTRUCTION : ',str(message.payload.decode("utf-8")) ) #printing Received message
  print("")

    
sub= paho.Client("subscriber") #create client object 
sub.on_message=on_message #Assigning fuction to on_message
   
print("connecting to ",broker,'.....')
sub.connect(broker)  #Establishing connection with Broker
print("Listening ....")    
sub.subscribe(topic) 

while 1:
    sub.loop_start() #contineously checking for message 

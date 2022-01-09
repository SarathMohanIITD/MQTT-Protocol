import paho.mqtt.client as paho #mqtt library

broker="localhost" #Loopback
topic="LED"; #topic name
port=1883 
ACCESS_TOKEN= 'led_control'

#  Callback function
def on_publish(client,userdata,result):
  print("PUBLISHED SUCESSFULLY\n\n")
  pass

pub= paho.Client("publisher") #create client object
pub.on_publish = on_publish #assign function to callback
pub.username_pw_set(ACCESS_TOKEN) 
pub.connect(broker,port,keepalive=60) #establishing connection

# LED Menu
while True: 
  print('\t\t LED MENU')
  print('\tType "ON" to turn on LED\n\tType "OFF" to turn off LED\n\t(Type "EXIT" to exit)\n\t')
  payload = input('Type the instruction : ')
  if payload == 'ON':
    payload = 'LED ON'
    ret = pub.publish(topic,payload)
    print('LED ON with brightness =  *  \n')
    us_ip=''
    while(us_ip != 'OFF'):
      print('\n\t\tBRIGHTNESS CONTROL MENU\n\tChoose the brightness level')
      print('\t1. *')
      print('\t2. **')
      print('\t3. ***')
      print('\t4. ****')
      print('\t5. *****')
      us_ip = input('\tType "OFF" to turn off\n Choose Your Option :  ')
      if us_ip == '1':
        payload = 'LED ON\t Set Brightness : *'
        ret = pub.publish(topic,payload)
      elif us_ip == '2':
        payload = 'LED ON\tSet Brightness : **'
        ret = pub.publish(topic,payload)
      elif us_ip == '3':
        payload = 'LED ON\tSet Brightness : ***'
        ret = pub.publish(topic,payload)
      elif us_ip == '4':
        payload = 'LED ON\tSet Brightness : ****'
        ret = pub.publish(topic,payload)
      elif us_ip == '5':
        payload = 'LED ON\tSet Brightness : *****'
        ret = pub.publish(topic,payload)
      elif us_ip == 'OFF':
        payload = 'LED OFF'
        ret = pub.publish(topic,payload)
        break
      elif payload == 'OFF':
        ret = pub.publish(topic,payload)
  elif payload == 'OFF':
    payload == 'LED OFF'
    ret = pub.publish(topic,payload)
  elif payload == 'EXIT':
    print('Exiting....') 
    exit()
  else:
    print("Wrong Choice, Try again ....\n")
    

 
  

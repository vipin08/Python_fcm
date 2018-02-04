import requests
import os
class Fcm:

  CONTANT_TYPE = 'application/json'
  FCM_END_POINT = "https://fcm.googleapis.com/fcm/send"

  FCM_MAX_RECIPIENTS = 1000
  FCM_LOW_PRIORITY = 'normal'
  FCM_HIGH_PRIORITY = 'high'
  body =''
  title =''
  icon = ''
  sound = ''
  color = ''
  notification_type= 1 # 1 for notification and other for data

  REGISTRATION_IDS = [] # Client FCM token

  def __init__(self, api_key):
      if api_key:
          self._FCM_API_KEY = api_key
      elif os.getenv('FCM_API_KEY', None):
          self._FCM_API_KEY = os.getenv('FCM_API_KEY', None)
      else:
          raise AuthenticationError("Please provide the api_key in the google-services.json file")

  def message_body(self):
    if((self.notification_type == 1) or (self.notification_type == '')):
  	   {'notification': { 'body': self.body, 'title': self.title, 'icon': self.icon, 'sound': self.sound, 'vibrate': True, 'color': self.color, 'priority': self.FCM_HIGH_PRIORITY}}
    else:
      {'data': { 'body': self.body, 'title': self.title, 'icon': self.icon, 'sound': self.sound, 'vibrate': True, 'color': self.color, 'priority': self.FCM_HIGH_PRIORITY}}


  def build_body(self, registration_ids, options = {}):
    { 'registration_ids': registration_ids }

  def send(self, registration_ids):
    if registration_ids:
      self.REGISTRATION_IDS = registration_ids
    else:
      raise AuthenticationError("Please provide the FCM Token")

    message = self.message_body()
    m_body = self.build_body(self.REGISTRATION_IDS, message)

    params = {
      'body': m_body,
      'headers': {
        'Authorization': "key=" + self._FCM_API_KEY,
        'Content-Type': self.CONTANT_TYPE
      }
    }
    response = requests.post(self.FCM_END_POINT, data = params)
    if(response.status_code == 200):
      response_body = {'result':{'status': 'true', 'message': 'Succssfully Sent', 'response': response.body}}
    elif(response.status_code == 400):
      response_body = {'result':{'status': 'false', 'message': 'Json Fields are invalid','response': ''}}
    elif(response.status_code == 401):
      response_body = {'result':{'status': 'false', 'message': 'Authentication Error!','response': ''}}
    elif(response.status_code == 503):
      response_body = {'result':{'status': 'false', 'message': 'Server is temporarily unavailable.', 'response': ''}}
    else:       
      response_body= {'result':{'status': 'false', 'message': 'Server is temporarily unavailable.', 'response': ''}}
    return response_body






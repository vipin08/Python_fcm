import requests
import os

class Fcm:

  CONTANT_TYPE = 'application/json'
  FCM_END_POINT = "https://fcm.googleapis.com/fcm/send"

  FCM_MAX_RECIPIENTS = 1000
  FCM_LOW_PRIORITY = 'normal'
  FCM_HIGH_PRIORITY = 'high'
  BODY =''
  TITLE =''
  ICON = ''
  SOUND = ''
  COLOR = ''
  REGISTRATION_IDS = []

  def __init__(self, api_key):
      if api_key:
          self._FCM_API_KEY = api_key
      elif os.getenv('FCM_API_KEY', None):
          self._FCM_API_KEY = os.getenv('FCM_API_KEY', None)
      else:
          raise AuthenticationError("Please provide the api_key in the google-services.json file")

  def message_body(self):
  	{'notification': { 'body': self.BODY, 'title': self.TITLE, 'icon': self.ICON, 'sound': self.SOUND, 'vibrate': True, 'color': self.COLOR, 'priority': self.FCM_HIGH_PRIORITY}}


  def build_body(self, registration_ids, options = {}):
    { 'registration_ids': registration_ids }

  def send(self, registration_ids):
    if registration_ids:
      self.REGISTRATION_IDS = registration_ids
    else:
      raise AuthenticationError("Please provide the FCM Token")

    message = self.message_body()
    body = self.build_body(self.REGISTRATION_IDS, message)
    params = {
      'body': body,
      'headers': {
        'Authorization': "key=" + self._FCM_API_KEY,
        'Content-Type': self.CONTANT_TYPE
      }
    }
    print(params)
    r = requests.post(self.FCM_END_POINT, data = params)


# f = Fcm('asdasdsdsd')
# # f.api_key = "hello"
# f.fcm_data()

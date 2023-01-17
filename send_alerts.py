# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:40:50 2023

@author: PGS2KOR
"""
def send_to_controller(breachType): 
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')

def send_alerts(alertTarget, breachType):
    if alertTarget == 'TO_CONTROLLER':
      send_to_controller(breachType)
    elif alertTarget == 'TO_EMAIL':
      send_to_email(breachType)
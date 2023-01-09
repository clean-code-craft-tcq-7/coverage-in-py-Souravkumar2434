from limits import LIMITS
from send_alerts import send_to_controller, send_to_email


def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'



def check_and_alert(alertTarget, batteryChar, temperatureInC):
  lowerlimit, upperlimit = LIMITS(batteryChar['coolingType'])
  breachType =\
    infer_breach(temperatureInC, lowerLimit, upperLimit)
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)



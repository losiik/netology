LUCKY = 'Счастливый билет'
NON_LUCKY = 'Несчастливый билет'


def is_lucky(ticket_num: str):
  first_part = [int(num) for num in ticket_num[:3]]
  last_part = [int(num) for num in ticket_num[3:]]

  if sum(first_part) == sum(last_part):
      return LUCKY
  return NON_LUCKY


ticket = input("Input ticket number: ")
print(is_lucky(ticket))
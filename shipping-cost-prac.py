## will calculate shipping cost and suggest the cheapest option
#enter weight of package
weight = 40
#calculate ground shipping cost
def ground_shipping_cost(weight):
  if weight <= 2:
    return weight * 1.50 + 20
  if weight > 2 and weight <= 6:
    return weight * 3.00 + 20
  if weight > 6 and weight <=10:
    return weight * 4.00 + 20
  else:
    return weight * 4.75 + 20
#make variable equal to return from ground_shipping_cost
ground_shipping = ground_shipping_cost(weight)
#calculate drone shipping cose
def drone_shipping_cost(weight):
  if weight <= 2:
    return weight * 4.50
  if weight > 2 and weight <= 6:
    return weight * 9.00
  if weight > 6 and weight <=10:
    return weight * 12.00
  else:
    return weight * 14.75
#make variable equal to drone_shipping_cost
drone_shipping = drone_shipping_cost(weight)
#one price variable for premium ground shipping
premium_ground_shipping = 125
#calculate cheapest option and return
def best_shipping_option(ground_shipping, drone_shipping, premium_ground_shipping):
  if ground_shipping<drone_shipping and ground_shipping<premium_ground_shipping:
    return print("Your cheapest option would be ground shipping for " + str(ground_shipping) + " dollars.")
  if drone_shipping<ground_shipping and drone_shipping<premium_ground_shipping:
    return print("Your cheapest option would be drone shipping for " + str(drone_shipping) + " dollars.")
  if premium_ground_shipping<ground_shipping and premium_ground_shipping<drone_shipping:
    return print("Your cheapest option would be premium ground shipping for " + str(premium_ground_shipping) + " dollars.")
#execute cheapest option string return
best_shipping_option(ground_shipping, drone_shipping, premium_ground_shipping)
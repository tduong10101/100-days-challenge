sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# Write your code below:
result = {word:len(word) for word in sentence.split()}


print(result)


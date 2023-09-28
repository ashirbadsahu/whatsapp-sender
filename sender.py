import pywhatkit

# Define the message you want to send
message = "Hii Ashish!"

phone_numbers = ["+919999999999", "+918888888888"]

# Send the message to each phone number in the list
for phone_number in phone_numbers:
    pywhatkit.sendwhatmsg(phone_number, message, 19, 36)

print("Messages sent successfully!")

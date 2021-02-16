# # works with both python 2 and 3
# from __future__ import print_function

# import africastalking

# class SMS:
#     def __init__(self):
# 		# Set your app credentials
#         self.username = "YOUR_USERNAME"
#         self.api_key = "YOUR_API_KEY"

# 		# Initialize the SDK
#         africastalking.initialize(self.username, self.api_key)

# 		# Get the SMS service
#         self.sms = africastalking.SMS

#     def fetch_subscriptions_sync(self):
# 		# Set your premium product shortCode and keyword
#         shortCode = "MyAppShortCode";
#         keyword = "MyAppKeyword";

#         # Our API will return 100 subscription numbers at a time back to you,
# 		# starting with what you currently believe is the lastReceivedId.
# 		# Specify 0 for the first time you access the method and the ID of
# 		# the last subscription we sent you on subsequent calls
#         try:
# 			lastReceivedId = 0;

#             # Fetch all messages using a loop
#             while True:
#                 subcriptionData = self.sms.fetch_subscriptions(shortCode, keyword, lastReceivedId)
#                 subcriptions = subcriptionData['responses']
#                 if len(subcriptions) == 0:
#                     print ('No subscription numbers.')
#                     break
#                 for subscription in subscriptions:
#                     print ('phone number : %s;' % subscription['phoneNumber'])
# 					# Reassign the lastReceivedId
#                     lastReceivedId = subscription['id']

# 		    # Note: Be sure to save the lastReceivedId for next time
#         except Exception as e:
#             print ("Error creating subscription:%s" %str(e))

# if __name__ == '__main__':
#     SMS().fetch_subscriptions_sync()
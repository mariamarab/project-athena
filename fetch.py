import requests

url = 'https://machinereading.azurewebsites.net/api'
#passage = input("Enter the passage: ") 
#question = input("Enter the question: ")
passage = "In mathematics, a geometric series is a series with a constant ratio between successive terms."
question = "What is geometric series?"

print("==============")
print("Passage: \n", passage)
print("==============")
print("Question: \n", question)
print("==============")

PARAMS = {'question':question, "passage":passage}
r = requests.post(url = url, json=PARAMS)

print(r.text)










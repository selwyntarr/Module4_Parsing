import json

#example of json
sample_json = '{"name":"John", "age":"30", "city":"New York City"}'

#parse json
parsed_json = json.loads(sample_json)
print("The output of json file is ", parsed_json)

print("Name: ", parsed_json["name"])
print("Age: ", parsed_json["age"])
print("City: ", parsed_json["city"])

import json

your_file = input("Enter a json name:")

with open(your_file, "r") as file:
    data = json.loads(file.read())
    
    def get_value_by_key(date, key):
        stack = [date]
        while stack:
            present = stack.pop()
            if isinstance(present, dict):
                for keys, value_key in present.items():
                    if keys == key:
                        return value_key
                    stack.append(value_key)
        return None

key = input("Enter the name of the key: ")
result = get_value_by_key(data, key)
print(f"Key data '{key}': {result}")
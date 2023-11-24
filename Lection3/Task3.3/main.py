import json

json_data = '''
{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": [
                            "GML",
                            "XML"
                        ]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
'''

def get_value_by_key(json_data, key):
    data = json.loads(json_data)
    
    if key in data:
        return data[key]
    else:
        return "Key not found"

desired_key = input("Enter the key: ")

result = get_value_by_key(json_data, desired_key)
print(f"Value by key '{desired_key}': {result}")
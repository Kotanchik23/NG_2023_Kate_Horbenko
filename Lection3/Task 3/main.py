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
data = json.loads(json_data)

def get_value_by_key(data, key):
    print(data, key, '\n\n')
    if key in data:
        return data[key]
    for keys, value in data.items():
        if isinstance(value, dict):
            found = get_value_by_key(value, key)
            if found is not None:
                return found
            
key = input("Enter the name of the key: ")
result = get_value_by_key(data, key)
print(f"Key data '{key}': {result}")
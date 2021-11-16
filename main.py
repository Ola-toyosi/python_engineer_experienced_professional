import json
import jsonschema
from jsonschema import validate
import genson
from genson import SchemaBuilder


jsonFile = input('Enter file name:')


try:
    f = open(f'./data/{jsonFile}.json', )
    jsonData = json.load(f)
    f.close()
    output_dict = {}

    for i in jsonData['message']:
        builder = SchemaBuilder()
        builder.add_schema(jsonData['message'][f'user'])
        builder.add_schema({"description": ''})
        builder.add_schema({"tag": ''})
        builder.add_schema({"required": False})

        schemaP = builder.to_schema()

        # with open(f"./schema/sampschema_{i}.json", "w") as outfile:
        #     json.dump(schemaP, outfile)

        print(schemaP)
        print(schemaP.get('description'))
        print(schemaP.get('required'))

        builder2 = SchemaBuilder()
        builder2.add_object(jsonData['message'][f'{i}'])

        schema2 = builder2.to_schema()

        # print(schema2)
        # print(schema2.get('type'))
        # print(schema2)

        output_dict[f'{i}'] = {
                                  "type": schema2.get('type'),
                                  "tag": schemaP.get('tag'),
                                  "description": schemaP.get('description'),
                                  "required": schemaP.get('required')
                              },

        with open(f"./schema/schema_1.json", "w") as outfile:
            json.dump(output_dict, outfile)
except FileNotFoundError as err:
    print(err)
    err = 'File not in directory'


# def get_schema():
#     # """This function loads the given schema available"""
#     with open('./schema/sampschema_1.json', 'r') as file:
#         schema = json.load(file)
#     print (schema)
#
# get_schema()

# schemaFile = get_schema()


# def validateJson(jsonData):
#     try:
#         validate(instance=jsonData, schema=schemaFile)
#     except jsonschema.exceptions.ValidationError as err:
#         print(err)
#         err = "Given JSON data is InValid"
#         return False, err
#     message = "Given JSON data is Valid"
#     return True, message


# is_valid, msg = validateJson(jsonData)
# print(msg)







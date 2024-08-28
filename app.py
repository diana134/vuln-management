import xmltodict
import flatdict

def print_keys(dic):
    for key, value in dic.items():
        print(key)
        if isinstance(value, dict):
            print_keys(value)



xml_file=open("reports/report-3d0c68dd-80e9-4708-a63a-db4fef7cbe1c.xml","r")
xml_string = xml_file.read()
data = xmltodict.parse(xml_string)
# print_keys(data)
flat_data = flatdict.FlatDict(data, delimiter='.')
print_keys(flat_data)
truly_flat_data = dict(flat_data)

# for key, value in truly_flat_data.items():
#     print(key, value)
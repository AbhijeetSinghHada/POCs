
def to_upper(value):
    return value.upper()


source_dict = {
    "name": ["abhijeet", "hada"],
    "address": {
        "flat": "123",
        "street_name": "ABC"
    }
}
source_dict.get("name", "")

mapper = {
    "user.firstname": ["name", lambda x : x[0]], # name[0]
    "user.lastname": ["name", lambda x : x[1]],# name[1]
    "user.address.house_number": "address.flat",
    "user.address.street_name": "address.street_name",
    "abhi.address.street_name": "address.street_name",
    "full_name.lowername": "name_s",
}

response_dict = {'user': {'name': 'ABHIJEET', 'address': {'house_number': '123', 'street_name': 'ABC'}}, 'abhi': {
    'address': {'street_name': 'ABC'}}, 'full_name': {'lowername': None}}


class Mapper:
    """This class maps a source dictionary to a target dictionary based on a mapping dictionary."""
    def __init__(self, source_dict, mapping_dict):
        self.source_dict = source_dict
        self.mapping_dict = mapping_dict
        self.response_dict = {}

    def map_dict(self):
        for key, value in self.mapping_dict.items():
            self._map(key, value)
        return self.response_dict

    def _map(self, key, value):
        """This method maps a key from the source dictionary to a key in the response dictionary based on the mapping dictionary."""
        keys = key.split(".")
        if isinstance(value, list) and len(value) == 2:
            target_keys = value[0].split(".")
            target_value = self._get_target_value(target_keys, self.source_dict)

            if callable(value[1]):
                # Checking if second element is a function and calling it with target value to transform
                caller_function = value[1]
                target_value = caller_function(target_value)
        else:
            target_keys = value.split(".")
            target_value = self._get_target_value(target_keys, self.source_dict)

        if target_value is not None:
            self._set_value_to_response(keys, target_value, self.response_dict)

    def _set_value_to_response(self, keys, value, response_dict):
        if len(keys) == 1:
            if value is not None:
                response_dict[keys[0]] = value
            return
        
        key = keys[0]
        if key not in response_dict:
            response_dict[key] = {}

        self._set_value_to_response(keys[1:], value, response_dict[key])

    def _get_target_value(self, keys, source_dict):
        if len(keys) == 1:
            return source_dict.get(keys[0])
        else:
            return self._get_target_value(keys[1:], source_dict[keys[0]])

mapping = Mapper(source_dict, mapper)
print(mapping.map_dict())


# mapping_dictt = {
#     "EmailAlias" : "missing",
#     "EmailDomain" : "missing",
#     "PassowordCount" : "NotFound",
#     "Passwords" : "",
#     "Breaches" : "",
# }

# print(list(mapping_dictt.keys()))

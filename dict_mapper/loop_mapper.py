class Mapper:
    def __init__(self, source_dict, mapper):
        self.source_dict = source_dict
        self.mapper = mapper
        self.transformed_dict = {}
    
    def map_dict(self):
        for key, value in self.mapper.items():
            self._map_key_value(key, value)
        return self.transformed_dict
    
    def _map_key_value(self, key, value):
        source_keys = key.split(".")
        value_keys = value.split(".")
        transformed_dict = self.transformed_dict
        for source_key in source_keys[:-1]:
            if source_key not in transformed_dict:
                transformed_dict[source_key] = {}
            transformed_dict = transformed_dict[source_key]
        
        last_source_key = source_keys[-1]
        value = self._get_value_from_dict(value_keys, self.source_dict)
        if value:
            transformed_dict[last_source_key] = value
    
    def _get_value_from_dict(self, keys, source_dict):
        for key in keys:
            source_dict = source_dict.get(key)
            if source_dict is None:
                return None
        return source_dict
    

source_dict = {
    "name": "abhijeet",
    "address" : {
        "flat" : ["123"], 
        "street_name" : "ABC"
    }
}

mapper = {
    "user.name" : "name",
    "user.address.house_number": "address.flat",
    "user.address.street_name" : "address.street_name",
    "abhi.address.street_name" : "address.street_name",
    "full_name.first_name" : "name_s.price"
}

transformed_dict = {
    "user": {
        "name": "abhijeet",
        "address": {
            "house_number": ["123"],
            "street_name": "ABC"
        }
    },
    "full_name": "abhijeet"
}

mapping = Mapper(source_dict, mapper)
print(mapping.map_dict())

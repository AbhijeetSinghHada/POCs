from .mapper import Mapper

def get_data_classes(data : dict):
    return list(data.keys())

def check_validity_by_score(validated : int):
    # To be Discussed
    return validated//80

def check_sensitivity(senstivity: str):
    # To be Discussed
    if senstivity == "High":
        return 1
    return 0
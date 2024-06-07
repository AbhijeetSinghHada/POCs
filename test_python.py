
def test_func(lst):

    if lst and type(lst) is list:
        print(lst)
    else:
        print("not list bro")

def test_func2(lst):

    if isinstance(lst, list):
        print(lst, "Part 2")
    else:
        print("not list bro part 2")

def test_return_params():
    return "abhi", True

def get_dict_mapping(data, resources, default_type=str):
    temp_data = data
    val = None
    for resource in resources:
        map_res = temp_data.get(resource, None)
        if isinstance(map_res, dict):
            temp_data = temp_data.get(resource)
        else:
            val = temp_data.get(resource)
    else:
        return val
    return default_type()


def test_error():
    
    try:
        print("try")
        raise Exception("Error")
    except Exception as e:
        print("exception")
        raise e
    finally:
        print("finally")


def main(event):
    f"""event, {event}"""
    pass


if __name__=="__main__":
    main("hello")
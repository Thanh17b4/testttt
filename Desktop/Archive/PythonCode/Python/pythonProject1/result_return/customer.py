
#Best way

def serialize_dict(customer) -> dict:
    # return {**{i:int(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}
    return {
        "_id": int(customer["_id"]),
        "name": customer["name"],
        "address": customer["address"],
    }


def serialize_list(list_customers) -> list:
    return [serialize_dict(c) for c in list_customers]
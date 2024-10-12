from fastapi import APIRouter, Response, status
from passlib.context import CryptContext
from config.db import db
from models.check_data import is_blank, is_integer
from schemas.schemas import Customer
from result_return.customer import serialize_dict, serialize_list

customers_router = APIRouter()
DB = db()["customers"]


@customers_router.get('/customers/all', status_code=200)
async def customers(limit: int, page: int, response: Response):
    if is_integer(limit) is False or is_integer(page) is False:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return f"page and limit must be number"
    total_customers = DB.estimated_document_count()
    d = total_customers % limit
    if d == 0:
        total_page = total_customers // limit
    else:
        total_page = total_customers // limit + 1
    offset = (page - 1) * limit
    if page > total_page or page <= 0:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return f"page is not exist, total page is {total_page}"
    else:
        pipeline = [
            {'$match': {}},
            {
                '$skip': offset
            }, {
                '$limit': limit
            }
        ]
        return serialize_list(DB.aggregate(pipeline))
        # return serialize_list(db().find().limit(limit).skip(offset))


@customers_router.get('/customers/detail/{id}', status_code=200)
async def find_one_customer(id: int, response: Response):
    if is_integer(id) is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return f"customer id must be number"
    a = DB.find_one({"_id": int(id)})
    if a is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return f"id is not correct"
    return serialize_dict(a)


@customers_router.put('/customers/update/{id}', status_code=200)
async def update_user(id: int, customer: dict, response: Response):
    if is_integer(id) is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return f"customer id must be number"
    x = DB.find_one({"_id": id})
    if x is None or id != customer["_id"]:
        response.status_code = status.HTTP_404_NOT_FOUND
        return f"id  invalid"
    else:
        DB.find_one_and_update({"_id": id}, {
            "$set": customer
        })
    return serialize_dict(DB.find_one({"_id": int(customer["_id"])}))


@customers_router.delete('/customers/delete/{id}', status_code=200)
async def delete_customer(id: int, response: Response):
    if is_integer(id) is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return f"customer id must be number"
    x = DB.find_one({"_id": id})
    if x is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return f"id {id} invalid"
    else:
        DB.find_one_and_delete({"_id": int(id)})
        return f"customer ID {id} has been deleted"


@customers_router.post('/customers/create', status_code=201)
async def create_customer(req: dict, response: Response):
    # Validate data
    is_ok, msg = __validate(req)
    if is_ok is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return msg
    # check exits
    c = Customer(req).to_dict()
    x = DB.find_one({"_id": c["_id"]})
    if x is not None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return f"id {x.get('_id')} had been used"
    new_customer = DB.insert_one(c)
    return f"customer_id {new_customer.inserted_id} has been inserted successfully"


def __validate(req: dict):
    if req.get("_id") is None:
        return False, "_id cannot be null"
    if req.get("name") is None or is_blank(req.get("name")) is True:
        return False, "name cannot be null"
    if req.get("address") is None or is_blank(req.get("address")) is True:
        return False, "address cannot be null"
    return req, ""


def __hash_password(pwd: str):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(pwd)



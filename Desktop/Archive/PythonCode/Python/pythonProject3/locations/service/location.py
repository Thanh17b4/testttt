from slugify import slugify

from locations.model.check_data import is_blank
from locations.schemas import Location
from locations.repo.location import create_location_repo


def create_location_service(req: Location):
    location = req.location_to_dict()
    # Validate data
    is_ok, msg = __validate(location)
    if is_ok is False:
        return msg
    location["slug"] = slugify(location["name"])
    return create_location_repo(req)


def __validate(req: dict):
    if req.get("name") is None or is_blank(req.get("name")) is True:
        return False, "name cannot be null"
    return req, None

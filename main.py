"""
FASTAPI APP
"""
from enum import Enum,IntEnum
from fastapi import FastAPI
# FastAPI application instance
app = FastAPI()
class Cars(str, Enum):
    """
    Docstring for Cars
    """
    CAR1 = "Toyota"
    CAR2 = "Honda"
    CAR3 = "Ford"
    CAR4 = "BMW"
    CAR5 = "Mercedes"

class Users(str, Enum):
    """
    Docstring for Users
    """
    USER1 = "Ahmed"
    USER2 = "Mohamed"
    USER3 = "Sara"
    USER4 = "Abdullah"
    USER5 = "yoona"
class Price(IntEnum):
    """
    Docstring for Price
    """
    CAR1 = 20000
    CAR2 = 25000
    CAR3 = 30000
    CAR4 = 40000
    CAR5 = 50000
instocks= [
    {"car_name": Cars.CAR1, "in_stock": True},
    {"car_name": Cars.CAR2, "in_stock": False},
    {"car_name": Cars.CAR3, "in_stock": True},
    {"car_name": Cars.CAR4, "in_stock": False},
    {"car_name": Cars.CAR5, "in_stock": True},
]
@app.get("/")
async def index():
    """
    Docstring for index
    """
    return {"message": "Welcome to the Car API!"}
@app.post("/add_car/")
async def add_car(user:Users, car_name:Cars):
    """
    Docstring for add_car
    
    :param user: Description
    :type user: Users
    :param car_name: Description
    :type car_name: Cars
    """
    prices = Price[car_name.name]
    return{"message": {
        "user": user.value,
        "car_name": car_name.value,
        "price": f"the price is {prices.value} dollars"
    }  }
@app.get("/repository")
async def repository(start:int = 0, limit:int = 5,car_name:Cars = None):
    """
    Docstring for repository
    """
    if car_name:
        item = next((car for car in instocks if car['car_name'] == car_name),None)
        if item:
            return item
    return instocks[start:limit]
@app.get("/cars/price")
async def price_range(ranges:Price = None):
    """
    Docstring for price_range
    
    :param ranges: Description
    :type ranges: Price
    """
    if ranges:
        return {Cars[car.name] for car in Price if car.value <= ranges.value}
    return {"Message": "Please provide a price range to filter cars."}

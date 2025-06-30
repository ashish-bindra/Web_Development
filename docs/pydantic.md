# Pydatic

1. Pydantic model that represents the ideal schema of the data

    - this includes the expected fields, their types and any calidation constraints (gr=0)

2. Instantiate the model with raw input data(usually a dicttionary or JSON like strucure)

    - Pydantic will automatically validate the data and coerce it into the correct Python types
    - If the data doesnot meet the model requirments, Pydatic raises a ValidationError

3. Pass the validatied model object to functions or use it through your codebase.
    - This ensures that every part of your program works with clean, type-safe, and logically valid data.

Pydantic is mostly widly used data validation libray for python

## Why to use pydatic

Type hits powering schema validation

- The schema pydataic validation against is generally defined by python type hints

`pydantic-setting` : for envirmoment valiable
`python-env`: To load the enviroment valiable
pip install pydantic pydantic-setting

first model example

```py
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {"id": 101, "name": "chai", "is_active": True}

user = User(**input_data)

print(user)
```

## Assignment 1 : TODO: Create Product model with id, name,price, in_stock

```py

from pydantic import BaseModel

class ProductModel(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = False
```

---

## Type Hints

```py

from pydantic import BaseModel
from types import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    item: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
```

## Assignment 2: TODO: Create Employee model

    fields:

    - id: int
    - name: str(min 3 chars)
    - department: Optional str (default 'Hernal')
    - salary: float (must be >= 10000)

```py
from pydantic import BaseModel, Field
from types import List, Dict, Optional


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Ashish Bindra",
    )
    department: Optional[str] = "General"
    salary: float = Field(..., ge=10000)
```

## customise validator

field validators

- it run first (before)

```py
class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls,v):
        if len(v) < 4 :
            raise ValueError("Username must be atleast 4 charaters")
        return v
```

Model Validator

```py
class SignupData(BaseModel):
    passwprd: str
    confirm_password: str

    @model_validator(mode="after")
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password do not match')
        return values

```

computed field

```py
class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self)-> float:
        return self.price * self.quantity
```

## Asignment 3: TODO: Create Booking model

    Fields:
    - user_id: int
    - room_id: int
    - night: int (must be >= 1)
    - rate_per_night: float
    - also, add computed field: total_amount = night * rate_per_night

```py
from pydantic import BaseModel, Field, computed_field
from types import List, Dict, Optional

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float
    
    @computed_field
    @property
    def total_amount(self)-> float:
        return self.nights * self.rate_per_night
    
```

## Neasted model

```py
class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

#  self refrenceing / self replication
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None # forword refer rences

    Comment.model_rebuild()
address = Address(
    street = "123 something",
    city = "jaipur",
    postal_code = "10001"
)

user - User(
    id =  1,
    name = "ashish",
    address = address
)

comment = Comment(
    id = 1,
    content = "First content",
    replies = [
        Comment(id=2, contet = "reply2")
        Comment(id=3, contet = "reply2")
    ]
)
```

## Assignment TODO: Create Cource model

    - Each Cource has modules
    - Each module has lessons

```py
class Lesson(BaseModel):
    lesson_id: int
    topic: str

class Model(BaseModel):
    module_id: int
    name: str
    lessons: List[Lesson]

class Cource(BaseModel):
    cource_id: int
    title: str
    modules: List[Module]
```

## serialization

up and down

```py
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(Base):
    id: int
    name: str
    email: str
    is_active: bool = True
    createAt: datetime
    address: Address
    tage: List[Str] = []

# create a user instance

user = User(
    id=1
    name="ashish"
    email= "asish@gmail.com"
    created_at = datetime(2026,3,12,12,30)
    address= Address(
        street = "something",
        city = "patiala"
        zip_code = "12222
),
is_active =True,
    tags = ["premium", "subscriber"]
)

# Using model_dump() -> dict

python_dict = user.model_dump()

# using model_dump_json()
json_str = user.model_dump_json()
```

but the date and time is not geting correct in json encode

add the COnfigDict it will tel json encode how to encode

```py
model_config = ConfigDict(
    json_encoders = {
        datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
    }
)
```

Dependency enjection tips

```py
class UserSignup(baseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "Chai App"
    admin_email: str = "admin@xhai.com"

def get_settings():
    return Settings()

@app.post('/signup'):
def signup(user: UserSignup):
    return {'message': f'User {user.username} signed up successfully'}

@app.get('/settings')
def get_usetting_end(setting: Setting = Depends(get_settings))
```

Only include name

```py
patient.model_dump(include=['name', 'gender'])
patient.model_dump(exclude=['name', 'gender'])
patient.model_dump(exclude={'address':['state']})
```

### exclude unset

patient.model_dump(exclude_unset=True)

defalut value wioo not consider when we not provide during object creation

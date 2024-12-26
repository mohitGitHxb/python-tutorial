from typing import Dict, List, Union
from dataclasses import dataclass


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0.0

def get_student_info(name: str, age: int, grades: List[float]) -> Dict[str, Union[str, int, float]]:
    """Return a dictionary with student information."""
    average_grade = calculate_average(grades)
    return {
        "name": name,
        "age": age,
        "average_grade": average_grade
    }

# Example usage
student_info = get_student_info("Alice", 20, [85.5, 90.0, 78.0])
print(student_info)  # Output: {'name': 'Alice', 'age': 20, 'average_grade': 84.5}

# ?? null coalescing operator TypeScript to Python 
value = None
default_value = value if value is not None else "Default Value"
print(default_value)  # Output: "Default Value"

# ?. null checking operator TypeScript to Python
user = {"name": "Alice", "address": {"city": "Wonderland"}}

# Using get() method for dictionaries
city = user.get("address", {}).get("city")
print(city)  # Output: "Wonderland"

country = user.get("address", {}).get("country")  # country is None
print(country)  # Output: None





# TypeScript Code (for reference)
# interface Address {
#     street: string;
#     city: string;
#     zipCode: string;
# }
#
# interface User {
#     id: number;
#     name: string;
#     email: string;
#     address: Address;
#     getFullAddress(): string;
# }
#
# class UserImpl implements User {
#     constructor(
#         public id: number,
#         public name: string,
#         public email: string,
#         public address: Address
#     ) {}
#
#     getFullAddress(): string {
#         return `${this.address.street}, ${this.address.city}, ${this.address.zipCode}`;
#     }
# }
#
# const user: User = new UserImpl(1, "Alice", "alice@example.com", {
#     street: "123 Main St",
#     city: "Wonderland",
#     zipCode: "12345"
# });
# console.log(user.getFullAddress());

# Python Equivalent Code


@dataclass
class Address:
    street: str
    city: str
    zip_code: str

@dataclass
class User:
    id: int
    name: str
    email: str
    address: Address

    def get_full_address(self) -> str:
        """Return the full address of the user as a string.

        Returns:
            str: The full address of the user.
        """
        return f"{self.address.street}, {self.address.city}, {self.address.zip_code}"

# Creating an instance of User
user = User(
    id=1,
    name="Alice",
    email="alice@example.com",
    address=Address(
        street="123 Main St",
        city="Wonderland",
        zip_code="12345"
    )
)

# Output the full address
print(user.get_full_address())  # Output: 123 Main St, Wonderland, 12345

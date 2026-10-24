# 1. Global Configuration & State
# A dictionary where keys are unique identifiers (like phone numbers or emails)
# and values are nested dictionaries containing contact details.
contacts: dict[str, dict] = {}

# 2. Data Structure Layout Example:
# contacts = {
#     "0708194272": {"name": "Edward", "email": "edward@example.com"},
#     "0712345678": {"name": "Alex", "email": "alex@example.com"}
# }

# 3. Core Functions (Single Responsibility Principle)

def add_contact(contact_dict: dict, name: str, phone: str, email: str) -> bool:
    """Modifies the dictionary to add a new contact. Returns True if successful."""
    pass

def search_contacts(contact_dict: dict, search_query: str) -> dict:
    """Searches through names and phone numbers. Returns a filtered dictionary."""
    pass

def update_contact(contact_dict: dict, phone: str, **kwargs) -> bool:
    """Updates specific fields of an existing contact using keyword arguments."""
    pass

def delete_contact(contact_dict: dict, phone: str) -> bool:
    """Removes a key-value pair from the contact record safely."""
    pass

# 4. User Interface Functions

def display_all_contacts(contact_dict: dict) -> None:
    """Formats and prints the contact sheet cleanly using loops."""
    pass

def main_menu() -> None:
    """Orchestrates the main input loop and maps options to respective functions."""
    pass


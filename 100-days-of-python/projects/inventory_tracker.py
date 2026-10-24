#!/usr/bin/python3
"""Warehouse Inventory Tracker - Final foundational step before OOP."""

# 1. Centralized Data State
# Structure: { "SKU_ID": {"name": str, "quantity": int, "price": float} }
inventory: dict[str, dict] = {}


# 2. Core Logic Functions

def add_product(stock_dict: dict, sku: str, name: str, qty: int, price: float) -> tuple[bool, str]:
    """Adds a new unique product to the inventory dictionary.

    Returns (True, "Success Message") or (False, "Error Message if SKU exists").
    """
    pass


def update_stock_level(stock_dict: dict, sku: str, quantity_change: int) -> tuple[bool, str]:
    """Increments or decrements stock quantity (e.g., handling sales or shipments).

    Must prevent stock quantities from falling below zero.
    """
    pass


def calculate_total_valuation(stock_dict: dict) -> float:
    """Loops through all items and returns the total financial value of the warehouse.

    Formula: Sum of (quantity * price) for every item.
    """
    pass


# 3. User Interface Functions

def print_low_stock_alert(stock_dict: dict, threshold: int = 5) -> None:
    """Scans inventory and prints any items running critically low."""
    pass


def main_menu() -> None:
    """The main interactive terminal loop mapping inputs to functions."""
    pass


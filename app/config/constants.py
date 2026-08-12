# Waste Categories (as per biomedical rules and extended streams)
WASTE_CATEGORIES = [
    "YELLOW", "RED", "WHITE", "BLUE",  # Existing biomedical
    "ORGANIC", "PLASTIC", "PAPER", "GLASS", "E-WASTE", "HAZARDOUS", "GENERAL" # New
]

# Waste lifecycle statuses (extended)
WASTE_STATUS = [
    "CREATED", "PENDING_ASSIGNMENT", "ASSIGNED", "ACCEPTED",
    "COLLECTING", "COLLECTED", "IN_TRANSIT", "ARRIVED",
    "PROCESSING", "RECYCLED", "TREATED", "DISPOSED",
    "VERIFIED", "CANCELLED",
    "pending", "collected", "in_transit", "disposed" # Preserved for backward compatibility
]

# Priority levels
PRIORITIES = ["NORMAL", "HIGH", "CRITICAL"]

# Alert levels
ALERT_LEVELS = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

# Facility types
FACILITY_TYPES = ["Hospital","Clinic","Diagnostic Lab","Medical College"]

ACCOUNT_STATUS = ["PENDING", "ACTIVE","REJECTED"]

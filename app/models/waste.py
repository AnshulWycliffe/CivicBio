from mongoengine import (
    Document, StringField, FloatField, BooleanField,
    DateTimeField, ListField, DictField, ReferenceField
)
from datetime import datetime
from app.config.roles import Roles

from app.config.constants import WASTE_CATEGORIES, WASTE_STATUS, PRIORITIES
from zoneinfo import ZoneInfo
import uuid

IST = ZoneInfo("Asia/Kolkata")


class Waste(Document):    
    # Existing core fields
    category = StringField(choices=WASTE_CATEGORIES)
    quantity = FloatField()
    facility_id = ReferenceField("User")
    status = StringField(choices=WASTE_STATUS, default="CREATED")
    storage_location = StringField()
    collected_by = ReferenceField("User")
    disposed_by = ReferenceField("User")
    disposal_method = StringField()
    issue_type = StringField()
    remarks = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(IST))
    
    # New extended lifecycle fields
    batch_code = StringField(unique=True)
    subcategory = StringField()
    unit = StringField(default="kg")
    priority = StringField(choices=PRIORITIES, default="NORMAL")
    
    # Timestamps for lifecycle
    collection_requested_at = DateTimeField()
    collected_at = DateTimeField()
    transport_started_at = DateTimeField()
    arrived_at = DateTimeField()
    processed_at = DateTimeField()
    
    # Processing specifics
    recycled_quantity = FloatField(default=0.0)
    treated_quantity = FloatField(default=0.0)
    disposed_quantity = FloatField(default=0.0)
    processing_facility = ReferenceField("User")
    
    # Proofs and updates
    proof_files = ListField(StringField())
    updated_at = DateTimeField(default=lambda: datetime.now(IST))

    def save(self, *args, **kwargs):
        if not self.batch_code:
            year = datetime.now(IST).year
            # Generate a short unique ID (e.g., CB-WST-2026-ABCD12)
            short_id = str(uuid.uuid4()).split('-')[0].upper()
            self.batch_code = f"CB-WST-{year}-{short_id}"
            
        self.updated_at = datetime.now(IST)
        return super(Waste, self).save(*args, **kwargs)
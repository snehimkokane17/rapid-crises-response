from database import SessionLocal, Resource, Alert

db = SessionLocal()

db.add(Resource(name="City Emergency Shelter", type="shelter", address="123 Main St", lat=40.7128, lng=-74.0060))
db.add(Resource(name="General Hospital", type="hospital", address="456 Oak Ave", lat=40.7138, lng=-74.0070))
db.add(Resource(name="Red Cross Center", type="shelter", address="789 Park Rd", lat=40.7148, lng=-74.0080))
db.add(Resource(name="Food Relief Camp", type="food", address="321 Lake Blvd", lat=40.7158, lng=-74.0090))

db.add(Alert(title="Flash Flood Warning", description="Avoid low-lying areas", severity="high"))
db.add(Alert(title="Earthquake Alert", description="Stay away from buildings", severity="high"))

db.commit()
db.close()
print("Sample data added successfully!")
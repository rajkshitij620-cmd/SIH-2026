"""Seed MongoDB when MONGODB_URI is configured; demo mode has built-in seed data."""
from app.database.store import store
from app.database.demo_data import DESTINATIONS, BUSINESSES
if __name__=='__main__':
 if store.mongo is None: print('DEMO_MODE: built-in demo data is already available.')
 else:
  store.mongo.destinations.delete_many({}); store.mongo.businesses.delete_many({})
  store.mongo.destinations.insert_many(DESTINATIONS); store.mongo.businesses.insert_many(BUSINESSES)
  store.mongo.users.create_index('email', unique=True); store.mongo.itineraries.create_index([('user_id', 1), ('saved', 1)]); store.mongo.itineraries.create_index([('destination.name', 1), ('input.start_date', 1), ('input.end_date', 1), ('input.travel_type', 1)]); store.mongo.destinations.create_index([('location.coordinates','2dsphere')])
  print('Seed complete.')

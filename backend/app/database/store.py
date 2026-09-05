from app.database.demo_data import DESTINATIONS, BUSINESSES
from app.config import settings
from pymongo import MongoClient
from pymongo.errors import PyMongoError

class Store:
 def __init__(self):
  self.users={}; self.itineraries={}; self.connections={}; self.groups={}; self.group_messages={}; self.mongo=None
  if settings.mongodb_uri:
   try: self.mongo=MongoClient(settings.mongodb_uri, serverSelectionTimeoutMS=1500)[settings.database_name]; self.mongo.command('ping')
   except Exception: self.mongo=None
 def destinations(self):
  if self.mongo is not None:
   try: return self._clean_many(self.mongo.destinations.find({}, {'_id': 0})) or DESTINATIONS
   except PyMongoError: pass
  return DESTINATIONS
 def businesses(self):
  if self.mongo is not None:
   try: return self._clean_many(self.mongo.businesses.find({}, {'_id': 0})) or BUSINESSES
   except PyMongoError: pass
  return BUSINESSES
 @staticmethod
 def _clean(document):
  if not document: return document
  document.pop('_id', None)
  return document
 def _clean_many(self, documents): return [self._clean(x) for x in documents]
 def user_by_email(self, email):
  if self.mongo is not None:
   try: return self._clean(self.mongo.users.find_one({'email': email}))
   except PyMongoError: return None
  return next((x for x in self.users.values() if x['email']==email), None)
 def user_by_id(self, identifier):
  if self.mongo is not None:
   try: return self._clean(self.mongo.users.find_one({'id': identifier}))
   except PyMongoError: return None
  return self.users.get(identifier)
 def create_user(self, user):
  if self.mongo is not None:
   self.mongo.users.insert_one(user.copy())
  else: self.users[user['id']]=user
  return user
 def update_user(self, identifier, fields):
  if self.mongo is not None:
   self.mongo.users.update_one({'id': identifier}, {'$set': fields})
   return self.user_by_id(identifier)
  self.users[identifier].update(fields)
  return self.users[identifier]
 def users_by_ids(self, identifiers):
  if self.mongo is not None:
   try: return self._clean_many(self.mongo.users.find({'id': {'$in': identifiers}}, {'_id': 0}))
   except PyMongoError: return []
  return [self.users[x] for x in identifiers if x in self.users]
 def save_itinerary(self, itinerary):
  if self.mongo is not None: self.mongo.itineraries.insert_one(itinerary.copy())
  else: self.itineraries[itinerary['id']]=itinerary
  return itinerary
 def itinerary_by_id(self, identifier):
  if self.mongo is not None:
   try: return self._clean(self.mongo.itineraries.find_one({'id': identifier}))
   except PyMongoError: return None
  return self.itineraries.get(identifier)
 def update_itinerary(self, identifier, fields):
  if self.mongo is not None:
   self.mongo.itineraries.update_one({'id': identifier}, {'$set': fields})
   return self.itinerary_by_id(identifier)
  if identifier in self.itineraries: self.itineraries[identifier].update(fields)
  return self.itineraries.get(identifier)
 def delete_itinerary(self, identifier):
  if self.mongo is not None: return bool(self.mongo.itineraries.delete_one({'id': identifier}).deleted_count)
  return self.itineraries.pop(identifier, None) is not None
 def saved_itineraries(self, user_id):
  if self.mongo is not None:
   try: return self._clean_many(self.mongo.itineraries.find({'user_id': user_id, 'saved': True}, {'_id': 0}))
   except PyMongoError: return []
  return [x for x in self.itineraries.values() if x['user_id']==user_id and x.get('saved')]
 def itineraries_for_user(self, user_id):
  if self.mongo is not None:
   try: return self._clean_many(self.mongo.itineraries.find({'user_id': user_id}, {'_id': 0}))
   except PyMongoError: return []
  return [x for x in self.itineraries.values() if x['user_id']==user_id]
 def group_trips(self, destination, start_date, end_date, current_location_city, exclude_user_id):
  # ``group`` keeps legacy API clients working; new clients opt in through
  # the explicit Connect People choice after selecting Single Travel.
  query={'destination.name': {'$regex': f'^{destination}$', '$options': 'i'}, 'input.start_date': start_date, 'input.end_date': end_date, '$or':[{'input.travel_type':'group'},{'input.connection_option':'connect_people'}], 'input.current_location_city': {'$regex': f'^{current_location_city}$', '$options': 'i'}, 'user_id': {'$ne': exclude_user_id}}
  if self.mongo is not None:
   try: return self._clean_many(self.mongo.itineraries.find(query, {'_id': 0}))
   except PyMongoError: return []
  return [x for x in self.itineraries.values() if x.get('user_id') != exclude_user_id and (x.get('input', {}).get('travel_type') == 'group' or x.get('input', {}).get('connection_option') == 'connect_people') and x.get('input', {}).get('current_location_city', '').casefold() == current_location_city.casefold() and x.get('input', {}).get('start_date') == start_date and x.get('input', {}).get('end_date') == end_date and x.get('destination', {}).get('name', '').casefold() == destination.casefold()]
 def all_matchable_trips(self, exclude_user_id=None, destination=None):
  query={'destination.name': {'$regex': f'^{destination}$', '$options': 'i'}} if destination else {}
  query['$or']=[{'input.travel_type':'group'},{'input.connection_option':'connect_people'}]
  if exclude_user_id: query['user_id']={'$ne': exclude_user_id}
  if self.mongo is not None:
   try: return self._clean_many(self.mongo.itineraries.find(query, {'_id': 0}))
   except PyMongoError: return []
  return [x for x in self.itineraries.values() if (not exclude_user_id or x.get('user_id') != exclude_user_id) and (x.get('input', {}).get('travel_type') == 'group' or x.get('input', {}).get('connection_option') == 'connect_people') and (not destination or x.get('destination', {}).get('name', '').casefold() == destination.casefold())]
 def save_connection(self, connection):
  if self.mongo is not None: self.mongo.connections.insert_one(connection.copy())
  else: self.connections[connection['id']]=connection
  return connection
 def connection(self, sender_id, receiver_id):
  if self.mongo is not None:
   try: return self._clean(self.mongo.connections.find_one({'sender_id': sender_id, 'receiver_id': receiver_id})) or self._clean(self.mongo.connections.find_one({'sender_id': receiver_id, 'receiver_id': sender_id}))
   except PyMongoError: return None
  return next((x for x in self.connections.values() if {x['sender_id'],x['receiver_id']}=={sender_id,receiver_id}),None)
 def connection_by_id(self, identifier):
  if self.mongo is not None:
   try: return self._clean(self.mongo.connections.find_one({'id': identifier}))
   except PyMongoError: return None
  return self.connections.get(identifier)
 def received_connections(self, user_id):
  if self.mongo is not None:
   try: return self._clean_many(self.mongo.connections.find({'receiver_id': user_id}).sort('created_at', -1))
   except PyMongoError: return []
  return sorted((x for x in self.connections.values() if x['receiver_id']==user_id),key=lambda x:x['created_at'],reverse=True)
 def update_connection(self, identifier, fields):
  if self.mongo is not None:
   self.mongo.connections.update_one({'id': identifier}, {'$set': fields}); return self.connection_by_id(identifier)
  if identifier in self.connections: self.connections[identifier].update(fields)
  return self.connections.get(identifier)
 def save_group(self, group):
  if self.mongo is not None: self.mongo.travel_groups.insert_one(group.copy())
  else: self.groups[group['id']]=group
  return group
 def groups_for_user(self, user_id):
  if self.mongo is not None:
   try: return self._clean_many(self.mongo.travel_groups.find({'member_ids': user_id}, {'_id': 0}))
   except PyMongoError: return []
  return [x for x in self.groups.values() if user_id in x['member_ids']]
 def group_by_id(self, identifier):
  if self.mongo is not None:
   try: return self._clean(self.mongo.travel_groups.find_one({'id': identifier}))
   except PyMongoError: return None
  return self.groups.get(identifier)
 def group_for_trip_with_member(self, trip_id, member_id):
  if self.mongo is not None:
   try: return self._clean(self.mongo.travel_groups.find_one({'trip_id': trip_id, 'member_ids': member_id}))
   except PyMongoError: return None
  return next((group for group in self.groups.values() if group['trip_id']==trip_id and member_id in group['member_ids']),None)
 def update_group(self, identifier, fields):
  if self.mongo is not None:
   self.mongo.travel_groups.update_one({'id': identifier}, {'$set': fields})
   return self.group_by_id(identifier)
  if identifier in self.groups: self.groups[identifier].update(fields)
  return self.groups.get(identifier)
 def delete_group(self, identifier):
  if self.mongo is not None:
   self.mongo.group_messages.delete_many({'group_id': identifier})
   return bool(self.mongo.travel_groups.delete_one({'id': identifier}).deleted_count)
  self.group_messages.pop(identifier, None)
  return self.groups.pop(identifier, None) is not None
 def save_group_message(self, message):
  if self.mongo is not None: self.mongo.group_messages.insert_one(message.copy())
  else: self.group_messages.setdefault(message['group_id'],[]).append(message)
  return message
 def group_messages_for(self, group_id):
  if self.mongo is not None:
   try: return self._clean_many(self.mongo.group_messages.find({'group_id': group_id}, {'_id': 0}).sort('created_at', 1))
   except PyMongoError: return []
  return self.group_messages.get(group_id,[])
store=Store()

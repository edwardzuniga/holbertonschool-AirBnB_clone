#!/usr/bin/python3


from models.place import Place
from tests.test_models.test_base_model import TestBaseModel


class TestPlace(TestBaseModel):
    '''
    =========================
    Place tests
    =========================
    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super().__init__(*args, **kwargs)
        self.test_class = Place
        self.test_name = "Place"

    def test_city_id(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.city_id, str)

    def test_user_id(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.user_id, str)
        
    def test_name(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.name, str)

    def test_description(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.description, str)
    
    def test_number_rooms(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.number_rooms, str)
    
    def test_number_bathrooms(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.number_bathrooms, str)
    
    def test_max_guest(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.max_guest, str)
    
    def test_price_by_night(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.price_by_night, str)
    
    def test_latitude(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.latitude, str)
    
    def test_longitude(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.longitude, str)
    
    def test_amenity_ids(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.amenity_ids, str)

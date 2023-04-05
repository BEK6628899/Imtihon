from Asosiy.serializers import *
from unittest import TestCase


class SuvSerializersTest(TestCase):
    def suv_test(self):
        suv = {"id":3,"brend":"Fanta","narx":9000,"litr":"1 litr","batafsil":"Gazlangan"}
        serializer = SuvSerializers(data=suv)
        assert serializer.is_valid() == True


# class MijozSerializersTest(TestCase):
#     def mijoz_test(self):
#         mijoz = {"id":4,""}
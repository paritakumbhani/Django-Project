from django.test import TestCase
from common.common import getData

""" Test To check If addNew view works properly"""
class UnitTest(TestCase):
    def test_addNew_in_dataBase(self):
        newData = {
            'id': 1,
            'CheeseId': '228',
            'CheeseNameEn': '',
            'ManufacturerNameEn': '',
            'ManufacturerProvCode': 'NB',
            'ManufacturingTypeEn': 'Farmstead',
            'WebSiteEn': '',
            'FatContentPercent': '24.2',
            'MoisturePercent': '47',
            'ParticularitiesEn': '',
            'FlavourEn': 'Sharp, lactic',
            'CharacteristicsEn': 'Uncooked',
            'RipeningEn': '9 Months',
            'Organic': '0',
            'CategoryTypeEn': 'Firm Cheese',
            'MilkTypeEn': 'Ewe',
            'MilkTreatmentTypeEn': 'Raw Milk',
            'RindTypeEn': 'Washed Rind',
            'LastUpdateDate': '2016-02-03'
        }
        response = self.client.post('/addnew',newData)
        self.assertEqual(response.context['dbData'][0],newData)
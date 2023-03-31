"""
Code > Programing Test
Authour> Hardik Gadher
Date> 06.04.2022
Location> Teltow, Potsdam
"""
import json

class Address:
    """
    Return> Working with different adress formats and their elements
    """

    def __init__(self,address):
        """
        :type address: String
        """
        self.address = address

    def Street(self):
        """
        :return: Street Name
        """

        #removing comma from the strinf is it is there
        AddressText = self.address.replace(',',' ')
        Characters = []
        for item in AddressText.split():
            if item.isalpha():
                Characters.append(item)
        return " ".join(Characters[:-1])

    def HouseNummer(self):
        """
        :return: House Number
        """
        global Housenummer
        AddressText = self.address.replace ( ',', ' ' )
        Characters = []
        Numbers = []
        for item in AddressText.split():
            if item.isalpha():
                Characters.append(item )
            else:
                Numbers.append(item)

        for number in Numbers:
            if len(number) == 5:
                Postcode = number
            else:
                Housenummer = number

        return Housenummer

    def Postcode(self):
        """
        :return: Postal Code
        """

        global Postcode
        AddressText = self.address.replace ( ',', ' ' )
        Characters = []
        Numbers = []
        for item in AddressText.split():
            if item.isalpha():
                Characters.append(item )
            else:
                Numbers.append(item)

        for number in Numbers:
            if len(number) == 5:
                Postcode = number
            else:
                Housenummer = number

        return Postcode

    def cityName(self):
        """
        :return: City name
        """
        AddressText = self.address.replace(',',' ')
        Characters = []
        for item in AddressText.split():
            if item.isalpha():
                Characters.append(item)
        return Characters[-1]

if __name__ == '__main__':

    AddressDict = {}

    AddressObject = Address("90 Vijazraj Rowhouse, Surat 39422")
    AddressDict['Street'] = AddressObject.Street()
    AddressDict['HouseNummer'] = AddressObject.HouseNummer()
    AddressDict['Postcode'] = AddressObject.Postcode()
    AddressDict['City'] = AddressObject.cityName()
    print(AddressDict)

    json_object = json.dumps (AddressDict, indent=4 )

    # Writing to output.json
    with open ( "Output.json", "w") as outfile:
        outfile.write (json_object)

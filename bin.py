#class definition of bin object and other related code
class Bin:
	__company = ""
	__address = ""
	__city = ""
	__postalCode = ""
	__longitude = ""
	__latitude = ""
	__name =""
	__type = ""

	def __init__(self, company, address, city, postalCode, longitude, latitude, name):
		self.company = company
		self.address = address
		self.city = city
		self.postalCode = postalCode
		self.longitude = longitude
		self.name = name
        
        def getCompany()
            return self.company

        def getAddress()
            return self.address

        def getCity()
            return self.city

        def getPostalCode()
            return self.postalcode

        def getLongitude()
            return self.longitude

        def getLatitude()
            return self.latitude

        def getName()
            return self.name

        def getType()
            return self.type

        def toString()
            return self.company + "is at" + self.address + ", " + self.city

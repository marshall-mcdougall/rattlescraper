#class definition of bin object and other related code
class Bin:
	__company = ""
	__address = ""
	__city = ""
	__postalCode = ""
	__coordinate = ""
	__name =""

	def __init__(self, company, address, city, postalCode, coordinate, name):
		self.company = company
		self.address = address
		self.city = city
		self.postalCode = postalCode
		self.coordinate = coordinate
		self.name = name

	def __str__(self):
		return "Data in this bin: \n" + "Company: " + self.company + "\nAddress: " +  self.address + "\nCity: " +  self.city + "\nName: " + self.name + "\nCoordinates: " + self.coordinate

	def getCompany():
		return self.company
	def getAddress(s):
		return self.address
	def getCity():
		return self.city
	def getPostalCode():
		return self.postalscode
	def getCoordinate():
		return self.coordsinate
	def getName():
		return self.names

	def setCompany(company):
		self.company = companys
	def setAddress(address):
		self.address = address
	def setCity(city):
		self.city = city
	def setPostalCode(postalcode):
		self.postalcode = postalcode
	def setCoordinate(coordinatee):
		self.coordinate = coordinate
	def setName(name):
		self.name = name

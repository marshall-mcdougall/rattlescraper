#class definition of bin object and other related code
class Bin:
	company = ""
	address = ""
	city = ""
	postalCode = ""
	coordinate = ""
	name =""

	def __init__(self, company, address, city, postalCode, coordinate, name):
		self.company = company
		self.address = address
		self.city = city
		self.postalCode = postalCode
		self.coordinate = coordinate
		self.name = name
	def __str__(self):
		return self.company + " is at " + self.address + ", " + self.city + " and its name is " + self.name + " and the coordinate is " + self.coordinate


	def getCompany():
		return self.company
	def getAddress():
		return self.address
	def getCity():
		return self.city
	def getPostalCode():
		return self.postalcode
	def getCoordinate():
		return self.coordinate
	def getName():
		return self.name
	def toString():
		return self.company + "is at" + self.address + ", " + self.city

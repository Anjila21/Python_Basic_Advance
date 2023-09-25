#constructor syntax: __init__()
#self : contains the memory refernce of the current object


class Country:
    def __init__(self,name,region,capital,literacy_rate):
        self.name =name
        self.region = region
        self.capital = capital
        self.literacy_rate = literacy_rate

    def country_info(self):
        print(f"{self.name} lies in {self.region}. Its capital is {self.capital} and literacy rate is{self.literacy_rate}")


con = Country('Nepal','Asia','Kathmandu',67)
con.country_info()

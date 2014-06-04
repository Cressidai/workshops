from __future__ import division


class CountryModified(object):
    #initialization
    def __init__(self, name, population, gdp, language=None):
        self.name = name
        self.population = population
        self.gdp = gdp
        self.language = language 
    def print_name(self):
        print "Name:", self.name

    def print_population(self):
        print "Population:", self.population

    def print_gdp(self):
        print "Gross domestic product:", self.gdp
    
    def print_language(self):
        if not self.language:
            print "Language not known"
        else:
            print "Official language", self.language


class Country(object):
    # class attributes
    country_num = 193
    population = 7237783400

    #initialization
    def __init__(self, name, population, gdp):
        self.name = name
        self.population = population
        self.gdp = gdp
    
    def print_name(self):
        print "Name:", self.name

    def print_population(self):
        print "Population:", self.population

    def print_gdp(self):
        print "Gross domestic product:", self.gdp


class EUCountry(CountryModified):
    # class attributes
    country_num = 28
    population = 504456000
    countries = set()

    #initialization
    def __init__(self, name, population, gdp, eurozone=False):
        self.countries.add(name)
        super(EUCountry, self).__init__(name, population, gdp)
        self.eurozone = eurozone

    def in_eurozone(self):
        print "In Eurozone:", self.eurozone

    # calculate percent of population out of total population
    def percent_population(self):
        return self.population/self.__class__.population

if __name__ == '__main__':
    obj1 = EUCountry("Portugal", 10609000, 23068, True)
    obj2 = Country("Montenegro", 620000, 11913)
    obj1.print_name()
    obj1.print_population()
    obj1.print_gdp()
    obj1.in_eurozone()
    obj1.print_language()
    print "=================================\n"

    obj2.print_name()
    obj2.print_population()
    obj2.print_gdp()

    try:
        obj2.in_eurozone()
    except Exception, e:
        print "%s is not an EU country" % (obj2.name)

    print "Countries:", EUCountry.countries 
    
    print "Percent of population:", obj1.percent_population()

############         Exercise      ####################

# 1. Add an attribute to EUCountry class that would contain all EU countries initialized

# 2. Add one more method to EUCountry

# 3. Create a new class for replacement of Country class and modify the subclassEUCountry so that it would inherit from this new class 




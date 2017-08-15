#Dataset source: MongoDB
#Python dictionary {'database':'dbName', 'collection':'collName'}
conn = {'database':'NjuskaloRealEstateAds', 'collection':'ApartmentForSaleCollection'}

#Target is the column that will be predicted
#Used by DatasetAnalyser to draw box and scatter graphs
target = u'priceInEuros'
#Values that represent null, None or 'Missing' in the dataset
#Used by DatasetAnalyser to change those into numpy.nan
nanValues = [0]
#Ignored columns don't have their occurences counted
#Used by DatasetAnalyser during value counting
dontCountColumns = [u'_id', u'adCode', u'adLink', u'adPublishedDate', u'objectCode']
#Binary columns have a yes or no, 1 or 0 value
binaryColumns = [u'hasCargoElevator', u'hasElevator', u'isNewlyBuilt']
#Columns that should be dropped from the dataset
#Used by DatasetAnalyser to mass eliminate columns from the dataset
dropColumns = [u'energyCertificate', u'hasCargoElevator', u'hasElevator', u'isNewlyBuilt', u'numberOfRooms', u'state',
               u'type', u'sizeOfBalcony', u'sizeOfGarden', u'sizeOfTerrace', u'yearOfConstruction',
			   u'yearOfLastAdaptation', u'_id', u'adCode', u'adLink', u'adPublishedDate', u'objectCode',
			   u'place', u'town']

#-.-.-.-.- #Columns are either categorical, numerical or for utility #-.-.-.-.-
#Categorical values have strings or similar category values
#Used by DatasetAnalyser to mass draw box graphs
categoricalColumns = [u'energyCertificate', u'floor',
                      u'hasCargoElevator', u'hasElevator', u'isNewlyBuilt', u'numberOfRooms',
					  u'place', u'state', u'town', u'type']
#Numerical values have floats, decimals or integers for values
#Used by DatasetAnalyser to mass draw distribution graphs
numericalColumns = [u'numberOfParkingSpaces', u'priceInEuros', u'size', u'sizeOfBalcony',
                    u'sizeOfGarden', u'sizeOfTerrace', u'yearOfConstruction', u'yearOfLastAdaptation']
#Utility columns have a very large number of unique values
utilityColumns = [u'_id', u'adCode', u'adLink', u'adPublishedDate', u'objectCode', u'sellerLink']
			  
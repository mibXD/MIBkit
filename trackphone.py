# Tracker main function
def Tracker():

        # Import
        import phonenumbers
        from phonenumbers import geocoder
        from opencage.geocoder import OpenCageGeocode

        # Set the key
        key = '86b3c36bfe4d4b1eab49c785386cfc8d'
        
        number = input('# Set the phone number: ')

        # Number location
        unumber = phonenumbers.parse(number)
        location = geocoder.description_for_number(unumber, 'en')

        # Number Coordinates
        gcoder = OpenCageGeocode(key)
        query = str(location)
        results = gcoder.geocode(query)

        # Get lat and lng
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']


        print(f'''State: {location}
Latitude & longitude: {lat, lng}''')

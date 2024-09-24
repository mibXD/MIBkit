def Tracker():


        import phonenumbers
        from phonenumbers import geocoder
        from opencage.geocoder import OpenCageGeocode


        key = '86b3c36bfe4d4b1eab49c785386cfc8d'
        number = input('# Set the phone number: ')


        unumber = phonenumbers.parse(number)
        location = geocoder.description_for_number(unumber, 'en')
        gcoder = OpenCageGeocode(key)
        query = str(location)
        results = gcoder.geocode(query)


        print(location, results)

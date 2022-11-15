from content import content


class Venue:
    def __init__(self):
        self.location: Location = None
        self.title: str = None
        self.address: str = None
        self.foursquare_id: str = None
        self.foursquare_type: str = None
        self.google_place_id: str = None
        self.google_place_type: str = None

    def set_data(self, context):
        self.location: Location = Location().set_data(context['location'])
        self.title: str = content(context, 'title')
        self.address: str = content(context, 'address')
        self.foursquare_id: str = content(context, 'foursquare_id')
        self.foursquare_type: str = content(context, 'foursquare_type')
        self.google_place_id: str = content(context, 'google_place_id')
        self.google_place_type: str = content(context, 'google_place_type')

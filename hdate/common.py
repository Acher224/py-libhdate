"""Small helper classes."""

import datetime
from collections import namedtuple

from dateutil import tz

HebrewDate = namedtuple("HebrewDate", ["year", "month", "day"])


class Location(object):
    """Define a geolocation for Zmanim calculations."""

    # pylint: disable=too-few-public-methods
    # pylint: disable=useless-object-inheritance

    def __init__(self, name="Jerusalem", latitude=31.778, longitude=35.235,
                 timezone="Asia/Jerusalem", altitude=754, diaspora=False):
        """Initialitze the location object."""
        self._timezone = None
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.altitude = altitude
        self.diaspora = diaspora

    def __repr__(self):
        """Return a representation of Location for programmatic use."""
        return ("Location(name='{}', latitude={}, longitude={}, timezone={}, "
                "altitude={}, diaspora={})".format(
            self.name, self.latitude, self.longitude, self.timezone,
            self.altitude, self.diaspora))

    def __eq__(self, other):
        """Override equality operator."""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        """Override inequality operator."""
        return not self.__eq__(other)

    @property
    def timezone(self):
        """Return the timezone."""
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        """Set the timezone."""
        self._timezone = (value if isinstance(value, datetime.tzinfo)
                          else tz.gettz(value))

"""
Jewish calendrical date and times for a given location.

HDate calculates and generates a represantation either in English or Hebrew
of the Jewish calendrical date and times for a given location
"""
from __future__ import division

import datetime
import math
from itertools import product

from dateutil import tz

import hdate.hdate_julian as hj
from hdate.hdate_string import get_hebrew_date
from hdate.hdate_string import get_zmanim_string
from hdate.htables import HOLIDAYS
from hdate.htables import JOIN_FLAGS


def set_date(date):
    """
    Check that the given date is valid.

    If no date is given set the date to today
    """
    if date is None:
        date = datetime.date.today()
    elif not isinstance(date, datetime.date):
        raise TypeError
    return date


class Zmanim(object):
    """Return Jewish day times."""

    def __init__(self, date=None, latitude=None, longitude=None,
                 timezone='', hebrew=True):
        """Initialize the Zmanim object."""
        if latitude is None or longitude is None:
            # Tel Aviv cordinates
            latitude = 32.08088
            longitude = 34.78057
        self.date = set_date(date)
        self.latitude = latitude
        self.longitude = longitude
        self._hebrew = hebrew
        if not timezone:
            timezone = 'UTC'
        self.timezone = timezone
        self.zmanim = self.get_zmanim()

    def utc_minute_timezone(self, minutes_from_utc):
        """Return the local time for a given time UTC."""
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz(self.timezone)
        utc = datetime.datetime(self.date.year, self.date.month,
                                self.date.day) + \
            datetime.timedelta(minutes=minutes_from_utc)
        utc = utc.replace(tzinfo=from_zone)
        local = utc.astimezone(to_zone)
        return local

    def get_zmanim(self):
        """Return a dictionary of the zmanim the object represents."""
        zmanim_dict = dict()
        zmanim_list = self.get_utc_sun_time_full()
        for zman in zmanim_list:
            zmanim_dict[zman] = self.utc_minute_timezone(zmanim_list[zman])
        return zmanim_dict

    def __repr__(self):
        """Return a representation of Zmanim for a given day and location."""
        return get_zmanim_string(
            self.zmanim, hebrew=self._hebrew).encode('utf-8')

    def gday_of_year(self):
        """Return the number of days since January 1 of the given year."""
        return (self.date - datetime.date(self.date.year, 1, 1)).days

    def _get_utc_sun_time_deg(self, deg):
        """
        Return the sunset and sunrise times in minutes from 00:00 (utc).

        This is done for a given sun altitude in sunrise `deg` degrees
        This function only works for altitudes sun really is.
        If the sun never gets to this altitude, the returned sunset and sunrise
        values will be negative. This can happen in low altitude when latitude
        is nearing the poles in winter times, the sun never goes very high in
        the sky there.
        """
        gama = 0        # location of sun in yearly cycle in radians
        eqtime = 0      # difference betwen sun noon and clock noon
        decl = 0        # sun declanation
        hour_angle = 0  # solar hour angle
        sunrise_angle = math.pi * deg / 180.0  # sun angle at sunrise/set

        # get the day of year
        day_of_year = self.gday_of_year()

        # get radians of sun orbit around earth =)
        gama = 2.0 * math.pi * ((day_of_year - 1) / 365.0)

        # get the diff betwen suns clock and wall clock in minutes
        eqtime = 229.18 * (0.000075 + 0.001868 * math.cos(gama) -
                           0.032077 * math.sin(gama) -
                           0.014615 * math.cos(2.0 * gama) -
                           0.040849 * math.sin(2.0 * gama))

        # calculate suns declanation at the equater in radians
        decl = (0.006918 - 0.399912 * math.cos(gama) +
                0.070257 * math.sin(gama) -
                0.006758 * math.cos(2.0 * gama) +
                0.000907 * math.sin(2.0 * gama) -
                0.002697 * math.cos(3.0 * gama) +
                0.00148 * math.sin(3.0 * gama))

        # we use radians, ratio is 2pi/360
        latitude = math.pi * self.latitude / 180.0

        # the sun real time diff from noon at sunset/rise in radians
        try:
            hour_angle = (math.acos(
                math.cos(sunrise_angle) /
                (math.cos(latitude) * math.cos(decl)) -
                math.tan(latitude) * math.tan(decl)))
        # check for too high altitudes and return negative values
        except ValueError:
            return -720, -720

        # we use minutes, ratio is 1440min/2pi
        hour_angle = 720.0 * hour_angle / math.pi

        # get sunset/rise times in utc wall clock in minutes from 00:00 time
        # sunrise / sunset
        return int(720.0 - 4.0 * self.longitude - hour_angle - eqtime), \
            int(720.0 - 4.0 * self.longitude + hour_angle - eqtime)

    def get_utc_sun_time_full(self):
        """Return a list of Jewish times for the given location."""
        # sunset and rise time
        sunrise, sunset = self._get_utc_sun_time_deg(90.833)

        # shaa zmanit by gara, 1/12 of light time
        sun_hour = (sunset - sunrise) // 12
        midday = (sunset + sunrise) // 2

        # get times of the different sun angles
        first_light, _n = self._get_utc_sun_time_deg(106.1)
        talit, _n = self._get_utc_sun_time_deg(101.0)
        _n, first_stars = self._get_utc_sun_time_deg(96.0)
        _n, three_stars = self._get_utc_sun_time_deg(98.5)
        mga_sunhour = (midday - first_light) / 6

        res = dict(sunrise=sunrise, sunset=sunset, sun_hour=sun_hour,
                   midday=midday, first_light=first_light, talit=talit,
                   first_stars=first_stars, three_stars=three_stars,
                   plag_mincha=sunset - 1.25 * sun_hour,
                   stars_out=sunset + 18. * sun_hour / 60.,
                   small_mincha=sunrise + 9.5 * sun_hour,
                   big_mincha=sunrise + 6.5 * sun_hour,
                   mga_end_shma=first_light + mga_sunhour * 3.,
                   gra_end_shma=sunrise + sun_hour * 3.,
                   mga_end_tfila=first_light + mga_sunhour * 4.,
                   gra_end_tfila=sunrise + sun_hour * 4.,
                   midnight=midday + 12 * 60.)
        return res


class HDate(object):
    """
    Hebrew date class.

    Supports converting from Gregorian and Julian to Hebrew date.
    """

    def __init__(self, date=None, diaspora=False, hebrew=True):
        """Initialize the HDate object."""
        self.gdate = set_date(date)
        self._hebrew = hebrew
        self._diaspora = diaspora
        self.jdn = hj.gdate_to_jdn(self.gdate.day, self.gdate.month,
                                   self.gdate.year)
        (self.h_day, self.h_month, self.h_year) = hj.jdn_to_hdate(self.jdn)
        self._weekday = (self.jdn + 1) % 7 + 1
        self.h_size_of_year = hj.get_size_of_hebrew_year(self.h_year)
        jdn_tishrey1 = hj.hdate_to_jdn(1, 1, self.h_year)
        self.h_new_year_weekday = (jdn_tishrey1 + 1) % 7 + 1
        self.h_year_type = hj.get_year_type(self.h_size_of_year,
                                            self.h_new_year_weekday)
        h_days = self.jdn - jdn_tishrey1
        self.h_weeks = (h_days + self.h_new_year_weekday - 1) // 7 + 1

    def __repr__(self):
        """Return the Hebrew date as a string."""
        return self.to_string(hebrew=self._hebrew).encode("utf-8")

    def to_string(self, short=False, hebrew=True):
        """Return the hebrew date as a string object."""
        return get_hebrew_date(self.h_day, self.h_month, self.h_year,
                               self.get_omer_day(), self._weekday,
                               self.get_holyday(), hebrew=hebrew, short=short)

    def hdate_set_hdate(self, day, month, year):
        """Set the dates of the HDate object based on a given Hebrew date."""
        # sanity check
        if not 0 < month < 15:
            raise ValueError('month ({}) legal values are 1-14'.format(month))
        if not 0 < day < 31:
            raise ValueError('day ({}) legal values are 1-31'.format(day))

        jdn = hj.hdate_to_jdn(day, month, year)
        self.hdate_set_jdn(jdn)

    def hdate_set_jdn(self, jdn):
        """Set the date of the HDate object based on Julian date."""
        gday, gmonth, gyear = hj.jdn_togdate(jdn)
        gdate = datetime.date(gyear, gmonth, gday)
        self.__init__(gdate, self._diaspora, self._hebrew)

    def get_hebrew_date(self):
        """Return the hebrew date in the form of day, month year."""
        return self.h_day, self.h_month, self.h_year

    def get_holyday(self):
        """Return the number of holyday."""
        # Get the possible list of holydays for this day
        holydays_list = [
            holyday for holyday in HOLIDAYS if
            (self.h_day, self.h_month) in product(
                *([x] if isinstance(x, int) else x for x in holyday.date))]

        # Filter any non-related holydays depending on Israel/Diaspora only
        holydays_list = [
            holyday for holyday in holydays_list if
            (holyday.israel_diaspora == "") or
            (holyday.israel_diaspora == "ISRAEL" and not self._diaspora) or
            (holyday.israel_diaspora == "DIASPORA" and self._diaspora)]

        # Filter any special cases defined by True/False functions
        holydays_list = [
            holyday for holyday in holydays_list if
            all(func(self) for func in holyday.date_functions_list)]

        assert len(holydays_list) <= 1

        # If anything is left return it, otherwise return 0
        return holydays_list[0].index if holydays_list else 0

    def short_kislev(self):
        """Return whether this year has a short Kislev or not."""
        return True if self.h_size_of_year in [353, 383] else False

    def get_omer_day(self):
        """Return the day of the Omer."""
        omer_day = self.jdn - hj.hdate_to_jdn(16, 7, self.h_year) + 1
        if not 0 < omer_day < 50:
            return 0
        return omer_day

    def get_reading(self, diaspora):
        """
        Return number of hebrew parasha.

        55..61 are joined readings e.g. Vayakhel Pekudei
        """
        # if simhat tora return vezot habracha
        if self.h_month == 1:
            # simhat tora is a day after shmini atzeret outsite israel
            if self.h_day == 22 and not diaspora:
                return 54
            if self.h_day == 23 and diaspora:
                return 54

        # if not shabat return none
        if self._weekday != 7:
            return 0

        if self.h_weeks == 1:
            if self.h_new_year_weekday == 7:
                # Rosh hashana
                return 0
            elif ((self.h_new_year_weekday == 2) or
                  (self.h_new_year_weekday == 3)):
                return 52
            # if (self.h_new_year_weekday == 5)
            return 53
        elif self.h_weeks == 2:
            if self.h_new_year_weekday == 5:
                # Yom kippur
                return 0
            return 53
        elif self.h_weeks == 3:
            # Succot
            return 0
        elif self.h_weeks == 4:
            if self.h_new_year_weekday == 7:
                # Not simhat tora in diaspora
                return 0
            return 1
        else:
            # simhat tora on week 4 bereshit too
            reading = self.h_weeks - 3

            # was simhat tora on shabat ?
            if self.h_new_year_weekday == 7:
                reading = reading - 1

            # no joining
            if reading < 22:
                return reading

            # pesach
            if (self.h_month == 7) and (self.h_day > 14):
                # Shmini of pesach in diaspora is on the 22 of the month*/
                if diaspora and (self.h_day <= 22):
                    return 0
                if not diaspora and (self.h_day < 22):
                    return 0

            # Pesach always removes one
            if (((self.h_month == 7) and (self.h_day > 21)) or
                    (self.h_month > 7 and self.h_month < 13)):
                reading -= 1

                # on diaspora, shmini of pesach may fall on shabat if
                # next new year is on shabat
                if (diaspora and (((self.h_new_year_weekday +
                                    self.h_size_of_year) % 7) == 2)):
                    reading -= 1

            # on diaspora, shavuot may fall on shabat if next new year is on
            # shabat
            if (diaspora and
                    (self.h_month < 13) and
                    ((self.h_month > 9) or
                     (self.h_month == 9 and self.h_day >= 7)) and
                    ((self.h_new_year_weekday + self.h_size_of_year)
                     % 7) == 0):
                if self.h_month == 9 and self.h_day == 7:
                    return 0
                else:
                    reading -= 1

            # joining
            if (JOIN_FLAGS[diaspora][self.h_year_type - 1][0] and
                    (reading >= 22)):
                if reading == 22:
                    return 55
                else:
                    reading += 1
            if (JOIN_FLAGS[diaspora][self.h_year_type - 1][1] and
                    (reading >= 27)):
                if reading == 27:
                    return 56
                else:
                    reading += 1
            if (JOIN_FLAGS[diaspora][self.h_year_type - 1][2] and
                    (reading >= 29)):
                if reading == 29:
                    return 57
                else:
                    reading += 1
            if (JOIN_FLAGS[diaspora][self.h_year_type - 1][3] and
                    (reading >= 32)):
                if reading == 32:
                    return 58
                else:
                    reading += 1

            if (JOIN_FLAGS[diaspora][self.h_year_type - 1][4] and
                    (reading >= 39)):
                if reading == 39:
                    return 59
                else:
                    reading += 1
            if (JOIN_FLAGS[diaspora][self.h_year_type - 1][5] and
                    (reading >= 42)):
                if reading == 42:
                    return 60
                else:
                    reading += 1
            if (JOIN_FLAGS[diaspora][self.h_year_type - 1][6] and
                    (reading == 51)):
                return 61
        return reading


def get_holyday_type(holyday):
    """Return a number describing the type of the holy day."""
    try:
        holyday_type = next((x.type for x in HOLIDAYS if x.index == holyday))
    except StopIteration:
        holyday_type = 0
    return holyday_type

class BaseReservationException(Exception):
    """This class is Base Class for handling Reservation Model Exceptions"""


class CapacityException(BaseReservationException):
    """This Exception is raised when demanded capacity is outnumbered real capacity of room"""


class RoomOccupiedException(BaseReservationException):
    """This Exception is raised when demanded room is occupied"""


class InvalidDate(BaseReservationException):
    """This Exceprion is raised when Datetime format is wrong"""
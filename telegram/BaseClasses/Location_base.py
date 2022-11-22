from dataclasses import dataclass
import typing


@dataclass
class BaseLocation:
    """Base Location Class"""
    longitude: typing.Union[float, None]
    latitude: typing.Union[float, None]
    horizontal_accuracy: typing.Union[None, float]
    live_period: typing.Union[None, int]
    heading: typing.Union[None, int]
    proximity_alert_radius: typing.Union[None, int]

from dataclasses import dataclass


@dataclass
class Purchase:
    street: str
    city: str
    zip: str
    state: str
    beds: int
    baths: int
    sqft: int
    type: str
    sale_date: str
    price: float
    latitude: float
    longitude: float

    @staticmethod
    def create_from_dict(lookup: dict):
        return Purchase(
            lookup["street"],
            lookup["city"],
            lookup["zip"],
            lookup["state"],
            int(lookup["beds"]),
            int(lookup["baths"]),
            int(lookup["sqft"]),
            lookup["type"],
            lookup["sale_date"],
            float(lookup["price"]),
            float(lookup["latitude"]),
            float(lookup["longitude"]),
        )

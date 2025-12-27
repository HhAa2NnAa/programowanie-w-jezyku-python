import requests
from typing import Optional
from dataclasses import dataclass
import argparse


@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    longitude: Optional[str]
    latitude: Optional[str]
    phone: Optional[str]
    website_url: Optional[str]
    updated_at: Optional[str]
    tag_list: Optional[list]

    def __str__(self):
        info = f"Browar: {self.name}\n"
        info += f"Id: {self.id}\n"
        info += f"Typ: {self.brewery_type}\n"
        if self.street:
            info += f"Ulica: {self.street}\n"
        if self.city:
            info += f"Miasto: {self.city}"
        if self.state:
            info += f", {self.state}"
        if self.postal_code:
            info += f" {self.postal_code}"
        info += "\n"
        if self.country:
            info += f"Państwo: {self.country}\n"
        if self.phone:
            info += f"Telefon: {self.phone}\n"
        if self.website_url:
            info += f"Strona: {self.website_url}\n"
        if self.latitude and self.longitude:
            info += f"Położenie: {self.latitude}, {self.longitude}\n"
        return info.strip()


def main():
    parser = argparse.ArgumentParser(description='Pobieranie browarów z Open Brewery DB API')
    parser.add_argument('--city', type=str)

    args = parser.parse_args()

    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {
        'per_page': 20,
        'page': 1
    }
    params['by_city'] = args.city
    response = requests.get(url, params=params)
    response.raise_for_status()
    breweries_data = response.json()

    breweries_list = []
    for data in breweries_data:
        brewery = Brewery(
            id=data.get('id', ''),
            name=data.get('name', ''),
            brewery_type=data.get('brewery_type', ''),
            street=data.get('street'),
            city=data.get('city'),
            state=data.get('state'),
            postal_code=data.get('postal_code'),
            country=data.get('country'),
            longitude=data.get('longitude'),
            latitude=data.get('latitude'),
            phone=data.get('phone'),
            website_url=data.get('website_url'),
            updated_at=data.get('updated_at'),
            tag_list=data.get('tag_list')
        )
        breweries_list.append(brewery)

    for i, brewery in enumerate(breweries_list, 1):
        print(f"\n{i}. {brewery}")


if __name__ == "__main__":
    main()
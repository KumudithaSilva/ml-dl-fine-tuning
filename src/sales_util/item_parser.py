from typing import Dict
from sales_util.items import Item

MAX_TEXT_EACH = 500


def summary_formate(short_description) -> str:
    # 'short_description': Value(dtype='string', id=None),
    return (
        str(short_description)
        .replace("\n", " ")
        .replace("\r", "")
        .replace("\t", "")
        .replace("  ", " ")
        .strip()[:MAX_TEXT_EACH]
    )

def date_formater(releaseDate) -> Dict:
    # releaseDate = game['release_date']  # Release date (string)
    # 'release_date': Value(dtype='string', id=None)
    pass

def cal_estimated_owners(estimatedOwners) -> int:
    # estimatedOwners = game['estimated_owners'] # Estimated owners (string, e.g.: "0 - 20000")
    # estimated_owners': Value(dtype='string', id=None)
    pass

def cal_supported_languages(supported_languages) -> int:
    # 'supported_languages': [Value(dtype='string', id=None)]
    pass

def cal_num_developers(developers) -> int:
    #  'developers': [Value(dtype='string', id=None)],
    pass

def cal_num_publishers(publishers) -> int:
    # 'publishers': [Value(dtype='string', id=None)],
    pass

def cal_num_categories(categories) -> int:
    # 'categories': [Value(dtype='string', id=None)],
    pass

def cal_num_genres(genres) -> int:
    # 'genres': [Value(dtype='string', id=None)],
    pass


def parse(datapoint):
    """
    Convert a raw datapoint dict into an Item object.
    """
    try:
        return Item(
            name=str(datapoint["name"]),
            peakCCU=int(datapoint["peak_ccu"]),
            required_age=int(datapoint["required_age"]),
            price=float(datapoint["price"]),
            dlcCount=int(datapoint["dlc_count"]),
            supportWindows=bool(datapoint["windows"]),
            supportMac=bool(datapoint["mac"]),
            supportLinux=bool(datapoint["linux"]),
            positive=int(datapoint["positive"]),
            negative=int(datapoint["negative"]),
            achievements=int(datapoint["achievements"]),

            # Optional fields
            recommendations = int(datapoint["recommendations"]) if datapoint.get("recommendations") is not None else None,
            release_year=int(datapoint["release_year"]) if datapoint.get("release_year") is not None else None,
            release_month=int(datapoint["release_month"]) if datapoint.get("release_month") is not None else None,
            release_day=int(datapoint["release_day"]) if datapoint.get("release_day") is not None else None,
            small_description=datapoint.get("small_description"),
            estimatedOwners=int(datapoint["estimatedOwners"]) if datapoint.get("estimatedOwners") is not None else None,
            supported_languages=int(datapoint["supported_languages"]) if datapoint.get("supported_language") is not None else None,
            num_developers=int(datapoint["num_developers"]) if datapoint.get("num_developers") is not None else None,
            num_publishers=int(datapoint["num_publishers"]) if datapoint.get("num_publishers") is not None else None,
            num_categories=int(datapoint["num_categories"]) if datapoint.get("num_categories")is not None else None,
            num_genres=int(datapoint["num_genres"]) if datapoint.get("num_genres") is not None else None,
        )
    except (KeyError, ValueError, TypeError) as e:
        print(f"Parse error: {e}")
        return None
from typing import Dict
from sales_util.items import Item

MAX_TEXT_EACH = 500


def summary_formate(short_description) -> str:
    return (
        str(short_description)
        .replace("\n", " ")
        .replace("\r", "")
        .replace("\t", "")
        .replace("  ", " ")
        .strip()[:MAX_TEXT_EACH]
    )

def date_formater(releaseDate) -> Dict:
    
    month_day, year = releaseDate.split(", ")
    month_str, day = month_day.split(" ")

    months = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
        "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }
    
    release_details = {
        'day': int(day),
        'month': months.get(month_str),
        "year": int(year)
    }

    return release_details
    

def cal_estimated_owners(estimatedOwners) -> int:
    min_owners, max_owners = estimatedOwners.split("-")
    owners = {
        "min": min_owners,
        "max": max_owners
    }

    return owners

def cal_supported_languages(supported_languages) -> int:
    count_supported_languages = len(supported_languages)
    return count_supported_languages

def cal_num_developers(developers) -> int:
    count_developers = len(developers)
    return count_developers

def cal_num_publishers(publishers) -> int:
    count_publishers = len(publishers)
    return count_publishers

def cal_num_categories(categories) -> int:
    count_categories = len(categories)
    return count_categories

def cal_num_genres(genres) -> int:
    count_genres = len(genres)
    return count_genres


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
            release_year= date_formater(datapoint.get("release_date")).get("year") if datapoint.get("release_date") is not None else None,
            release_month= date_formater(datapoint.get("release_date")).get("month") if datapoint.get("release_date") is not None else None,
            release_day= date_formater(datapoint.get("release_date")).get("day") if datapoint.get("release_date") is not None else None,
            small_description= summary_formate(datapoint.get("short_description")) if datapoint.get("short_description") is not None else None,
            min_estimatedOwners= cal_estimated_owners(datapoint.get("estimated_owners")).get("min") if datapoint.get("estimated_owners") is not None else None,
            max_estimatedOwners=cal_estimated_owners(datapoint.get("estimated_owners")).get("max") if datapoint.get("estimated_owners") is not None else None,
            supported_languages= cal_supported_languages(datapoint["supported_languages"]) if datapoint.get("supported_languages") is not None else None,
            num_developers= cal_num_developers(datapoint["developers"]) if datapoint.get("developers") is not None else None,
            num_publishers= cal_num_publishers(datapoint["publishers"]) if datapoint.get("publishers") is not None else None,
            num_categories= cal_num_categories(datapoint['categories']) if datapoint.get("categories")is not None else None,
            num_genres= cal_num_genres(datapoint['genres']) if datapoint.get("genres") is not None else None,
        )
    except (KeyError, ValueError, TypeError) as e:
        print(f"Parse error: {e}")
        return None
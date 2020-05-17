import json
import pprint
import requests
import geojson


def raw_json_to_pretty_json(raw_json, file_type=None):
    if file_type == "geojson":
        return geojson.dumps(raw_json, indent=4, sort_keys=True, ensure_ascii=False)
    else:
        return json.dumps(raw_json, indent=4, sort_keys=True, ensure_ascii=False)


def rest_request(request_url, method, params=None):
    return requests.request(method=method, url=request_url, params=params).text


if __name__ == "__main__":
    NON_STANDARD_PARAMS = {
        "f": "json",
        "where": "datetime<'2019-06-26 17:49:42'",
        "resultRecordCount": 5,
    }  # Non Standard Date query
    STANDARD_PARAMS = {
        "f": "json",
        "where": "Field<timestamp '2019-06-27 20:06:24'",
        "resultRecordCount": 5,
    }  # Standard Date query

    NON_STANDARD_DATE_QUERY_URL = ""
    STANDARD_DATE_QUERY_URL = ""
    response = rest_request(
        STANDARD_DATE_QUERY_URL, method="GET", params=STANDARD_PARAMS
    )
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(response)

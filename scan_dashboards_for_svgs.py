from other.my_secrets import get_regression_devext_dbqa_gis

REGRESSION_GIS = get_regression_devext_dbqa_gis()


items = REGRESSION_GIS.content.search(
    f"type:Dashboard", max_items=100000, outside_org=True
)

for item in items:
    try:
        str_dashboard_json = str(item.get_data())
        if "animate" in str_dashboard_json:
            print(item.id)

    except RuntimeError:
        continue

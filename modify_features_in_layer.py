import random
import time
from other.my_secrets import get_regression_devext_dbqa_gis, AGOL_ITEM_DICT

REGRESSION_GIS = get_regression_devext_dbqa_gis()


def modify_feature_layer(feature_layer):
    feature_set = feature_layer.query()

    toronto_police_dictionary = {
        "Status": ["Available", "Active"],
        "LastReportedOn": int,
        "Speed": int,
        "GasLevel": int,
        "x": int,
        "y": int,
    }
    new_features = []
    for _ in feature_set.features:
        feature = random.choice(feature_set.features)

        feature.attributes["Status"] = random.choice(
            toronto_police_dictionary["Status"]
        )
        feature.attributes["LastReportedOn"] = time.time() * 1000
        feature.attributes["Speed"] = random.randint(0, 100)
        feature.attributes["GasLevel"] = random.randint(0, 100)
        feature.geometry["x"] += random.uniform(-0.01, 0.01)
        feature.geometry["y"] += random.uniform(-0.01, 0.01)
        new_features.append(feature)

    feature_set._features = new_features
    # feature_layer.edit_features(updates=feature_set)

    # feature_collection = features.FeatureCollection.from_featureset(feature_set)
    # feature_layer.append(edits=str(feature_collection._lyr_json))


if __name__ == "__main__":
    LAYER_ITEM_ID = AGOL_ITEM_DICT["DEVEXT_FEATURE_LAYER_ITEM"]
    LAYER = REGRESSION_GIS.content.get(LAYER_ITEM_ID)
    while True:
        try:
            START_TIME = time.time()
            modify_feature_layer(LAYER)
            time.sleep(2)
            print(f"I took {time.time() - START_TIME} seconds to complete")
        except RuntimeError:
            pass

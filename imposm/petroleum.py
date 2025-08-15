from funcs import table, type_col, str_col

table(
    "marker",
    {"pipeline": ["marker"], "power": ["marker"], "marker": ["__any__"]},
    "point",
    columns=[type_col],
)

table(
    "pipeline",
    {"man_made": ["pipeline"], "construction:man_made": ["pipeline"]},
    "linestring",
    columns=[
        str_col("substance"),
        str_col("type"),
        str_col("construction:man_made", "construction"),
    ],
)

table(
    "petroleum_site",
    {
        "industrial": [
            "oil",
            "fracking",
            "oil_storage",
            "petroleum_terminal",
            "hydrocarbons",
            "oil sands",
            "oil_sands",
            "gas",
            "gas_storage",
            "natural_gas",
            "wellsite",
            "well_cluster",
            "refinery",
        ],
    },
    "polygon",
    columns=[type_col, str_col("name")],
)

table(
    "petroleum_substation",
    {
        "pipeline": ["substation"],
    }
    ["points", "polygon"],
    columns=[type_col, str_col("substance"), str_col("substation")],
)

table(
    "pipeline_feature",
    {"pipeline": ["valve", "flare"]},
    "point",
    columns=[type_col, str_col("diameter")],
)

table(
    "petroleum_well",
    {"man_made": ["petroleum_well", "oil_well"]},
    "point",
    columns=[type_col],
)

table(
    "offshore_platform",
    {"man_made": ["offshore_platform"]},
    ["points", "polygons"],
)

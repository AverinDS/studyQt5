class ComponentsConst:
    TREND = "TREND"
    RANDOM = "RANDOM"
    SEASONS = "SEASONS"


class AnomalyConst:
    SINGLE = "SINGLE"
    GROUP = "GROUP"
    AVOID = "AVOID"
    MIN_GROUP_SIZE=2


class GeneratorSetting:
    COUNT_OF_MODELS = 10
    MAX_TIME = 800  # can be changed by user
    MAX_VALUE = 100


class TermSetting:
    FILENAME = "TERMS.csv"
    SEPARATOR = "|"
    COUNT_OF_TERMS = 5  # can be changed by user

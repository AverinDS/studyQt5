class ComponentsConst:
    TREND = "TREND"
    RANDOM = "RANDOM"
    SEASONS = "SEASONS"


class AnomalyConst:
    SINGLE = "SINGLE"
    GROUP = "GROUP"
    AVOID = "AVOID"
    MIN_GROUP_SIZE = 2


class GeneratorSetting:
    COUNT_OF_MODELS = 10
    MAX_TIME = 800  # can be changed by user
    MAX_VALUE = 500


class TermSetting:
    FOLDERNAME = 'TERMS'
    FILENAME = "TERMS.csv"
    SEPARATOR = "|"
    COUNT_OF_TERMS = 5  # can be changed by user
    MARGIN = -20
    ROUND_TO = 3


class TranslatingConst:
    NUMBER_SOFT_MATRIX = "NUMBER_SOFT_MATRIX"
    NUMBER_SOFT_VECTOR = "NUMBER_SOFT_VECTOR"
    NUMBER_LINGUISTIC = "NUMBER_SOFT_LINGUISTIC"
    NUMBER_LINGUISTIC_SOFT = "NUMBER_LINGUISTIC_SOFT"
    NUMBER_NUMBER = "NUMBER_NUMBER"

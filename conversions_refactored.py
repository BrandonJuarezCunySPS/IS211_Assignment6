class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    conversions = {
        "Celsius": {
            "Kelvin": value + 273.15,
            "Fahrenheit": (value * 9/5) + 32,
        },
        "Fahrenheit": {
            "Celsius": (value - 32) * 5/9,
            "Kelvin": (value - 32) * 5/9 + 273.15,
        },
        "Kelvin": {
            "Celsius": value - 273.15,
            "Fahrenheit": (value - 273.15) * 9/5 + 32,
        },
        "Meters": {
            "Yards": value * 1.09361,
            "Miles": value / 1609.34,
        },
        "Yards": {
            "Meters": value / 1.09361,
            "Miles": value / 1760,
        },
        "Miles": {
            "Meters": value * 1609.34,
            "Yards": value * 1760,
        }
    }

    if fromUnit == toUnit:
        return value

    try:
        return conversions[fromUnit][toUnit]
    except KeyError:
        raise ConversionNotPossible("Conversion from {} to {} is not possible.".format(fromUnit, toUnit))
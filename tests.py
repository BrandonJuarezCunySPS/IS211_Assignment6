import unittest
from conversions import (convertCelsiusToKelvin, convertCelsiusToFahrenheit, convertFahrenheitToCelsius, convertFahrenheitToKelvin,
convertKelvinToCelsius, convertKelvinToFahrenheit)
from conversions_refactored import convert, ConversionNotPossible  # Import the new function

class TestTemperatureConversions(unittest.TestCase):
    # ... (your existing test methods)

    def test_convert_with_refactored(self):
        # Add tests for temperature conversions
        temperature_cases = [
            ("Celsius", "Kelvin", 0.0, 273.15),
            ("Celsius", "Fahrenheit", 0.0, 32.0),
            ("Fahrenheit", "Celsius", 32.0, 0.0),
            ("Kelvin", "Celsius", 273.15, 0.0),
            ("Kelvin", "Fahrenheit", 273.15, 32.0),
        ]
        for fromUnit, toUnit, value, expected in temperature_cases:
            result = convert(fromUnit, toUnit, value)
            print(f"Testing convert({fromUnit}, {toUnit}, {value}): Expected {expected}, got {result}")
            self.assertAlmostEqual(result, expected)

        # Check for conversion from one unit to itself
        for unit in ["Celsius", "Fahrenheit", "Kelvin"]:
            self.assertEqual(convert(unit, unit, 100), 100)

        # Check for raising exception on invalid conversion
        with self.assertRaises(ConversionNotPossible):
            convert("Celsius", "Miles", 100)

if __name__ == "__main__":
    unittest.main()

class TestTemperatureConversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        test_cases = [
            (0, 273.15),
            (100, 373.15),
            (25, 298.15),
            (-273.15, 0),
            (300, 573.15)
        ]

        for celsius, expected_kelvin in test_cases:
            result = convertCelsiusToKelvin(celsius)
            print(f"Testing convertCelsiusToKelvin({celsius}) = {result}, expected = {expected_kelvin}")
            self.assertAlmostEqual(result, expected_kelvin, places=2)

    def test_convertCelsiusToFahrenheit(self):
        test_cases = [
            (0, 32),
            (100, 212),
            (25, 77),
            (-40, -40),
            (300, 572)
        ]

        for celsius, expected_fahrenheit in test_cases:
            result = convertCelsiusToFahrenheit(celsius)
            print(f"Testing convertCelsiusToFahrenheit({celsius}) = {result}, expected = {expected_fahrenheit}")
            self.assertAlmostEqual(result, expected_fahrenheit, places=2)

    def test_convertFahrenheitToCelsius(self):
        test_cases = [
            (32, 0),
            (212, 100),
            (-40, -40),
            (77, 25),
            (572, 300),
        ]

        for fahrenheit, expected_celsius in test_cases:
            result = convertFahrenheitToCelsius(fahrenheit)
            print(f'Testing convertFahrenheitToCelsius: {fahrenheit}°F => {result}°C (Expected: {expected_celsius}°C)')
            self.assertAlmostEqual(result, expected_celsius, places=2)

    def test_convertFahrenheitToKelvin(self):
        test_cases = [
            (32, 273.15),
            (212, 373.15),
            (-40, 233.15),
            (77, 298.15),
            (572, 573.15),
        ]

        for fahrenheit, expected_kelvin in test_cases:
            result = convertFahrenheitToKelvin(fahrenheit)
            print(f'Testing convertFahrenheitToKelvin: {fahrenheit}°F => {result}K (Expected: {expected_kelvin}K)')
            self.assertAlmostEqual(result, expected_kelvin, places=2)

    def test_convertKelvinToCelsius(self):
        test_cases = [
            (273.15, 0),
            (373.15, 100),
            (0, -273.15),
            (298.15, 25),
            (573.15, 300),
        ]

        for kelvin, expected_celsius in test_cases:
            result = convertKelvinToCelsius(kelvin)
            print(f'Testing convertKelvinToCelsius: {kelvin}K => {result}°C (Expected: {expected_celsius}°C)')
            self.assertAlmostEqual(result, expected_celsius, places=2)

    def test_convertKelvinToFahrenheit(self):
        test_cases = [
            (273.15, 32),
            (373.15, 212),
            (0, -459.67),
            (298.15, 77),
            (573.15, 572),
        ]

        for kelvin, expected_fahrenheit in test_cases:
            result = convertKelvinToFahrenheit(kelvin)
            print(f'Testing convertKelvinToFahrenheit: {kelvin}K => {result}°F (Expected: {expected_fahrenheit}°F)')
            self.assertAlmostEqual(result, expected_fahrenheit, places=2)


if __name__ == "__main__":
    unittest.main()

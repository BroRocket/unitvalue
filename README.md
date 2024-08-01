# Unit/Dimensioned Quantities Module

## Overview

The Unit Converter Module is a Python library designed to handle various unit conversions. It allows for the creation of `UnitValue` objects, which can represent values with different units and convert between them.

## Features

- Create `UnitValue` objects with specified units and values.
- Convert between different units within the same dimension (e.g., meters to kilometers).
- Support for different measurement systems (e.g., metric and imperial).
- Arithmetic operations with unit handling (addition, subtraction, multiplication, division).
- Error handling for unsupported units and invalid operations.

## Installation

To be done

## Usage

### Creating a UnitValue

To create a `UnitValue` object, use the `create_dimensioned_quantity` function:

```python
from units import create_dimensioned_quantity

# Create a UnitValue object with a specified unit and value
distance = create_dimensioned_quantity('meter', 100)
```

### Converting Units

You can convert the unit of a `UnitValue` object using the `convert` method:

```python
# Convert the distance to kilometers
distance.convert(unit='kilometer')
print(distance)  # Output: 0.1 kilometer
```

### Arithmetic Operations

`UnitValue` objects support arithmetic operations, maintaining unit consistency:

```python
from units import create_dimensioned_quantity

length1 = create_dimensioned_quantity('meter', 50)
length2 = create_dimensioned_quantity('meter', 30)

# Addition
total_length = length1 + length2
print(total_length)  # Output: 80 meter

# Subtraction
remaining_length = length1 - length2
print(remaining_length)  # Output: 20 meter

# Multiplication by a scalar
double_length = length1 * 2
print(double_length)  # Output: 100 meter

# Division by a scalar
half_length = length1 / 2
print(half_length)  # Output: 25 meter
```

### Accessing Unit Information

You can access the unit, measurement type, and system of a `UnitValue` object using properties:

```python
print(distance.get_unit)  # Output: 'kilometer'
print(distance.get_measurement_type)  # Output: 'LENGTH'
print(distance.get_system)  # Output: 'METRIC'
```

## Error Handling

The module includes error handling for unsupported units and invalid operations:

```python
try:
    invalid_distance = create_dimensioned_quantity('unknown_unit', 100)
except Exception as e:
    print(e)  # Output: Invalid unit unknown_unit: this unit is not currently supported by the module
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue on the GitHub repository.

## License

This project is licensed under the MIT License.

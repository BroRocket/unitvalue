from ..src.unitvalue import *

# Examples of use
if __name__ == "__main__":
    d = UnitValue("METRIC", "DISTANCE", "m", 5) # this and the line belwo are equivalent, just the top one requires more manual knowledge of path to unit
    d1 = create_dimensioned_quantity("m", 5)
    d2 = create_dimensioned_quantity("cm", 200)
    d3 = create_dimensioned_quantity("ft", 10)
    new = d1*d3*d2
    print(new)
    m1 = create_dimensioned_quantity("g", 1000)
    rho = m1 / new
    print(m1 / new)
    print(rho * d1**3)
    temp = d1**0.5
    print(temp**2)
    temp1 = d2**1.5
    print(temp * temp1)
    print(d1 - d2, d2 + d1)
    print("Testing enery")
    v1 = create_dimensioned_quantity("m/s", 100)
    m2 = create_dimensioned_quantity("kg", 5)
    mom = m2*v1
    print(mom)
    print(mom*v1)
    t = create_dimensioned_quantity("s", 2)
    frequency = t**-1
    f = 1 / t
    print(frequency, f.convert_to(False, "Hz"))

    m3 = create_dimensioned_quantity("kg", 10)
    print((2*m3 - m2) / m2)

    a = create_dimensioned_quantity("m^6", 2)
    b = create_dimensioned_quantity("m", 5)
    c = b**-5
    print(a, b, c)
    print(a**-0.5)

    print(v1.to("km/h"))

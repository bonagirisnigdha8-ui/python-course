import math #inporting module

#isclose function to check whether to value are close or not

print(math.isclose(12.014, 12.56))

print(math.isclose(12.014, 12.014))

print(math.isclose(12.45, 12.46))

print(math.isclose(12.014, 12.434, abs_tol = 0.5))

print(math.isclose(12.014, 12.014, abs_tol = 0.4))




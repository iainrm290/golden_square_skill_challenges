def factorial(n):
    product = 1
    print(f"at the start product is {product}")
    while n > 0:
        print(n)
        print()
        # n -= 1
        print(n)
        print()
        print(f"we multiply {product} by {n}")
        product *= n
        print(product)
        print()
        print(f"we get {product}")
        n -= 1
    return product

print(f"""
 Running: factorial(5)
Expected: 120
  Actual: {factorial(5)}
""")

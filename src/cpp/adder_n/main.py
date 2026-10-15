import adder

n = [10, 20, 30, 40]


for i in range(len(n)+1):
    numbers = n[0:i]

    result = adder.add_numbers(*numbers)

    print(f"sum {numbers} = {result}")
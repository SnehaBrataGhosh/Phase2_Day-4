# 31. Create a list of 10 numbers, print sum and average.
# Q31: Create a list of 10 numbers, print sum and average (Ultra-Deep Teaching Version)

def list_sum_and_avg():
    """
    Problem in simple words:
    We need a list of 10 numbers, find their sum, and compute the average.
    Sum is adding all numbers; average is sum divided by total count.
    """

    # Step 1: Create the list
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("Step 1: Created list:", numbers)
    # Here, numbers[0] = 10, numbers[1] = 20, ..., numbers[9] = 100

    # Step 2: Calculate sum manually (to show how sum works internally)
    total = 0
    for idx, num in enumerate(numbers):
        print(f"  Adding numbers[{idx}]={num} to total={total}")
        total += num
        print(f"  New total={total}")
    # After loop, total = 550
    print("Step 2: Total sum =", total)

    # Step 3: Count number of elements
    count = len(numbers)
    print("Step 3: Number of elements =", count)

    # Step 4: Calculate average
    avg = total / count
    print("Step 4: Average =", avg)

    # Step 5: Final results
    print("\nFinal Output:")
    print("List:", numbers)
    print("Sum:", total)
    print("Average:", avg)

# Run Q31
list_sum_and_avg()

"""
Step-by-Step Dry Run:

1. numbers = [10,20,30,...,100]
2. Initialize total=0
3. Loop:
   - i=0, num=10, total=0+10=10
   - i=1, num=20, total=10+20=30
   - i=2, num=30, total=30+30=60
   - i=3, num=40, total=60+40=100
   - i=4, num=50, total=100+50=150
   - i=5, num=60, total=150+60=210
   - i=6, num=70, total=210+70=280
   - i=7, num=80, total=280+80=360
   - i=8, num=90, total=360+90=450
   - i=9, num=100, total=450+100=550
4. count = len(numbers) = 10
5. avg = 550 / 10 = 55.0
6. Print final output.
"""

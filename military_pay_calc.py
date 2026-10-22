# Military Pay Calculator
# Estimates monthly Base Pay, BAS, and BAH based on pay grade

def get_base_pay(pay_grade, years):
    base_pay_table = {
        "E-1": [1917.60, 1917.60, 1917.60, 1917.60],
        "E-2": [2149.20, 2149.20, 2149.20, 2149.20],
        "E-3": [2259.90, 2410.80, 2410.80, 2410.80],
        "E-4": [2503.50, 2630.40, 2756.40, 2843.10],
        "E-5": [2727.30, 2913.00, 3037.50, 3150.60],
        "E-6": [2980.50, 3281.40, 3406.80, 3520.50],
        "E-7": [3445.80, 3758.40, 3885.00, 4000.20],
        "O-1": [3637.20, 3790.80, 4586.40, 4586.40],
        "O-2": [4185.60, 4764.60, 5490.00, 5490.00],
        "O-3": [4836.60, 5476.80, 5906.40, 6186.60],
    }

    if pay_grade not in base_pay_table:
        return None

    # years of service
    if years < 2:
        col = 0
    elif years < 4:
        col = 1
    elif years < 6:
        col = 2
    else:
        col = 3

    return base_pay_table[pay_grade][col]


def get_bas(pay_grade):
    # Officers and enlisted BAS
    if pay_grade.startswith("O"):
        return 311.68
    else:
        return 460.25


def get_bah(pay_grade, has_dependents):
    # BAH rates differ
    bah_table = {
        "E-1": [971.00, 1188.00],
        "E-2": [971.00, 1188.00],
        "E-3": [1026.00, 1275.00],
        "E-4": [1089.00, 1350.00],
        "E-5": [1170.00, 1440.00],
        "E-6": [1260.00, 1530.00],
        "E-7": [1359.00, 1638.00],
        "O-1": [1296.00, 1575.00],
        "O-2": [1440.00, 1728.00],
        "O-3": [1629.00, 1962.00],
    }

    if pay_grade not in bah_table:
        return None

    return bah_table[pay_grade][1] if has_dependents else bah_table[pay_grade][0]


def main():
    print("=" * 45)
    print("   U.S. Military Monthly Pay Calculator")
    print("=" * 45)
    print()

    valid_grades = ["E-1", "E-2", "E-3", "E-4", "E-5",
                    "E-6", "E-7", "O-1", "O-2", "O-3"]

    
    while True:
        pay_grade = input("Enter your pay grade (e.g., E-3, O-1): ").strip().upper()
        if pay_grade in valid_grades:
            break
        print("Invalid pay grade. Please enter E-1 through E-7 or O-1 through O-3.")

   
    while True:
        try:
            years = float(input("Enter your years of service: "))
            if years < 0:
                print("Years of service cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

   
    while True:
        dep_input = input("Do you have dependents? (yes/no): ").strip().lower()
        if dep_input in ["yes", "y"]:
            has_dependents = True
            break
        elif dep_input in ["no", "n"]:
            has_dependents = False
            break
        else:
            print("Please enter 'yes' or 'no'.")

   
    base_pay = get_base_pay(pay_grade, years)
    bas = get_bas(pay_grade)
    bah = get_bah(pay_grade, has_dependents)
    total_pay = base_pay + bas + bah

    # results
    print()
    print("=" * 45)
    print("         Monthly Pay Breakdown")
    print("=" * 45)
    print(f"  Pay Grade:        {pay_grade}")
    print(f"  Years of Service: {years}")
    print(f"  Dependents:       {'Yes' if has_dependents else 'No'}")
    print("-" * 45)
    print(f"  Base Pay:         ${base_pay:,.2f}")
    print(f"  BAS:              ${bas:,.2f}")
    print(f"  BAH:              ${bah:,.2f}")
    print("-" * 45)
    print(f"  Total Monthly Pay: ${total_pay:,.2f}")
    print("=" * 45)
    print()
    print("Note: Estimates based on 2024 pay tables.")
    print("Actual pay may vary by duty station and other factors.")


if __name__ == "__main__":
    main()

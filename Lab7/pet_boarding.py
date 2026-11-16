
import math


def parse_booking(text):
    if not isinstance(text, str):
        return None

    try:
        pet, days = text.split(':')
        pet = pet.strip().title()
        days = float(days)

        if not pet or not math.isfinite(days) or days < 0:
            return None

        return pet, days
    except (ValueError, OverflowError):
        return None


def stay_average(days_csv):
    if not isinstance(days_csv, str):
        return None

    try:
        values = [int(r.strip()) for r in days_csv.split(',')]

        if not values or any(v < 0 for v in values):
            return None

        return sum(values) // len(values)
    except (ValueError, OverflowError):
        return None


def payable_fee(text):
    if not isinstance(text, str):
        return None

    try:
        fee, discount = text.split('|')
        fee = float(fee)
        discount = float(discount)

        if not all(map(math.isfinite, (fee, discount))):
            return None

        if fee < 0 or discount < 0:
            return None

        total = fee * 1.18 - discount

        if not math.isfinite(total):
            return None

        return max(total, 0)
    except (ValueError, OverflowError):
        return None


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter pet:days (e.g. dog:5): ")
    result = parse_booking(user_input)
    print("Pet and Days:", result)

    print("\n==== Running stay_average ====")
    user_input = input("Enter stay lengths in days as CSV (e.g. 2,5,7): ")
    result = stay_average(user_input)
    print("Average Stay:", result)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 1500|100): ")
    result = payable_fee(user_input)
    print("Payable Fee:", result)


if __name__ == "__main__":
    main()

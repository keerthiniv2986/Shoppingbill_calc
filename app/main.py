import sys
from app.billing import BillingSystem

def main():
    billing = BillingSystem()
    print("=== Shopping Bill Calculator ===")
    print("1. Calculate Total Bill")
    print("2. Exit")
    
    choice = input("Enter choice (1-2): ").strip()
    if choice == '2' or choice not in ['1', '2']:
        print("Exiting application.")
        sys.exit(0)
        
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        
        total = billing.calculate_total(price, quantity)
        print(f"Total Bill Amount: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
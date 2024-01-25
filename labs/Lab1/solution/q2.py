import sys

def calculate_net_profit(buying_price, selling_price):
    net_profit = 0
    # Corner case testing
    #Write your code here
    
    initial_stock = 1000
    total_selling_price = selling_price * initial_stock
    restocking_cost = (buying_price + 2) * initial_stock
    net_profit = total_selling_price - restocking_cost

    #Don't write anything below this line, store the calculated net profit in variable net_profit
    print(f"{net_profit}")

if __name__ == "__main__":
    # Check if there are exactly two command line arguments
    if len(sys.argv) != 3:
        print("Usage: python program.py <buying_price> <selling_price>")
    else:
        buying_price_arg = int(sys.argv[1])
        selling_price_arg = int(sys.argv[2])
        calculate_net_profit(buying_price_arg, selling_price_arg)

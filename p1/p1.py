# Solution to:
# Multiples of 3 and 5

def sum_multiples(max_num):
    #keep a running sum so you don't have to generate all the multiples simultaneously
    multiple_sum = 0
    for num in range(1, max_num):
        if (num % 3 == 0 or num % 5 == 0):
            multiple_sum += num

    return multiple_sum 

    
def sum_multiples2(max_num):
    multiples = [num for num in range(1, max_num) if (num % 3 == 0 or num % 5 == 0)]
    return sum(multiples)



def main():
    print(sum_multiples(10**3))

if __name__ == '__main__':
    main() 

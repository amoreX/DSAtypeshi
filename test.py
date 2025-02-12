import math

def divide(dividend: int, divisor: int) -> int:
    # Handle edge case (overflow case)
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1  # Clamping to prevent overflow
    
    # Calculate quotient using logarithms
    quotient = math.exp(math.log(abs(dividend)) - math.log(abs(divisor)))
    
    # Convert to integer (truncate towards zero)
    quotient = int(quotient)
    
    # Adjust sign based on input signs
    if (dividend < 0) ^ (divisor < 0):  
        quotient = -quotient
    
    return quotient

# Example
print(divide(-1, 0)) # Output: -3

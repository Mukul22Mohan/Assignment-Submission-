#Write a program which accept principle, rate and time from user and print the simple interest. 
#The formula to calculate simple interest is: simple interest = principle x rate x time / 100 Solution




principle = int(input('Enter the Principle Amount: '))
rate = int(input('Enter the Rate of the interest: '))
month = int(input('Enter the duration in month '))

time = month / 12               #converting months into year 

simple_interest = (principle * rate * time) / 100

print(f'This is your simple interest {simple_interest} on principle amount of {principle} at the rate of {rate} for {time} month')
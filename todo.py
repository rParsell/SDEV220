print('What is the secret number?')
secret = input()
print('What is the guess')
guess = input()
if guess < secret :
    print('Too Low')
elif guess > secret :
    print('Too High')
else:
    print('Just right')
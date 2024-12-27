def greet():
    print("Welcome to the multilingual Python script!\n")

def वर्गफल_निकालें(संख्या):
    return संख्या ** 2

# Add two numbers
def 加法(数字1, 数字2):
    return 数字1 + 数字2

def fun_fact():
    print("Did you know? Python was named after the comedy group 'Monty Python', not the snake!")

def सम_या_विषम(संख्या):
    if संख्या % 2 == 0:
        return "सम संख्या"
    else:
        return "विषम संख्या"

# Multiply two numbers
def 乘法(数字1, 数字2):
    return 数字1 * 数字2


def main():
    greet()
    
    संख्या = 5
    print(f"वर्गफल निकालें: {संख्या} का वर्गफल है {वर्गफल_निकालें(संख्या)}")
    
    
    号码1, 号码2 = 10, 20
    print(f"加法: {号码1} + {号码2} = {加法(号码1, 号码2)}")
    
    print(f"सम या विषम: {संख्या} एक {सम_या_विषम(संख्या)} है")
    
    print(f"乘法: {号码1} * {号码2} = {乘法(号码1, 号码2)}")
    
    # Displaying a fun fact in English
    fun_fact()

# Execute the main function
if __name__ == "__main__":
    main()

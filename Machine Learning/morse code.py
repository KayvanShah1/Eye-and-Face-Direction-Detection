#Dictionary comprising symbol and its respective morse code. 
MorseCodes = {  'A':'.-',   'B':'-...',   'C':'-.-.',
                'D':'-..',  'E':'.',      'F':'..-.',
                'G':'--.',  'H':'....',   'I':'..',
                'J':'.---', 'K':'-.-',    'L':'.-..',
                'M':'--',   'N':'-.',     'O':'---',
                'P':'.--.', 'Q':'--.-',   'R':'.-.',
                'S':'...',  'T':'-',      'U':'..-',
                'V':'...-', 'W':'.--',    'X':'-..-',
                'Y':'-.--', 'Z':'--..',
                
                '1':'.----', '2':'..---', '3':'...--', 
                '4':'....-', '5':'.....', '6':'-....', 
                '7':'--...', '8':'---..', '9':'----.', 
                '0':'-----',

                ',' :'--..--', '.':'.-.-.-', '+':'.-.-.', 
                '?' :'..--..', '/':'-..-.',  '$':'...-..-',
                '-' :'-....-', '(':'-.--.',  '@':'.--.-.',
                ')' :'-.--.-', '_':'..--.-', '&':'.-...',
                ':' :'---...', ';':'-.-.-.', '!':'-.-.--',
                "'" :'.----.', '=':'-...-',  '"':'.-..-.',
              }

#Defining a function to encode the input message.
def encoder(msg):
    encoded_msg=''
    #Convert entire message to Upper Case.
    msg=msg.upper()
    #When a symbol is encountered in the message it is replaced
    #by its respective morse code else,while blank is kept as it is. 
    for symbol in msg:
        if symbol==' ':
            encoded_msg += ' ' 
        else:
            encoded_msg += MorseCodes[symbol]+ ' '
            
    return encoded_msg

def decoder(msg):
    decoded_msg=''
    msg=list(msg.split())
    for i in msg:
        for symbol in MorseCodes:
            if MorseCodes[symbol]==i:
                decoded_msg += str(symbol)+' '
    decoded_msg = decoded_msg[0:len(decoded_msg)-1]
    
    return decoded_msg

msg=str(input("Enter the message to be encoded : "))

#Calling the encoder function to encode the input message and
#storing the encoded msg into a variable.
encoded_msg=encoder(msg)

print('The encoded message: ',encoded_msg)

decoded_msg=decoder(encoded_msg)

print('The decoded message: ',decoded_msg)

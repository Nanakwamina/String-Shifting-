
#Name: Kobena Badu Enyam
#Email: kobena.badu@azubiafrica.org

#import string library
import string

#define function for encrption
def encryption(text,shift,alphabets):
    #define function for string shifting
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    # put shifted strings into a tuple according upper and lower and punctuations
    shifted_alphabets = tuple(map(shift_alphabet,alphabets))
    print(shifted_alphabets)
    #join alphabets to an empty list 
    final_alphabet = ''.join(alphabets)
    print(final_alphabet)

    #join shifted tuple to an empty list
    final_shifted_alphabet = ''.join(shifted_alphabets)
    print(final_shifted_alphabet)
    # make a dictionary of two variables
    table =  str.maketrans(final_alphabet, final_shifted_alphabet)
    print(table)

    #return the corresponding encryted alphabet for input by user for encrytion
    return text.translate(table)

plaintext = input('please input plaintext to encrypt:')
number_of_shifts = int(input('input the number of shift'))

#limits shifts with modulo 26
number_of_shifts = (number_of_shifts % 26)
print(encryption(plaintext,number_of_shifts,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))
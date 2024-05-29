def alpha_check(alphabet):
    # define the vowel and consonant alphabets
    vowel = "a, e, i, o, u,A,E,I,O,U,"
    consonants = "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z,B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,U,V, W,X,Y,Z"

    # check if the input is a single alphabet character
    if len(alphabet) == 1:
        if alphabet in vowel:
            return "The alphabet is a vowel."
        elif alphabet in consonants:
            return "The alphabet is a consonant."
        else:
            return "Invalid input, Enter a letter."
    else:
        return "Invalid input, Enter a Letter. "


# get input from user
letter = input("enter alphabet to check: ")

# check the input and print
output = alpha_check(letter)
print(output)

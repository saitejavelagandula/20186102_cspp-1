'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    a = list(str(input()))
    l=len(a)
    for i in range(0, l):
        if a[i] == '!' or a[i] == '@' or a[i] == '$' or a[i] == '%' or a[i] == '^' or a[i] == '*' or a[i] == '#':
            a[i] = " "
            print(str(a))


            

if __name__ == "__main__":
    main()

# import sys 
# if len(sys.argv) < 3:
#     print('usage: python argument.py <x> <y>') 
#     sys.exit(1)
    
# print('number of arguments :',len(sys.argv),'arguments.') 
# print('argument list:',str(sys.argv)) 

# x = int(sys.argv[1]) 
# y = int(sys.argv[2]) 
# z = x + y 
# print('x = ',x,'y = ',y,'z = ',z)
import argparse 
if __name__ == "__main__":
    parser = argparse.ArgumentParser() 
    parser.add_argument('--number1',help= 'firstnumber') 
    parser.add_argument('--number2',help= 'secondnumber') 
    parser.add_argument('--operation',help= 'operation') 
    
    args = parser.parse_args()
    print(args.number1) 
    print(args.number2) 
    print(args.operation)
    
    n1 = int(args.number1) 
    n2 = int(args.number2) 
    result = None 
    
    if args.operation == 'add':
        result = n1 + n2 
    elif args.operation == 'subtract':
        result = n1 - n2 
    else:
        print('unsupported operations')
    print('result:',result)
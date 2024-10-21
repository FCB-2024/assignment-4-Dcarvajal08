## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys
def main() :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	x=int(sys.argv([1]))	
	def divisorsx():
		divisorsx=0
		comptadorx=1
		while comptadorx<=x:
				if x%comptadorx==0:
					divisorsx=divisorsx+1
		comptadorx=comptadorx+1
		return(divisorsx)
	r1=divisorsx
 
	def divisorspetitsx():
		comptadorx=1
		divisorspetitsx=0
		while comptadorx<x:
			comptadorpetitsx=1
			while comptadorpetitsx<comptadorx:
				if comptadorx % comptadorpetitsx ==0:
					divisorspetitsx=divisorspetitsx+1
		comptadorx=comptadorx+1
		comptadorpetitsx=comptadorpetitsx+1
		return(divisorspetitsx)
	r2=divisorspetitsx
	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
	if r1>=r2:
			return("Not antiprime")
	else:
			return("Anti-prime")

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main())

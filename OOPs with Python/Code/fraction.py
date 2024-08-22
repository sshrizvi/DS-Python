class Fraction:
    """
    A class to represent a mathematical fraction.

    Attributes
    ----------
    num : int
        The numerator of the fraction.
    den : int
        The denominator of the fraction.

    Methods
    -------
    __str__():
        Returns the string representation of the fraction.
    __add__(other):
        Adds two fractions and returns the result in its simplest form.
    __sub__(other):
        Subtracts one fraction from another and returns the result in its simplest form.
    __mul__(other):
        Multiplies two fractions and returns the result in its simplest form.
    __truediv__(other):
        Divides one fraction by another and returns the result in its simplest form.
    simplest_form():
        Returns the fraction in its simplest form.
    """

    def __init__(self, num=0, den=0) -> None:
        """
        Constructs all the necessary attributes for the Fraction object.

        Parameters
        ----------
        num : int, optional
            The numerator of the fraction (default is 0).
        den : int, optional
            The denominator of the fraction (default is 0).
        """
        self.num = num
        self.den = den
    
    def __str__(self) -> str:
        """
        Returns the string representation of the fraction in the form 'numerator/denominator'.

        Returns
        -------
        str
            The string representation of the fraction.
        """
        fraction = '{}/{}'.format(self.num, self.den)
        return fraction
    
    def __add__(self, other) -> str:
        """
        Adds two fractions and returns the result in its simplest form.

        Parameters
        ----------
        other : Fraction
            The other fraction to be added.

        Returns
        -------
        str
            The result of the addition in its simplest form as a string.
        """
        num = (self.num * other.den) + (other.num * self.den)
        den = self.den * other.den

        sum = Fraction(num, den)

        return sum.simplest_form()

    def __sub__(self, other) -> str:
        """
        Subtracts one fraction from another and returns the result in its simplest form.

        Parameters
        ----------
        other : Fraction
            The fraction to be subtracted.

        Returns
        -------
        str
            The result of the subtraction in its simplest form as a string.
        """
        num = (self.num * other.den) - (other.num * self.den)
        den = self.den * other.den

        difference = Fraction(num, den)

        return difference.simplest_form()

    def __mul__(self, other) -> str:
        """
        Multiplies two fractions and returns the result in its simplest form.

        Parameters
        ----------
        other : Fraction
            The other fraction to be multiplied.

        Returns
        -------
        str
            The result of the multiplication in its simplest form as a string.
        """
        num = self.num * other.num
        den = self.den * other.den

        product = Fraction(num, den)

        return product.simplest_form()

    def __truediv__(self, other) -> str:
        """
        Divides one fraction by another and returns the result in its simplest form.

        Parameters
        ----------
        other : Fraction
            The fraction to divide by.

        Returns
        -------
        str
            The result of the division in its simplest form as a string.
        """
        num = self.num * other.den
        den = self.den * other.num

        quotient = Fraction(num, den)

        return quotient.simplest_form()
    
    def simplest_form(self) -> str:
        """
        Reduces the fraction to its simplest form using the greatest common divisor (GCD).

        Returns
        -------
        str
            The fraction in its simplest form as a string.
        """
        import math
        
        hcf = math.gcd(self.num, self.den)
        num = self.num // hcf
        den = self.den // hcf
        simplest_fraction = Fraction(num, den)

        return simplest_fraction


# Driver Code
frac1 = Fraction(5, 7)
frac2 = Fraction(3, 5)

print('SUM'.ljust(20,' '), ': ', end = '')
print(frac1 + frac2)

print('DIFFERENCE'.ljust(20,' '), ': ', end = '')
print(frac1 - frac2)

print('PRODUCT'.ljust(20,' '), ': ', end = '')
print(frac1 * frac2)

print('QUOTIENT'.ljust(20,' '), ': ', end = '')
print(frac1 / frac2)
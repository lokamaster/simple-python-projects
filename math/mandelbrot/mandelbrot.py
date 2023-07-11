# Mandelbrot constants.
MAX_ITERATIONS = 10**2

# Printing constants.
MARKER = "*"
EMPTY_MARKER = " "
RESOLUTION = 60

# Size of argand plane.
MIN_REAL = -2.5
MAX_REAL = 0.5
RANGE_REAL = MAX_REAL - MIN_REAL
MIN_IMAG = -2
MAX_IMAG = 2
RANGE_IMAG = MAX_IMAG - MIN_IMAG


def mandelbrot(c: complex) -> bool:
    """Calculates if a complex point is in the mandelbrot set.

    A point is in the set if the below sequence is bounded (does not
    grow to infinity).  For the mandelbrot set this is synonymous with
    the absolute value of any point in the sequence never being larger
    than 2.

    The sequence is given by
        next value = (previous value)**2 + c
    where c is a complex number.
    """
    z = 0
    for i in range(MAX_ITERATIONS):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True


def main():
    for i in range(RESOLUTION):
        row = ""
        for j in range(RESOLUTION):
            # The image will be printed from top left to bottom right,
            # i.e. from positive imaginary axis / negative real axis
            # to negative imaginary axis / positive real axist on the
            # Argand plane.

            # Calculate real and imaginary coordinates.
            real = MIN_REAL + RANGE_REAL / RESOLUTION * j  # Re(c))
            imaginary = MAX_IMAG - RANGE_IMAG / RESOLUTION * i  # Im(c)

            # See if point is in the set:
            c = complex(real, imaginary)
            row += MARKER if mandelbrot(c) else EMPTY_MARKER

        # Print row if it is non-empty
        if not row.isspace():
            print(row)


if __name__ == "__main__":
    main()


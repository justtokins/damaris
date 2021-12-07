# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:08:13 2021

@author: warmate tokini
"""


from math import *
import math
import random
from random import choice
from random import randint
import cryptomath

# Picks out the primes of the values of a and b


def primes(a, b):
    prime_list = []
    for n in range(a, b):
        isPrime = True
        for num in range(2, n):
            if n % num == 0:
                isPrime = False
        if isPrime:
            prime_list.append(n)
    return prime_list

# choce a random prime values


prime_list = primes(1, 50)
q = random.choice(prime_list)
p = random.choice(prime_list)
e = random.choice(prime_list)
N = p*q
n = (q-1) * (p-1)
print('N', + N)
# list out the factors of n


def factors(n):
    """
    Get factors of n.

    Parameters
    ----------
    n : Integer
        (q-1) * (p-1).

    Returns
    -------
    data : List
        Returns a list of a the factors of n.

    """
    data = []
    for i in range(1, n + 1):
        if n % i == 0:
            data.append(i)
    return data


a = factors(n)

# checks if the e is included in the factors of n and if so picks a new
# value for e


def random_exclude(e):
    """
    Exclude function.

    Parameters
    ----------
    e : Ineger
        Makes the value of e is not found in the factors of n.

    Returns
    -------
    m : Integer
       Returns the value of e when e is not a factor of n.

    """
    exclude = set(a)
    for e in exclude:
        while e in exclude:
            e = random.choice(prime_list)
    else:
        if e not in exclude:
            return (e)
    return (e)


b = random_exclude(e)


# checks for the greatest common divisor of a and b
# although i dont see how this usefull

o = gcd(b, n)

# this runs the euclidean algorithm
# still no use as phi(n) was already defined as (p-1) * (q-1)
print('b', + b)
print('n', + n)

# e*d % n == 1
k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if gcd(b, n) == 1:
    d = cryptomath.Inverse(b, n)
print('d', +d)


# generates aes sbox values

sbox = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
        0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2,
        0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5,
        0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80,
        0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6,
        0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe,
        0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02,
        0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda,
        0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e,
        0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8,
        0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac,
        0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
        0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74,
        0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57,
        0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87,
        0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d,
        0x0f, 0xb0, 0x54, 0xbb, 0x16
    ]

sboxInv = [
            0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3,
            0x9e, 0x81, 0xf3, 0xd7, 0xfb,
            0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43,
            0x44, 0xc4, 0xde, 0xe9, 0xcb,
            0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95,
            0x0b, 0x42, 0xfa, 0xc3, 0x4e,
            0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2,
            0x49, 0x6d, 0x8b, 0xd1, 0x25,
            0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c,
            0xcc, 0x5d, 0x65, 0xb6, 0x92,
            0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46,
            0x57, 0xa7, 0x8d, 0x9d, 0x84,
            0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58,
            0x05, 0xb8, 0xb3, 0x45, 0x06,
            0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd,
            0x03, 0x01, 0x13, 0x8a, 0x6b,
            0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf,
            0xce, 0xf0, 0xb4, 0xe6, 0x73,
            0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37,
            0xe8, 0x1c, 0x75, 0xdf, 0x6e,
            0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62,
            0x0e, 0xaa, 0x18, 0xbe, 0x1b,
            0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0,
            0xfe, 0x78, 0xcd, 0x5a, 0xf4,
            0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10,
            0x59, 0x27, 0x80, 0xec, 0x5f,
            0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a,
            0x9f, 0x93, 0xc9, 0x9c, 0xef,
            0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb,
            0x3c, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14,
            0x63, 0x55, 0x21, 0x0c, 0x7d
    ]
# The substitution Box limits the capabites of the system


class Encryption():
    """This class contains the encryption and decryption functions.

    and should be called befor the class functions.
    """

    def __init__(self):
        """
        Start the execution of the class.

        Returns
        -------
        None.

        """
        pass

    def encrypt(self, M1, M2):
        """
        Encryption function.

        Parameters
        ----------
        M1 : integer
            Stores the first input message given by the user.
        M2 : Integer
            Stores the second input message given by the user.

        Returns
        -------
        last_cypher : Integer
            This gives the final encrypted message also known as c'.

        """
        self.M1 = M1

        self.M2 = M2

        M3 = M1*M2

        C1 = (M1**b) % N
        print('c1 = ', + C1)

        C2 = (M2**b) % N
        print('c2 = ', + C2)

        C3 = int(C1 * C2) % N
        print('c3 = ', + C3)

        C4 = sbox[C3]

        last_cypher = int(C4**b % N)
        print("last ", + last_cypher)

        return last_cypher

        """ in the project work it was stated we had to first convert
             to binary and the divide by two
            and convert the resulting two 4 bits binary values into their
            equvalent hex values and run them through the sbox
            but with this function all that is done automatically and with
            less lines of codes
            """

    def decrypt(self, data):
        """
        Decryption function.

        Parameters
        ----------
        data : Integer
            Takes the final cypher-text or c'
            from the encryption class as input value

        Returns
        -------
        message : Integer
            DESCRIPTION.

        """
        self.data = data

        mess = (data**d) % N
        print('mess', + mess)

        messinvs = sboxInv[mess]

        message = int(messinvs**d % N)
        print(message)

        return message

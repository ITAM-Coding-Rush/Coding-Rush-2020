#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import sys
import os
import re
import unittest

from omegaup.validator import validatortest


class Test(unittest.TestCase):
    def test(self):
        with open('data.in', 'r') as handle:
            original_input = handle.read()

        lines = original_input.split('\n')

        # En la la primera línea, un entero N
        regex = re.compile(r'^(\d+)$')
        self.assertTrue(regex.match(lines[0]))
        N = int(lines[0])
        self.assertEqual(1 <= N <= 100000)

        # En la segunda línea, un entero K
        regex = re.compile(r'^(\d+)$')
        self.assertTrue(regex.match(lines[1]))
        K = int(lines[1])
        self.assertEqual(0 <= K <= 1e9)

        # En las siguientes N líneas el arreglo
        lines = lines[2:]
        self.assertEqual(len(lines), N)
        for line in lines:
            # Cada línea debe tener un número A_i
            regex = re.compile(r'^(\d+)$')
            self.assertTrue(regex.match(line))
            # El número es menor a 1e9
            x = int(line)
            self.assertEqual(0 <= x <= 1e9)


if __name__ == '__main__':
    validatortest.main()

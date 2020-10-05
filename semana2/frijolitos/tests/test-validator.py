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

        # Aquí añade los checks necesarios de la entrada
        lines = original_input.split('\n')
        self.assertEqual(lines[-1], '')
        lines.pop()

        # En las primeras dos líneas hay dos números, n y k
        regex = re.compile(r'^(\d+)\n(\d+)$')
        self.assertTrue(regex.match(lines[0]))
        N, K = [int(v) for v in lines[0].split('\n')]

        # Checar que estén correctos los límites de N y K
        self.assertEqual(1 <= N <= 100000)
        self.assertEqual(0 <= K <= 1e9)

        lines = lines[2:]
        # Hay N líneas
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

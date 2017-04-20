#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tiangan = "甲乙丙丁戊己庚辛壬癸"
dizhi = "子丑寅卯辰巳午未申酉戌亥"

jiazi = [tiangan[n % len(tiangan)] + dizhi[n % len(dizhi)] for n in range(60)]

print(jiazi)
print(len(jiazi))

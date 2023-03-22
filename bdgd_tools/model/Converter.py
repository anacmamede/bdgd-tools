# -*- encoding: utf-8 -*-
"""
 * Project Name: bdgd_tests
 * Created by eniocc
 * Date: 08/03/2023
 * Time: 22:52
 *
 * Edited by: eniocc
 * Date: 08/03/2023
 * Time: 22:52
"""
import json
import pathlib


# Pular 1 acima
def convert_tten(case):
    switch_dict = {
        "0": 0.11,
        "1": 0.115,
        "2": 0.12,
        "3": 0.121,
        "4": 0.125,
        "5": 0.127,
        "6": 0.208,
        "7": 0.216,
        "8": 0.2165,
        "9": 0.22,
        "10": 0.23,
        "11": 0.231,
        "12": 0.24,
        "13": 0.254,
        "14": 0.38,
        "15": 0.4,
        "16": 0.44,
        "17": 0.48,
        "18": 0.5,
        "19": 0.6,
        "20": 0.75,
        "21": 1,
        "22": 2.3,
        "23": 3.2,
        "24": 3.6,
        "25": 3.785,
        "26": 3.8,
        "27": 3.848,
        "28": 3.985,
        "29": 4.16,
        "30": 4.2,
        "31": 4.207,
        "32": 4.368,
        "33": 4.56,
        "34": 5,
        "35": 6,
        "36": 6.6,
        "37": 6.93,
        "38": 7.96,
        "39": 8.67,
        "40": 11.4,
        "41": 11.9,
        "42": 12,
        "43": 12.6,
        "44": 12.7,
        "45": 13.2,
        "46": 13.337,
        "47": 13.53,
        "48": 13.8,
        "49": 13.86,
        "50": 14.14,
        "51": 14.19,
        "52": 14.4,
        "53": 14.835,
        "54": 15,
        "55": 15.2,
        "56": 19.053,
        "57": 19.919,
        "58": 21,
        "59": 21.5,
        "60": 22,
        "61": 23,
        "62": 23.1,
        "63": 23.827,
        "64": 24,
        "65": 24.2,
        "66": 25,
        "67": 25.8,
        "68": 27,
        "69": 30,
        "70": 33,
        "71": 34.5,
        "72": 36,
        "73": 38,
        "74": 40,
        "75": 44,
        "76": 45,
        "77": 45.4,
        "78": 48,
        "79": 60,
        "80": 66,
        "81": 69,
        "82": 72.5,
        "83": 88,
        "84": 88.2,
        "85": 92,
        "86": 100,
        "87": 120,
        "88": 121,
        "89": 123,
        "90": 131.6,
        "91": 131.63,
        "92": 131.635,
        "93": 138,
        "94": 145,
        "95": 230,
        "96": 245,
        "97": 345,
        "98": 500,
        "99": 550,
        "100": 750,
        "101": 1000,
    }
    return switch_dict.get(case, 'Invalid case')

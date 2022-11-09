const romanToInt = require('../6_leetcode_roman_to_integer_13')

test('roman to Integer convert: with input III', () => {
  expect(romanToInt('III')).toBe(3)
})

test('roman to Integer convert: with input IV', () => {
  expect(romanToInt('IV')).toBe(4)
})

test('Roman to Int: with input IX', () => {
  expect(romanToInt('LVIII')).toBe(58)
})

test('Roman to Integer: with input MCMXCIV', () => {
  expect(romanToInt('MCMXCIV')).toBe(1994)
})

test('Roman to Int: with input MMMCMXCIX', () => {
  expect(romanToInt('MMMCMXCIX')).toBe(3999)
})

test('Roman to Int: with input XCVIII', () => {
  expect(romanToInt('XCVIII')).toBe(98)
})

test('Roman to Int: with input MMXXIII', () => {
  expect(romanToInt('MMXXIII')).toBe(2023)
})

test('Roman to Int: with input MMM', () => {
  expect(romanToInt('MMM')).toBe(3000)
})

test('Roman to Int: with input MMMCMXCIX', () => {
  expect(romanToInt('LXXXVIII')).toBe(88)
})

test('Roman to Int with Input MCMXCIII', () => {
  expect(romanToInt('MCMXCIII')).toBe(1993)
})

test('Roman to Int with Input MCDLXXVI', () => {
  expect(romanToInt('MCDLXXVI')).toBe(1476)
})

test('Roman to Int with Input MMMXLV', () => {
  expect(romanToInt('MMMXLV')).toBe(3045)
})

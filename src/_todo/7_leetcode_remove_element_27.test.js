const removeElement = require('../7_leetcode_remove_element_27')

test('RemoveElement ', () => {
  expect(removeElement([3, 2, 2, 3], 3)).toBe(2)
})

test('RemoveElement ', () => {
  expect(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)).toBe(5)
})

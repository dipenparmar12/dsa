console.clear()
console.log(new Date(), '-----------')

// Reference
// @src: https://codehandbook.org/split-number-individual-digits-using-javascript/#:~:text=JavaScript%20split%20method%20can%20be,transform%20each%20letter%20to%20Number.

function countChars(numsLength, char) {
  const numbers = Array.from({length:numsLength}, (_, i) => i+1)
  return ([...numbers + ''].map(Number).reduce((acc, num)=> acc += num === char, 0))
}


const count2 = countChars(30, 2) // 13 
const count3 = countChars(100, 3) // 20
const count4 = countChars(100, 1) // 21
console.log('index.js::[20] count2, count3', count2, count3, count4)

// // function countChars(nums, char) {
// //   return nums.reduce((acc,item) => {
// //     const chars = item.toString().split('')
// //     if( chars.includes(char.toString())) {
// //       chars.forEach(char => (char === char.toString()) && (acc += 1))
// //     }
// //     return acc
// //   }, 0)
// // }

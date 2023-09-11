console.clear()
console.log(new Date(), '-----------')

/* 
========================================================
 
 4, 3, 1, 2
 i
    j

i=0 -> 3,4,1,2
i=1 -> 
======================================================== 
*/
function test() {
  let arr = [4, 6, 3, 1, 2]
  function swap(i, j) {
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
  }

  for (let i = 0; i < arr.length; i++) {
    for (let j = i; j < arr.length; j++) {
      if (arr[i] < arr[j]) {
        swap(i, j)
      }
    }
  }

  console.log('index.js::[6] a', arr)
}


const output = test(30, 2)
// console.log('index.js::[20] output', output)
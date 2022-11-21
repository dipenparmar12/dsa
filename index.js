console.clear()
console.log(new Date(), '-----------')

function test() {
  console.log('index.js::[5] ',  ...arguments)
  return [...arguments]
}


const output = test(30, 2)
console.log('index.js::[20] output', output)
console.clear()
console.log(new Date(), '-----------')

function test(arg) {
  let result = {}

  console.log('index.js::[7] arg', arg)
  return result
}

console.log('OUTPUT::', test())

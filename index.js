console.clear()
console.log(new Date(), '-----------')

// // Expected output is 
// {
//   "userName": "XYZ",
//   "userCreatedDate": "123424",
//   "userDepartmentId": "0123",
//   "userDepartmentType": "ABC"
// }

const obj = {
  "user":{
    "name": "XYZ",
    "createdDate": "123424",
    "department": {
      "id": "0123",
      "type": "ABC"
    }}
}

function isObject(x) {
  return Object.prototype.toString.call(x) === '[object Object]'
}

function test(source, key ='') {
  if(!isObject(source))  return source
  let result = {}

  for (const parentKey in source) {
    console.log('index.js::[33] parentKey',  parentKey, key, source, source[parentKey])
      // if(){ }
      for (const key in source[parentKey]) {
        if(isObject(source[parentKey][key])){
          result[parentKey + key] = test(source[parentKey][key], parentKey + key)
        } else {
          result[parentKey + key] =  source[parentKey][key]
        }
      }
  }

  return result
}

console.log('------------------------', )
console.log(test(obj))
// // My Input is
// {
//   "user": {
//     "name": "XYZ"
//     "createdDate": "123424",
//     "department": {
//       "id": "0123",
//       "type": "ABC"
//     }
//   }
// }


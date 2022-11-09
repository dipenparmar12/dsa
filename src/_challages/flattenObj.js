console.clear()
console.log(new Date(), '-----------')

function flattenObj(source, key = '') {
  if (!isObject(source)) return source
  let result = {}

  for (const [prop, el] of Object.entries(source)) {
    const newKey = (key ? key + '_' : '') + prop
    if (isObject(el)) {
      const temp = flattenObj(el, newKey)
      result = { ...result, ...temp }
    } else {
      result[newKey] = el
    }
  }

  return result
}

const obj = {
  user: {
    name: 'XYZ',
    createdDate: '123424',
    department: {
      id: '0123',
      type: 'ABC',
      staff: {
        a: 'a',
        b: {
          name: 'IamB_',
          age: 12,
        },
      },
    },
  },
}
// // Expected output is
// const OUTPUT = {
//   user_name: 'XYZ',
//   user_createdDate: '123424',
//   user_department_id: '0123',
//   user_department_type: 'ABC',
//   user_department_staff_a: 'a',
//   user_department_staff_b_name: 'IamB_',
//   user_department_staff_b_age: 12,
// }

console.log('OUTPUT::', flattenObj(obj))

function isObject(x) {
  return Object.prototype.toString.call(x) === '[object Object]'
}

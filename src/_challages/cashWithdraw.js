/* 
You have to write logic to withdraw money from an ATM Machine. Consider a hypothetical ATM machine
which gives you notes of 10, 20, 50, 100, 500 & 1000 in denomination. If I enter 5,550 Rs. It should give me
5 notes of 1000, 1 note of 500 and 1 note of 50. ATM machines cannot store coins. So, if the input amount is
something like 1978 then the machine should print “Invalid Amount”.


Case 1:
Input: 2340
Output:
2 x 1000 = 2000
3 x 100 = 300
2 x 20 = 40
Total = 2340

Case 2:
Input: 7878
Output: “Invalid Amount”

Case 3:
Input: 5680
Output:
5 x 1000 = 5000
1 x 500 = 500
1 x 100 = 100
1 x 50 = 50
1 x 20 = 20
1 x 10 = 10
Total = 5680

*/

console.clear()
console.log(new Date(), '-----------')

function cashWithdrawMath(amt) {
  if (amt <= 0 || amt % 10 !== 0) return 'Invalid Amount'
  const banknotes = [1000, 500, 100, 50, 20, 10]
  const output = {}

  while (amt > 0) {
    const note = banknotes.find((note) => (amt >= note ? note : 0))
    output[note] = Math.floor(amt / note)
    amt = amt % note
  }

  console.log('cashWithdraw.js::[58] ', output)
  return output
}

// console.log(10000, ':', cashWithdrawMath(5680))
// console.log(10000, ':', cashWithdrawMath(5680))
// console.log(10000, ':', cashWithdrawMath(2340))

;[0, 10, -10, 11, 15, 2340, 7878, 5680].forEach((amt) => {
  console.log('cashWithdraw.js::[79] amt', cashWithdrawMath(amt))
})

// function cashWithdraw(amount){
//   if (amount <= 0 || amount % 10 !== 0) return 'Invalid Amount'
//   const banknotes = [1000, 500, 100, 50, 20, 10]
//   const output = {}
//   while(amount > 0) {
//     const note  = banknotes.find(note =>  amount >= note ? note: 0)
//     output[note] = output[note] ? output[note] + 1 : 1
//     amount -= note
//   }
//   return output
// }

// [0, 10, -10, 11, 15, 2340, 7878, 5680].forEach(amt => {
//   console.log('cashWithdraw.js::[79] amt', cashWithdraw(amt))
// })

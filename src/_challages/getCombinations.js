console.clear()
console.log(new Date(), '-----------')
const log = console.log

function getCombinations(arr) {
  if (arr.length === 0) return [[]]

  const firstEl = arr[0]
  const rest = arr.slice(1)

  const combWithoutFirst = getCombinations(rest)
  let combWithFirst = []

  combWithoutFirst.forEach((comb) => {
    const combWithFirstEl = [...comb, firstEl]
    combWithFirst.push(combWithFirstEl)
  })

  console.log(
    'getCombinations.js::[19] LEN:',
    [...combWithoutFirst, ...combWithFirst].length,
  )
  return [...combWithoutFirst, ...combWithFirst]
}

console.log('getCombinations::', getCombinations([]))
console.log('getCombinations::', getCombinations(['a']))
console.log('getCombinations::', getCombinations(['a', 'b']))
console.log('getCombinations::', getCombinations(['a', 'b', 'c']))
console.log('getCombinations::', getCombinations(['a', 'b', 'c', 'd']))
console.log('getCombinations::', getCombinations(['A', 'B', 'C', 'D', 'E']))

t = `
@see: https://codereview.stackexchange.com/questions/7001/generating-all-combinations-of-an-array

const powerset = (array) => { // O(2^n)
	const results = [[]];
	for (const value of array) {
		const copy = [...results]; // See note below.
		for (const prefix of copy) {
			results.push(prefix.concat(value));
		}
	}
	return results;
};

console.log(powerset(['A', 'B', 'C']) );

Because results is extended within the loop body, we cannot iterate over it using for-of — doing so would iterate over the newly added elements as well, resulting in an infinite loop. We only want to iterate over the elements that are in results when the loop starts, i.e. indices 0 until results.length - 1. So we either cache the original length in a variable and use that, i.e.
for (let index = 0, length = results.length; index < length; index++) {
    const prefix = results[index];
    // …
}
…or we just create a static copy of results and iterate over that.


--------------
function combinations(str) {
    var fn = function(active, rest, a) {
        if (!active && !rest)
            return;
        if (!rest) {
            a.push(active);
        } else {
            fn(active + rest[0], rest.slice(1), a);
            fn(active, rest.slice(1), a);
        }
        return a;
    }
    return fn("", str, []);
}

function getCombinations(chars) {
  var result = [];
  var f = function(prefix, chars) {
    for (var i = 0; i < chars.length; i++) {
      result.push(prefix + chars[i]);
      f(prefix + chars[i], chars.slice(i + 1));
    }
  }
  f('', chars);
  return result;
}


function string_recurse(active, rest) {
    if (rest.length == 0) {
        console.log(active);
    } else {
        string_recurse(active + rest.charAt(0), rest.substring(1, rest.length));
        string_recurse(active, rest.substring(1, rest.length));
    }
}
string_recurse("", "abc");

`

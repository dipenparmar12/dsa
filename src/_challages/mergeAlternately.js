/**
 * Merges two strings by adding letters in alternating order, starting with word1.
 * If a string is longer than the other, appends the additional letters to the end
 * of the merged string.
 *
 * @param {string} word1 - The first input string.
 * @param {string} word2 - The second input string.
 * @returns {string} The merged string.
 *
 * @example
 * // Example 1:
 * const word1 = "abc";
 * const word2 = "pqr";
 * const result = mergeStrings(word1, word2);
 * // Output: "apbqcr"
 * // Explanation: The merged string will be merged as so:
 * // word1:  a   b   c
 * // word2:    p   q   r
 * // merged: a p b q c r
 *
 * @example
 * // Example 2:
 * const word1 = "ab";
 * const word2 = "pqrs";
 * const result = mergeStrings(word1, word2);
 * // Output: "apbqrs"
 * // Explanation: Notice that as word2 is longer, "rs" is appended to the end.
 * // word1:  a   b 
 * // word2:    p   q   r   s
 * // merged: a p b q   r   s
 *
 * @example
 * // Example 3:
 * const word1 = "abcd";
 * const word2 = "pq";
 * const result = mergeStrings(word1, word2);
 * // Output: "apbqcd"
 * // Explanation: Notice that as word1 is longer, "cd" is appended to the end.
 * // word1:  a   b   c   d
 * // word2:    p   q 
 * // merged: a p b q c   d
 */
function mergeStrings(word1, word2) {
    let i = 0;
    let output = "";

    while (i <= word1.length || i <= word2.length) {

        if (i < word1.length) {
            output += word1[i];
        }

        if (i < word2.length) {
            output += word2[i];
        }

        i++;
    }
    return output;
}

/*
    Runtime
    Details
    54ms
    Beats 53.86%of users with JavaScript
    Memory
    Details
    42.77MB
    Beats 20.73%of users with JavaScript
*/


/*

/**

var mergeAlternately_1 = function(word1, word2) {
    let i = 0
    let j =0
    let arr = []
    while(i<word1.length && j<word2.length){
        arr.push(word1[i++])
        arr.push(word2[j++])
    }
    while(i<word1.length){
        arr.push(word1[i++])
    }
    while(j<word2.length){
        arr.push(word2[j++])
    }
    return arr.join("")
};

*/
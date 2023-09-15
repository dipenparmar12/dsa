/**
 * 2833. Furthest Point From Origin
 * You are given a string moves of length n consisting only of characters 'L', 'R', and '_'. The string represents your movement on a number line starting from the origin 0.
 * In the ith move, you can choose one of the following directions:
 * move to the left if moves[i] = 'L' or moves[i] = '_'
 * move to the right if moves[i] = 'R' or moves[i] = '_'
 * Return the distance from the origin of the furthest point you can get to after n moves.
 * @difficulty Easy
 * @param {String} moves
 * @returns {Number}
 * @example
 * // Example 1:
 * const moves = "RRR";
 * const result = furthestDistanceFromOrigin(moves);
 * // Output: 3
 * // Explanation: The only optimal move is to take all three steps to the right.
 * // The origin at 0 is the only reachable point after 3 moves.
 *
 * @example
 * // Example 2:
 * const moves2 = "L_RL__R";
 * const result2 = furthestDistanceFromOrigin(moves2);
 * // Output: 3
 * // Explanation: The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves "LLRLLLR".
 *
 * @example
 * // Example 3:
 * const moves3 = "_R__LL_";
 * const result3 = furthestDistanceFromOrigin(moves3);
 * // Output: 5
 * // Explanation: The furthest point we can reach from the origin 0 is point -5 through the following sequence of moves "LRLLLLL".
 *
 * @example
 * // Example 4:
 * const moves4 = "_______";
 * const result4 = furthestDistanceFromOrigin(moves4);
 * // Output: 7
 * // Explanation: The furthest point we can reach from the origin 0 is point 7 through the following sequence of moves "RRRRRRR".
 *
 * @example
 * // Example 5:
 * const moves5 = "R_";
 * const result5 = furthestDistanceFromOrigin(moves5);
 * // Output: 2
 * @see {@link https://leetcode.com/problems/furthest-point-from-origin/|LeetCode post}
 */
function furthestDistanceFromOrigin(moves) {
    let moved = moves.split('').reduce((acc, item)=>{
        acc[item] += 1
        return acc
    }, {R:0,L:0,_:0, far:0})

    if(moved.R > moved.L) {
       moved.far = moved.R - moved.L
    } 
    
    if(moved.L > moved.R) {
       moved.far = moved.L - moved.R
    }

    return Math.abs(moved.far += moved._)
}

/*
Runtime
57ms
Beats 86.83%of users with JavaScript

Memory
43.98MB
Beats 76.25%of users with JavaScript
*/



/*

var furthestDistanceFromOrigin = function(moves) {
    // Initialize a variable to keep track of the distance from the origin.
    let distanceFromOrigin = 0;

    // Initialize a variable to count the number of dashes encountered.
    let dashCount = 0;

    // Loop through each character in the 'moves' string.
    for (const move of moves) {
        // Check if the current character is a dash ('_').
        if (move === '_') {
            // Increment the dash count.
            ++dashCount;
        }
        // Check if the current character is 'L'.
        else if (move === 'L') {
            // Move left by decrementing the distance from the origin.
            --distanceFromOrigin;
        }
        // If neither dash nor 'L', then the character must be 'R'.
        else {
            // Move right by incrementing the distance from the origin.
            ++distanceFromOrigin;
        }
    }

    // Return the sum of absolute distance from the origin and dash count.
    return Math.abs(distanceFromOrigin) + dashCount;
};

*/
/**
 * You are given an integer array nums consisting of n elements, and an integer k.
 * Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
 * Any answer with a calculation error less than 10-5 will be accepted.
 * 
 * @title 643. Maximum Average Subarray I
 * @link https://leetcode.com/problems/maximum-average-subarray-i/
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 * @example 
 * // Example 1:
 * const nums = [1,12,-5,-6,50,3];
 * const k = 4;
 * const result = findMaxAverage(nums, k);
 * // Output: 12.75
 * // Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 * @example
 * // Example 2:
 * const nums = [5];
 * const k = 1;
 * const result = findMaxAverage(nums, k);
 * // Output: 5.00
 * @example
 * // Example 3:
 *  const nums = [0,1,1,3,3];
 * const k = 4;
 * const result = findMaxAverage(nums, k);
 * // Output: 2.00
 * @example
 * // Example 4:
 * const nums = [4,2,1,3,3];
 * const k = 2;
 * const result = findMaxAverage(nums, k);
 * // Output: 3.00
 */
function findMaxAverage(nums, k) {
    maxS = Number.MIN_VALUE;
    temp = 0;

    for (i = 0; i < k; i++) {
        // console.log(temp, nums[i])
        console.log(i, nums[i]);
        temp += nums[i];
    }

    maxS = temp;

    for (j = k; j < nums.length; j++) {
        // console.log(temp, nums[j])
        temp += nums[j];
        temp -= nums[j - k];

        // console.log(j, ":", temp, nums[j])
        if (temp > maxS) {
            maxS = temp;
        }
    }

    // console.log("----", maxS)
    return maxS / k;
}

/*
Runtime
879ms
Beats 20.81%of users with JavaScript

Memory
72.33MB
Beats 5.05%of users with JavaScript
*/



/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
function findMaxAverage1(nums, k) {
    let front = 0;
    let back = k - 1;
    let avg = (nums.slice(0, k).reduce((p, c) => p + c, 0)) / k;
    let maxAvg = avg;
    // console.log(`Avg from [${front}, ${back}]: ${avg}`)
    while (back < nums.length - 1) {
        let sum = avg * k;

        // remove front
        sum -= nums[front];
        front++;

        // add back
        back++;
        sum += nums[back];

        avg = sum / k;
        // console.log(`Avg from [${front}, ${back}]: ${avg}`)
        maxAvg = Math.max(maxAvg, avg);
    }

    return maxAvg;
}


/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = (x) => {
  let r = 0
  let p = x
  while (p > 0) {
    let rem = p % 10
    p = (p - rem) / 10
    r = r * 10 + rem
  }
  return r === x
};

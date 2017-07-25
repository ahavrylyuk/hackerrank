const reverse = (num) => {
  const split = (num, base) => {
    if (num === 0) return []
    const rem = num % base
    return [rem].concat(split(num - rem, base * 10))
  }
  const nums = split(num, 10)
  const reversed = nums.reduce((rev, n, i) => {
    const div = Math.pow(10, i)
    const mult = Math.pow(10, nums.length - 1 - i)
    return rev + n / div * mult
  }, 0)
  return Math.abs(reversed) > Math.pow(2, 32 - 1) ? 0 : reversed
}

a = reverse(-153423646)

const reverse = (num) => {
  const split = (x) => {
    if (x === 0) return []
    const rem = x % 10
    return [rem].concat(split((x - rem) / 10))
  }
  const reversed = split(num).reduce((rev, x) => 10 * rev + x, 0)
  return Math.abs(reversed) > Math.pow(2, 32 - 1) ? 0 : reversed
}

a = reverse(-123)

const reverse = (num) => {
  let rev = 0;
  const max = Math.pow(2, 32 - 1)
  while (num !== 0) {
    let rem = num % 10
    rev = rev * 10 + rem
    if (Math.abs(rev) > max) return 0
    num = (num - rem) / 10
  }
  return rev
}

a = reverse(-123)

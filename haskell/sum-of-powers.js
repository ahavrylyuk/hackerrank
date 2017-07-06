const sum = xs => xs.reduce((s, x) => s + x, 0)
const cons = (x, xs) => [].concat(xs).concat(x)
const foldIf = (xs, pred) => xs.reduce((xs, x, i) => pred(i, x, xs) ? cons(x, xs) : xs, [])
const take = (c, xs) => foldIf(xs, i => i < c)
const drop = (c, xs) => foldIf(xs, i => i > c - 1)

const generator = (next, current) => () => {
  const prev = current
  current = next(current)
  return prev
}

const takeWhile = (pred, iter) => {
  const acc = []
  let curr = iter()
  while(pred(curr)) {
    acc.push(curr)
    curr = iter()
  }
  return acc
}

const sumOfPow = (n, x) => {
  const numbers = generator(i => i + 1, 1)
  const powers = takeWhile(x => x <= n, generator(i => Math.pow(numbers(), x), numbers()))

  // for (let i = 0; i < powers.length; i++) {
  //   const line = drop(i, powers)
  //   for (let j = 0; j < line.length; j++) {
  //     console.log(take(j + 1, line))
  //   }
  // }

  const subsetSum = (acc, curr, values) => {
    const s = sum(curr)
    if (s === n) return acc.push(curr)
    if (s > n) return
    for (let i = 0; i < values.length; i++) {
      const v = values[i];
      subsetSum(acc, cons(v, curr), drop(i + 1, values))
    }
    return acc
  }
  return subsetSum([], [], powers)
}

const r = sumOfPow(100, 2)
r

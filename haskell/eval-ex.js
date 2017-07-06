var f = [];
function factorial (n) {
  if (n == 0 || n == 1)
    return 1;
  if (f[n] > 0)
    return f[n];
  return f[n] = factorial(n-1) * n;
}   

solve = x =>     
	Array.from(new Array(9), (_,i) => i + 1)
		.map(t => Math.pow(x, t)/factorial(t))
		.reduce((sum, x) => sum + x, 1);

console.log(solve(20));

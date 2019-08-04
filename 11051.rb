def binomial(n, k)
  return 1 if k == 0
  (((n-k+1)..n).reduce(:*) / (1..k).reduce(:*)) % 10007
end

n, k = gets.split.map(&:to_i)
puts binomial(n,k)

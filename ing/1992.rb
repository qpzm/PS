# Why runtime error at 100%?
# 1992.py passes

def quadtree(size, arr, i, j)
  val = arr[i][j]
  same = true

  (0...size).each do |x|
    (0...size).each do |y|
      if arr[i + x][j + y] != val
        same = false
        break
      end
    end
  end

  return val if same

  half = size / 2
  "(#{quadtree(half, arr, i, j) +
    quadtree(half, arr, i, j + half) +
    quadtree(half, arr, i + half, j) +
    quadtree(half, arr, i + half, j + half)})"
end

if __FILE__ == $0
  size = gets.to_i
  arr = []
  size.times do
    arr << gets.chomp!.chars
  end
  puts quadtree(size, arr, 0, 0)
end

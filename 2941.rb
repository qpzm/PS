module Croatian
  PATTERN = /c=|c-|dz=|d-|lj|nj|s=|z=|[a-z]/

  def self.count(str)
    str.scan(PATTERN).size
  end
end

if __FILE__ == $0
  puts Croatian.count(gets)
end

class Bst
  attr_reader :data, :right, :left

  def initialize(data)
    @data = data
  end

  def insert(num)
    if num > data
      @right&.insert(num) || @right = Bst.new(num)
    else
      @left&.insert(num) || @left = Bst.new(num)
    end
  end

  def self.build_from_preorder(list)
    bst = Bst.new(list[0])
    list[1..-1].each { |e| bst.insert(e) }
    bst
  end

  def postorder
    @left&.postorder
    @right&.postorder
    puts data
  end
end

inputs = ARGF.each_line.map(&:to_i)
bst = Bst.build_from_preorder(inputs)
bst.postorder

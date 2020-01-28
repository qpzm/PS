# frozen_string_literal: true
require 'ruby-prof'

class Board
  attr_accessor :matrix
  attr_reader :size

  def initialize(matrix, size)
    @matrix = matrix
    @size = size
  end

  def [](i, j)
    raise StandardError if i < 0 || i > size || j < 0 || j > size
    @matrix[i * size + j]
  end

  def []=(i, j, x)
    raise StandardError if i < 0 || i > size || j < 0 || j > size
    @matrix[i * size + j] = x
  end

  def available?(row, col)
    self[row, col].zero?
  end

  def fill!(row, col)
    fill_row(row, col)
    fill_col(col)
    fill_upper_diagnoal(row, col)
    fill_lower_diagonal(row, col)
    # To mark queen
    # self[row, col] = 2
  end

  private

  def fill_row(row, col)
    (col...size).each { |j| self[row, j] = 1 }
  end

  def fill_col(col)
    (0...size).each { |i| self[i, col] = 1 }
  end

  def fill_upper_diagnoal(row, col)
    margin = [row, size - col - 1].min
    (0..margin).each { |i| self[row - i, col + i] = 1 }
  end

  def fill_lower_diagonal(row, col)
    margin = [size - row - 1, size - col - 1].min
    (0..margin).each { |i| self[row + i, col + i] = 1 }
  end
end

def n_queen(size)
  $sum = 0
  matrix = [0] * size * size
  empty_board = Board.new(matrix, size)
  n_queen_iter(empty_board, 0)
  return $sum
end

def n_queen_iter(board, col)
  # profile the code
  result = RubyProf.profile do
    (0...board.size).each do |row|
      if board.available?(row, col)
        if col == board.size - 1
          $sum += 1
        else
          old_matrix = board.matrix.dup
          board.fill!(row, col)
          n_queen_iter(board, col + 1)
          board.matrix = old_matrix
        end
      end
    end
  end
end

if __FILE__ == $PROGRAM_NAME
  size = gets.to_i
  puts n_queen(size)

  printer = RubyProf::GraphPrinter.new(result)
  printer.print(STDOUT, {})
end

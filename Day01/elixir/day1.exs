defmodule Day1 do

  def part1([_head | tail], _target) when tail == [] do
  	nil
  end
  
  def part1([head | tail], target) do	
  	sums = for t <- tail, do: head + t
  	idx = Enum.find_index(sums, fn x -> x == target end)
  	if idx do
  	  Enum.fetch!(tail, idx) * head
  	else
  	  part1(tail, target)
  	end
  end


  def part2([_head | tail], _target) when length(tail) < 2 do
  	nil
  end

  def part2([head | tail], target) do
  	fs = first_sum(tail)
  	ps = first_prod(tail)
  	sums = for s <- fs, do: head + s
  	idx = Enum.find_index(sums, fn x -> x == target end)
  	if idx do
  	  Enum.fetch!(ps, idx) * head
  	else
  	  part2(tail, target)
  	end
  end

  def first_sum([_head | tail]) when tail == [] do
  	[]
  end
  def first_sum([head | tail]) do
  	sums = for t <- tail, do: head + t
  	sums ++ first_sum(tail)
  end

  def first_prod([_head | tail]) when tail == [] do
  	[]
  end
  def first_prod([head | tail]) do
  	prods = for t <- tail, do: head * t
  	prods ++ first_prod(tail)
  end

end

input = File.read!("../input.txt")
numbers = String.split(input)
vals = for n <- numbers, do: elem(Integer.parse(n), 0)

IO.puts("Part 1: #{Day1.part1(vals, 2020)}")

#IO.puts(["[", Enum.join(Day1.first_sum([4,3,2,1]), ", "), "]"])
#IO.puts(["[", Enum.join(Day1.first_prod([4,3,2,1]), ", "), "]"])

IO.puts("Part 2: #{Day1.part2(vals, 2020)}")

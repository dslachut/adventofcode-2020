defmodule Day2 do

	def part1(lns) do
		cts = for ln <- lns, do: part1_validate(ln)
		sum(cts)
	end

	def sum([head | tail]) when tail == [] do
		head
	end
	def sum([head | tail]) do
		head + sum(tail)
	end
	
	def part1_validate(ln) do
		{mini, maxi, letter, pwd} = List.to_tuple(ln)
		ct = length(Enum.filter(String.graphemes(pwd), fn x -> x == letter end))
		if (mini <= ct) && (ct <= maxi) do
			1
		else
			0
		end
	end

	def part2(lns) do
		cts = for ln <- lns, do: part2_validate(ln)
		sum(cts)
	end

	def part2_validate(ln) do
		{mini, maxi, letter, pwd} = List.to_tuple(ln)
		idx1 = mini - 1
		idx2 = maxi - 1
		chars = String.graphemes(pwd)
		case Enum.fetch(chars, idx1) do
			{:error, _reason} -> 0
			{:ok, ltr1}      -> part2_validate_step2(ltr1, idx2, letter, chars)
		end
	end
	def part2_validate_step2(ltr1, idx2, letter, chars) do
		case Enum.fetch(chars, idx2) do
			{:error, _reason} -> 
				if ltr1 == letter do
					1
				else
					0
				end
			{:ok, ltr2}      ->
				cond do
					ltr1 == ltr2 -> 0
					ltr1 == letter -> 1
					ltr2 == letter -> 1
					true -> 0
				end
		end
	end
	
	def parse_row(r) do
		rng = for m <- String.split(Enum.fetch!(r, 0), "-"), do: elem(Integer.parse(m), 0)
		letter = String.slice(Enum.fetch!(r, 1), 0..0)
		rng ++ [letter] ++ [Enum.fetch!(r, 2)]
	end
	
end

input = File.read!("../input.txt")
rows = String.split(input, "\n")
entries = for r <- Enum.take(rows, length(rows)-1), do: String.split(r)
parsed = for e <- entries, do: Day2.parse_row(e)

IO.puts(Day2.part1(parsed))
IO.puts(Day2.part2(parsed))

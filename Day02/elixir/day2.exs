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
	
	def parse_row(r) do
		rng_str = Enum.fetch!(r, 0)
		rng_splt = String.split(rng_str, "-")
		IO.puts(Enum.join([Enum.join(r, ", "), rng_str, Enum.join(rng_splt, ", ")], "; "))
		for m <- rng_splt, do: IO.puts(Integer.parse(m))
		rng = for m <- rng_splt, do: elem(Integer.parse(m), 0)
		letter = String.slice(Enum.fetch!(r, 1), 0..0)
		rng ++ [letter] ++ [Enum.fetch!(r, 2)]
	end
	
end

input = File.read!("../input.txt")
rows = String.split(input, "\n")
entries = for r <- rows, do: String.split(r)
#IO.puts(Enum.join(entries, "\n"))
parsed = for e <- entries, do: Day2.parse_row(e)

IO.puts(Day2.part1(parsed))

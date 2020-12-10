defmodule Day3 do
	def part1(field) do
		scoot(field, 0, 3, 1)
	end
	def part2(field) do
		a = scoot(field, 0, 1, 1)
		b = scoot(field, 0, 3, 1)
		c = scoot(field, 0, 5, 1)
		d = scoot(field, 0, 7, 1)
		e = scoot(field, 0, 1, 2)
		a*b*c*d*e
	end
	
	def scoot([], _pos, _r_stride, _d_stride) do
		0
	end
	def scoot([plane|field], pos, r_stride, d_stride) do
		next_pos = rem((pos + r_stride), length(plane))
		if Enum.fetch!(plane, pos) == "." do
			0 + downhill(field, next_pos, r_stride, d_stride)
		else
			1 + downhill(field, next_pos, r_stride, d_stride)
		end
	end
	def downhill(field, pos, r_stride, d_stride) do
		if d_stride > 1 do
			skip_row(field, pos, r_stride, d_stride, d_stride-1)
		else
			scoot(field, pos, r_stride, d_stride)
		end
	end
	def skip_row([], _pos, _r_stride, _d_stride, _skips) do
		0
	end
	def skip_row([_plane|field], pos, r_stride, d_stride, skips) do
		if skips <= 1 do
			scoot(field, pos, r_stride, d_stride)
		else
			skip_row(field, pos, r_stride, d_stride, skips-1)
		end
	end
end

input = File.read!("../input.txt")
lines = String.split(input, "\n")
rows = for l <- Enum.take(lines, length(lines)-1), do: String.split(l)
parsed = for r <- rows, do: String.graphemes(hd(r))
IO.puts(Day3.part1(parsed))
IO.puts(Day3.part2(parsed))

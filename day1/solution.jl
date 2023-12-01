
function parse_line(line)
    d_l = [d for d in line if isdigit(d)]
    # 🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮
    return parse(Int, d_l[1] * d_l[end])
end

function part1(input)
    res = 0
    for line in input
        res += parse_line(line)
    end
    return res
end

file = open("test_input.txt", "r")
input = readlines(file)
close(file)

println(part1(input))

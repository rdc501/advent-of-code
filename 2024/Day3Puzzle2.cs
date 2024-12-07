namespace _2024;

public class Day3Puzzle2
{
    private static bool _mulEnabled = true;
    
    public static string Execute()
    {
        _mulEnabled = true;
        
        var lines = File.ReadAllLines("inputs/day_three.txt");
        
        var muls = new List<(int, int, string)>();

        foreach (var line in lines)
        {
            ProcessLine(line, muls);
        }
        
        
        return muls.Select(mul => mul.Item1 * mul.Item2).Sum().ToString();
    }

    private static void ProcessLine(string line, List<(int, int, string)> muls)
    {
        for (var i = 0; i < line.Length; i++)
        {
            if (line[i..].StartsWith("do()"))
            {
                _mulEnabled = true;
            }

            if (line[i..].StartsWith("don't()"))
            {
                _mulEnabled = false;
            }
            
            if (_mulEnabled && line[i..].StartsWith("mul("))
            {
                var closingBracket = (int?)null;

                if (i + 7 < line.Length && line[i + 7] == ')')
                    closingBracket = 7;

                if (i + 8 < line.Length && line[i + 8] == ')')
                    closingBracket ??= 8;

                if (i + 9 < line.Length && line[i + 9] == ')')
                    closingBracket ??= 9;
                
                if (i + 10 < line.Length && line[i + 10] == ')')
                    closingBracket ??= 10;
                
                if (i + 11 < line.Length && line[i + 11] == ')')
                    closingBracket ??= 11;
                
                if (closingBracket is not null && i + closingBracket < line.Length)
                    processMul(line[(i+4)..(i+(int)closingBracket)], muls, line[i..(i + (int)closingBracket + 1)]);
            }
        }
    }

    private static void processMul(string line, List<(int, int, string)> muls, string rawMul)
    {
        var strings = line.Split(',');

        if (
            strings.Length != 2 ||
            strings[0].Length < 1 ||
            strings[0].Length > 3 ||
            strings[1].Length < 1 ||
            strings[1].Length > 3    
        )
            return;
        
        if (
            int.TryParse(strings[0], out int first) &&
            int.TryParse(strings[1], out int second)
        )
            muls.Add((first, second, rawMul));
    }
}
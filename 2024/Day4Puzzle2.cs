using System.Runtime.InteropServices.JavaScript;
using System.Text;
using System.Text.RegularExpressions;

namespace _2024;

public class Day4Puzzle2
{
    public static string Execute()
    {
        var lines = File.ReadAllLines("inputs/day4.txt");

        return FindAs(lines)
            .Select(x => HasDiagonals(x, lines))
            .Sum()
            .ToString();
    }

    private static List<(int row, int col)> FindAs(params string[] lines)
    {
        var result = new List<(int, int)> { };
        
        for (var rowIndex = 0; rowIndex < lines.Length; rowIndex++)
        {
            for (var colIndex = 0; colIndex < lines[0].Length; colIndex++)
            {
                if (lines[rowIndex][colIndex] == 'A')
                    result.Add((rowIndex, colIndex));
            }
        }
        
        return result;
    }

    private static int HasDiagonals((int row, int col) index, string[] lines)
    {
        var first = GetSubstring(
            index.row - 1,
            index.col - 1,
            index.row + 1,
            index.col + 1,
            lines
        );
        
        var second = GetSubstring(
            index.row - 1,
            index.col + 1,
            index.row + 1,
            index.col - 1,
            lines
        );
        
        return (first == "SM" || first == "MS") && 
               (second == "SM" || second == "MS") ? 1 : 0;
    }

    private static string GetSubstring(
        int startRow,
        int startCol,
        int endRow, 
        int endCol,
        string[] lines
    )
    {
        var result = string.Empty;

        if (startRow < 0 || startRow >= lines.Length)
            return result;
        
        if (startCol < 0 || startCol >= lines[0].Length)
            return result;

        if (endRow < 0 || endRow >= lines.Length)
            return result;
        
        if (endCol < 0 || endCol >= lines[0].Length)
            return result;
        
        return $"{lines[startRow][startCol]}{lines[endRow][endCol]}";
    }
}